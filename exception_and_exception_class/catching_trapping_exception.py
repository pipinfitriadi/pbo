#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

import sys


print('Previous code with exception handling')

try:
    number = int(
        input('Please enter the number: ')
    )
except ValueError:
    print('Error.. numbers only')
    sys.exit()

print('You have entered number', number)
