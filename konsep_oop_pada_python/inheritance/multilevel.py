#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

# Parent class
class Hewan:
    def bicara(self):
        print('Hewan berbicara')


# Child class mewarisi dari class Hewan
class Kucing(Hewan):
    def meaow(self):
        print('meaow....meaow....meaow..!!!')


# Child class AnakKucing mewarisi dari class hewan
class AnakKucing(Kucing):
    def minum(self):
        print('minum susu')


a_k = AnakKucing()
a_k.bicara()
a_k.meaow()
a_k.minum()
