#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTemplate

api = TheHiveApi('http://<thehive_url>:9000', 'username', 'password', {'http': '', 'https': ''})

# Get the template by it's name
print('Fetch case template')
print('-----------------------------')
template = api.get_case_template('Phishing')

caseTemplate = CaseTemplate(json=template)
print(caseTemplate.jsonify())
print('')


print('Create case from template')
print('-----------------------------')
case = Case(title='From TheHive4Py based on the Phishing template', description='N/A', tlp=2, template=caseTemplate)
print(case.jsonify())

print('Create Case')
print('-----------------------------')
response = api.create_case(case)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)
