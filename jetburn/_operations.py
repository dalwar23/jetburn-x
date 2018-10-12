#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

# Import python libraries
import sys
import datetime
from pyrainbowterm import *
import inquirer
from pyfiglet import Figlet
import re

# Import local python libraries
import _release_info as release_info

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


reload(sys)
sys.setdefaultencoding('utf8')


# Create initial message
def __initial_message():
    """
    This function creates initial message and prints it
    """
    marker = '\U0001f6ea'  # Must be single character
    # Print a general help message
    text_to_render = 'jetburn'
    fig_let = Figlet(font='banner3')

    date_time = datetime.datetime.now()
    _print_string = "Airline tickets explorer program"
    _print_string += " [" + date_time.strftime("%d-%B-%Y %H:%M:%S") + "]"
    # Author message display
    _author_string = "Author: {} ({})".format(release_info.__author__, release_info.__email__)
    # Help message
    _help_string = "Need help? jetburn -h/--help"
    # Create prefix and suffix
    prefix = marker * 2 + ' '
    suffix = ' ' + marker * 2
    print_string = prefix + _print_string
    version_message = prefix + release_info.__package__ + " v" + release_info.__version__
    author_string = prefix + _author_string
    help_string = prefix + _help_string
    # Take max
    str_length = max([len(print_string), len(version_message), len(author_string), len(help_string)]) + 3
    # Create padding
    print_string = print_string + " " * (str_length - len(print_string) - len(suffix)) + suffix
    version_message = version_message + " " * (str_length - len(version_message) - len(suffix)) + suffix
    author_string = author_string + " " * (str_length - len(author_string) - len(suffix)) + suffix
    help_string = help_string + " " * (str_length - len(help_string) - len(suffix)) + suffix
    # Print
    line_block = marker * str_length
    print(fig_let.renderText(text_to_render), color='green')
    print(line_block, print_string, version_message, author_string, help_string, line_block, sep='\n')


# Create a list of questions
def __get_trip_info(round_trip=None):
    """
    This function generates a set of questions for the user

    :return: (dict) A python dict
    """
    date_reg_ex = '(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/]' \
                  '(0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])' \
                  '(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)'
    if round_trip:
        questions = [
            inquirer.Text(name='origin', message='Please provide origin airport \U0001f6eb ',
                          validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
            inquirer.Text(name='destination', message='Please provide destination airport \U0001f6ec ',
                          validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
            inquirer.Text(name='fly_out_date', message='Please provide fly out date (dd/mm/yyyy) \U0001f4c5 ',
                          validate=lambda _, x: re.match(date_reg_ex, x)),
            inquirer.Text(name='fly_back_date', message='Please provide fly back date (dd/mm/yyyy) \U0001f4c5 ',
                          validate=lambda _, x: re.match(date_reg_ex, x)),
            inquirer.Text(name='adults', message='Number of adults (>16 Years)? \U0001f468 ', default='1'),
            inquirer.Text(name='teens', message='Number of teens (12-15 Years)? \U0001f466 ', default='0'),
            inquirer.Text(name='children', message='Number of children (2-11 Years)? \U0001f9d2 ', default='0'),
            inquirer.Text(name='infants', message='Number of infants (<2 Years)? \U0001f476 ', default='0'),
        ]
    else:
        questions = [
            inquirer.Text(name='origin', message='Please provide origin airport \U0001f6eb ',
                          validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
            inquirer.Text(name='destination', message='Please provide destination airport \U0001f6ec ',
                          validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
            inquirer.Text(name='fly_out_date', message='Please provide fly out date (dd/mm/yyyy) \U0001f4c5 ',
                          validate=lambda _, x: re.match(date_reg_ex, x)),
            inquirer.Text(name='adults', message='Number of adults (>16 Years)? \U0001f468 ', default='1'),
            inquirer.Text(name='teens', message='Number of teens (12-15 Years)? \U0001f466 ', default='0'),
            inquirer.Text(name='children', message='Number of children (2-11 Years)? \U0001f9d2 ', default='0'),
            inquirer.Text(name='infants', message='Number of infants (<2 Years)? \U0001f476 ', default='0'),
        ]
    # Prompt the questions
    answers = inquirer.prompt(questions)
    if round_trip:
        answers = answers
    else:
        answers['fly_back_date'] = ''

    # Return
    return answers


# Create trip status question
def __trip_status():
    """
    This function helps to determine trip status (one way or round trip)

    :return: (dict) Python dictionary
    """
    # Create trip question
    question = [
        inquirer.Text(name='trip_status', message='Round Trip? ([Y]/n) \U0001f5d8 ', default='Y',
                      validate=lambda _, x: re.match('^[a-zA-Z]$', x))
    ]

    answer = inquirer.prompt(question)

    if answer['trip_status'] == 'Y' or answer['trip_status'] == 'y':
        return True
    else:
        return False


# Check if currency is a valid currency or not
def __is_valid_currency(currency=None):
    """
    This function check if the currency is in the valid currency list or not

    :param currency: (str) Three letter upper case currency code
    :return: (boolean) True or false
    """
    # List valid Currencies
    valid_currencies = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT',
                        'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYR', 'BZD',
                        'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF',
                        'DKK', 'DOP', 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP',
                        'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS',
                        'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF',
                        'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD',
                        'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MTL', 'MUR', 'MVR', 'MWK', 'MXN',
                        'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP',
                        'PKR', 'PLN', 'PYG', 'QAR', 'QUN', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG',
                        'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT',
                        'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND',
                        'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR',
                        'ZMK', 'ZMW', 'ZWL']
    # Check if given currency is valid or not
    if currency in valid_currencies:
        return True
    else:
        return False
