#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

import logging

from custom_exception import NegativeNumberException


def enter_age(age):
    if age < 1:
        raise NegativeNumberException(
            age, 'Only positive integers are allowed'
        )
    if age % 2 == 0:
        logging.info('Age is Even')
    else:
        logging.info('Age is Odd')


try:
    num = int(input('Enter your age: '))
    enter_age(num)
    num/0
except NegativeNumberException as error:
    logging.error(error, error.age)
except Exception:
    logging.warning('Something is wrong')
