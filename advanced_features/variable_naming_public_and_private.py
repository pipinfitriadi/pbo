#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

class GetSet:
    instance_count = 0  # public
    _satu_underscore = 1
    __mangled_name = 'no privacy!'

    def get_mangled_name(self):
        return self.__mangled_name + ' <- Ini bisa diambil'


print(GetSet.instance_count)
print(GetSet().get_mangled_name())
print(GetSet._satu_underscore)
print(GetSet.__mangled_name)  # Ini pasti error, tidak usah panik
