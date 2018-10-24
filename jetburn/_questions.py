#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

# Import python libraries
import sys
import inquirer
import re

# Import local python libraries
import _icons as icon

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'

# LINUX/MAC
# Date generation regular expression
date_reg_ex = '(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/]' \
              '(0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|' \
              '32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)'
# Generate questions for flight search information
# -------------------- Round Trip ---------------------------------------------------------------
linux_round_trip_questions = [
    inquirer.Text(name='origin', message='Origin airport ' + icon.departure,
                  validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
    inquirer.Text(name='destination', message='Destination airport ' + icon.arrival,
                  validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
    inquirer.Text(name='fly_out_date', message='Fly out date (dd/mm/yyyy) ' + icon.calendar,
                  validate=lambda _, x: re.match(date_reg_ex, x)),
    inquirer.Text(name='fly_back_date', message='Fly back date (dd/mm/yyyy) ' + icon.calendar,
                  validate=lambda _, x: re.match(date_reg_ex, x)),
    inquirer.Text(name='adults', message='Adults (>16 Years)? ' + icon.adult, default='1'),
    inquirer.Text(name='teens', message='Teens (12-15 Years)? ' + icon.teen, default='0'),
    inquirer.Text(name='children', message='Children (2-11 Years)? ' + icon.child, default='0'),
    inquirer.Text(name='infants', message='Infants (<2 Years)? ' + icon.infant, default='0'),
]
# -------------------- One Way --------------------------------------------------------------------
linux_one_way_questions = [
    inquirer.Text(name='origin', message='Origin airport ' + icon.departure,
                  validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
    inquirer.Text(name='destination', message='Destination airport ' + icon.arrival,
                  validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
    inquirer.Text(name='fly_out_date', message='Fly out date (dd/mm/yyyy) ' + icon.calendar,
                  validate=lambda _, x: re.match(date_reg_ex, x)),
    inquirer.Text(name='adults', message='Adults (>16 Years)? ' + icon.adult, default='1'),
    inquirer.Text(name='teens', message='Teens (12-15 Years)? ' + icon.teen, default='0'),
    inquirer.Text(name='children', message='Children (2-11 Years)? ' + icon.child, default='0'),
    inquirer.Text(name='infants', message='Infants (<2 Years)? ' + icon.infant, default='0'),
]

# WINDOWS
# Generate questions for flight search information
# ----------------------- Round Trip ---------------------------------------------------------------
windows_round_trip_questions = []