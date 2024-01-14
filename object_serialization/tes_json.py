#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

import json
from pprint import pprint

SPACE: str = '+' * 100

with open('data1.json') as json_file:
    data1 = json.load(json_file)

pprint(data1)
print(SPACE)
print(type(data1))
print(SPACE)
data1['neykey'] = 9.04050

with open('data1.json', 'w') as json_file:
    json.dump(data1, json_file)

print(data1)
