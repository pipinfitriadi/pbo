#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

import yaml

my_dict = {'a': 2, 'b': 4, 'c': 6}
my_list = [1, 2, 3, 4, 5]
my_tuple = ('x', 'y', 'z')

print(yaml.dump(my_dict, default_flow_style=False))
print(yaml.dump(my_list, default_flow_style=False))
print(yaml.dump(my_tuple, default_flow_style=False))
