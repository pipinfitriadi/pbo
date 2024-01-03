#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

from typing import Self


class SumList(object):
    def __init__(self, my_list: list):
        self.my_list = my_list

    def __add__(self, other: Self) -> Self:
        new_list = [x + y for x, y in zip(self.my_list, other.my_list)]

        return SumList(new_list)

    def __repr__(self) -> str:
        return str(self.my_list)


aa = SumList([3, 6, 9, 12, 15])
bb = SumList([100, 200, 300, 400, 500])
cc = aa + bb  # cc = aa.__add__(bb)
print(cc)
