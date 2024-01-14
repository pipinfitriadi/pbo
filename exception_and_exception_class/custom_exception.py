#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.


class NegativeNumberException(RuntimeError):
    def __init__(self, age, *args: object):
        super().__init__(*args)
        self.age = age
