#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

class Sepeda:
    total_roda: int

    def __init__(self, total_roda: int):
        self.total_roda = total_roda

    def get_total_roda(self) -> int:
        return self.total_roda


s = Sepeda(3)
print(s.get_total_roda())
