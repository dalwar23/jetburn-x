#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

# Import python libraries
from pprint import pprint
import re
from PyInquirer import Validator, ValidationError

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


# Date generation regular expression
date_reg_ex = '(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/]' \
              '(0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|' \
              '32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)'


# Airport IATA code validator
class IataCodeValidator(Validator):
    def __init__(self):
        pass

    def validate(self, document):
        ok = re.match('^[a-zA-Z]{3}$', document.text)
        if not ok:
            raise ValidationError(
                message='Please use 3 letter IATA airport codes. To find out IATA codes '
                        'use: jetburn --find-airport <city_name>',
                cursor_position=len(document.text)
            )


# Date validator
class DateValidator(Validator):
    def __init__(self):
        pass

    def validate(self, document):
        ok = re.match(date_reg_ex, document.text)
        if not ok:
            raise ValidationError(
                message='Please enter date in correct format',
                cursor_position=len(document.text)  # Moves cursor to the end
            )


class NumberValidator(Validator):
    def __init__(self):
        pass

    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text)
            )


# Generate questions for flight search information
one_way_questions = [
    {
        'type': 'input',
        'name': 'origin',
        'message': 'Origin airport:',
        'validate': IataCodeValidator
    },
    {
        'type': 'input',
        'name': 'destination',
        'message': 'Destination airport:',
        'validate': IataCodeValidator
    },
    {
        'type': 'input',
        'name': 'fly_out_date',
        'message': 'Fly out date (dd/mm/yyyy):',
        'validate': DateValidator
    },
    {
        'type': 'input',
        'name': 'adults',
        'message': 'Adults (>16 Years)?',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': '1'
    },
    {
        'type': 'input',
        'name': 'teens',
        'message': 'Teens (12-15 Years)?',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': '0'
    },
    {
        'type': 'input',
        'name': 'children',
        'message': 'Children (2-11 Years)?',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': '0'
    },
    {
        'type': 'input',
        'name': 'infants',
        'message': 'Infants (<2 Years)?',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': '0'
    }
]
fly_back_question = {
        'type': 'input',
        'name': 'fly_back_date',
        'message': 'Fly back date (dd/mm/yyyy):',
        'validate': DateValidator
}


def __get_questions(round_trip=None):
    """
    This function returns a set of questions based on trip type

    :param round_trip: (boolean) If it's a round trip or not
    :return: (list) python list of dictionary based questions
    """
    if round_trip:
        one_way_questions.insert(3, fly_back_question)
        round_trip_questions = one_way_questions
        return round_trip_questions
    else:
        return one_way_questions


# # Generate questions for flight search information
# # -------------------- Round Trip ---------------------------------------------------------------
# linux_round_trip_questions = [
#     inquirer.Text(name='origin', message='Origin airport ' + icon.departure,
#                   validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
#     inquirer.Text(name='destination', message='Destination airport ' + icon.arrival,
#                   validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
#     inquirer.Text(name='fly_out_date', message='Fly out date (dd/mm/yyyy) ' + icon.calendar,
#                   validate=lambda _, x: re.match(date_reg_ex, x)),
#     inquirer.Text(name='fly_back_date', message='Fly back date (dd/mm/yyyy) ' + icon.calendar,
#                   validate=lambda _, x: re.match(date_reg_ex, x)),
#     inquirer.Text(name='adults', message='Adults (>16 Years)? ' + icon.adult, default='1'),
#     inquirer.Text(name='teens', message='Teens (12-15 Years)? ' + icon.teen, default='0'),
#     inquirer.Text(name='children', message='Children (2-11 Years)? ' + icon.child, default='0'),
#     inquirer.Text(name='infants', message='Infants (<2 Years)? ' + icon.infant, default='0'),
# ]
# # -------------------- One Way --------------------------------------------------------------------
# linux_one_way_questions = [
#     inquirer.Text(name='origin', message='Origin airport ' + icon.departure,
#                   validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
#     inquirer.Text(name='destination', message='Destination airport ' + icon.arrival,
#                   validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
#     inquirer.Text(name='fly_out_date', message='Fly out date (dd/mm/yyyy) ' + icon.calendar,
#                   validate=lambda _, x: re.match(date_reg_ex, x)),
#     inquirer.Text(name='adults', message='Adults (>16 Years)? ' + icon.adult, default='1'),
#     inquirer.Text(name='teens', message='Teens (12-15 Years)? ' + icon.teen, default='0'),
#     inquirer.Text(name='children', message='Children (2-11 Years)? ' + icon.child, default='0'),
#     inquirer.Text(name='infants', message='Infants (<2 Years)? ' + icon.infant, default='0'),
# ]
