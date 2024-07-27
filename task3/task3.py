import json
import sys
from pprint import pp


def set_value(tests: list):
    for test in tests:
        if 'value' in test:
            test['value'] = values_dict[test['id']]
        if 'values' in test:
            set_value(test['values'])


values_file, tests_file, report_file = sys.argv[1:]

with open(values_file) as f:
    values = json.load(f)
    values_dict = {test['id'] : test['value'] for test in values['values']}

with open(tests_file) as f:
    tests = json.load(f)['tests']

set_value(tests)
report_dict = {'tests': tests}

with open(report_file, 'w') as f:
    json.dump(report_dict, f, indent=2)

