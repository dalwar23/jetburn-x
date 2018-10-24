#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

# Import python libraries
import sys
import datetime
from pyrainbowterm import *
from pyfiglet import Figlet
import re
from tabulate import tabulate
from datapackage import Package
import requests
import platform

# Import local python libraries
import _release_info as release_info
import _questions as questions
import _icons as icon

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


reload(sys)
sys.setdefaultencoding('utf8')


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


# Create initial message
def __initial_message():
    """
    This function creates initial message and prints it

    """
    # Assign marker
    if platform.system() == 'Windows':
        marker = "="
    else:
        marker = icon.airplane  # Must be single character
    # Print a general help message
    text_to_render = 'jetburn'
    fig_let = Figlet(font='banner3')

    date_time = datetime.datetime.now()
    _print_string = "Airline ticket explorer program"
    _print_string += " [" + date_time.strftime("%d-%B-%Y %H:%M:%S") + "]"
    # Author message display
    _author_string = "Author: {} ({})".format(release_info.__author__, release_info.__email__)
    # Help message
    _help_string = "Need help? jetburn -h/--help"
    # Warning message
    _warn_line0 = '..::DISCLAIMER::..'
    _warn_line1 = 'This program is not an airline ticket booking system and has'
    _warn_line2 = 'no partnership with any airlines or ticketing agents'
    # Create prefix and suffix
    prefix = marker * 2 + ' '
    suffix = ' ' + marker * 2
    print_string = prefix + _print_string
    version_release = " v" + release_info.__version__ + "." + release_info.__release__
    license = release_info.__license__
    version_message = prefix + release_info.__package__ + ": " + version_release + " / " + "License: " + license
    author_string = prefix + _author_string
    help_string = prefix + _help_string
    warn_line1 = prefix + _warn_line1
    warn_line2 = prefix + _warn_line2
    # Take max
    str_length = max([len(print_string), len(version_message), len(author_string), len(help_string),
                      len(warn_line1), len(warn_line2)]) + 3
    blank_space = str_length -(len(prefix) + len(suffix))
    warn_space = blank_space - len(_warn_line0)
    if warn_space % 2 == 0:
        warn_space_before = warn_space/2
        warn_space_after = warn_space/2
    else:
        warn_space_before = warn_space/2
        warn_space_after = warn_space/2 + 1
    # Create padding
    print_string = print_string + " " * (str_length - len(print_string) - len(suffix)) + suffix
    version_message = version_message + " " * (str_length - len(version_message) - len(suffix)) + suffix
    author_string = author_string + " " * (str_length - len(author_string) - len(suffix)) + suffix
    help_string = help_string + " " * (str_length - len(help_string) - len(suffix)) + suffix
    warn_line1_padding = " " * (str_length - len(warn_line1) - len(suffix))
    warn_line2_padding = " " * (str_length - len(warn_line2) - len(suffix))

    # Print
    line_block = marker * str_length
    print(fig_let.renderText(text_to_render), color='green')
    print(line_block, print_string, version_message, author_string, help_string, line_block, sep='\n')
    print (prefix, end='')
    print(' ' * warn_space_before, end='')
    print(_warn_line0, color='orange', end='')
    print(' ' * warn_space_after, end='')
    print(suffix)
    print(prefix, end='')
    print(_warn_line1 + warn_line1_padding, color='orange', end='')
    print(suffix)
    print(prefix, end='')
    print(_warn_line2 + warn_line2_padding, color='orange', end='')
    print(suffix, line_block, sep='\n')


# Create a list of questions
def __get_trip_info(round_trip=None):
    """
    This function generates a set of questions for the user

    :return: (dict) A python dict
    """
    # Import required libraries
    if platform.system() == 'Windows':
        try:
            import PyInquirer
        except ImportError as e:
            print('Python module import error! ERROR: {}'.format(e), log_type='error', color='red')
            sys.exit(1)
        # Questions for flight search
        if round_trip:
            flight_search_questions = questions.windows_questions
        else:
            flight_search_questions = questions.windows_questions.__delitem__(3)
        # Prompt the questions
        answers = PyInquirer.prompt(flight_search_questions)
        if round_trip:
            answers = answers
        else:
            answers['fly_back_date'] = ''

        # Return
        return answers
    else:
        try:
            import inquirer
        except ImportError as e:
            print('Python module import error. ERROR: {}', format(e), log_type='error', color='red')
            sys.exit(1)
        # Questions for flight search
        if round_trip:
            flight_search_questions = questions.linux_round_trip_questions
        else:
            flight_search_questions = questions.linux_one_way_questions
        # Prompt the questions
        answers = inquirer.prompt(flight_search_questions)
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
    # Import required python library
    if platform.system() == 'Windows':
        try:
            import PyInquirer
        except ImportError as e:
            print('Python module import error! ERROR: {}'.format(e), log_type='error', color='red')
            sys.exit(1)

        # Create trip type [one way, round trip] question
        question = [
            {
                'type': 'confirm',
                'message': 'Round Trip? ',
                'name': 'trip_status',
                'default': True
            }
        ]
        answer = PyInquirer.prompt(question)
        if answer['trip_status']:
            return True
        else:
            return False
    else:
        try:
            import inquirer
        except ImportError as e:
            print('Python module import error. ERROR: {}', format(e), log_type='error', color='red')
            sys.exit(1)

        # Create trip type [one way, round trip] question
        question = [
            inquirer.Text(name='trip_status', message='Round Trip? ([Y]/n) ' + icon.cycle, default='Y',
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
    # Check if given currency is valid or not
    if currency in valid_currencies:
        return True
    else:
        return False


# List the names of valid currencies according to their internation currency code
def __get_currency_names():
    """
    This function generates human readable names for the valid currency codes

    :return: <>
    """
    # Create a package for currency data
    print('Collecting currency information from internet.....', log_type='info')
    package = Package('https://datahub.io/core/currency-codes/datapackage.json')
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/json':
            url = resource.descriptor['path']
            print('Requesting ISO 4217 currency codes.....', log_type='info')
            response = requests.get(url)
            if response.status_code == 200:
                print('ISO 4217 currency codes received.', log_type='info')
                currencies = response.json()
            else:
                print('Currency codes can not be obtained over internet.', log_type='error', color='red')
                sys.exit(1)
    # Currency table
    currency_table_header = ['Country', 'Currency']
    currency_table_rows = []
    print('Creating valid currency table.....', log_type='info')
    for currency_code in valid_currencies:
        for entry in currencies:
            if entry['AlphabeticCode'] == currency_code:
                country = entry['Entity']
                currency = entry['Currency']
                currency_with_code = currency_code + " (" + currency + ")"
            else:
                pass
        currency_table_row = [country, currency_with_code]
        currency_table_rows.append(currency_table_row)
    print(tabulate(currency_table_rows, headers=currency_table_header, tablefmt='grid'), color='green')


# List all the valid airport codes and full airport names
def __get_airport_names_by_city(search_city=None):
    """
    This function searches for IATA codes

    :param search_city: (str) pattern to search for in airport names for IATA code
    :return: (str) three letter IATA code
    """
    # TODO Add country name
    # Create a package for currency data
    print('Collecting airport information from internet.....', log_type='info')
    package = Package('https://datahub.io/core/airport-codes/datapackage.json')
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/json':
            url = resource.descriptor['path']
            print('Requesting IATA airport codes.....', log_type='info')
            response = requests.get(url)
            if response.status_code == 200:
                print('IATA airport codes received.', log_type='info')
                airports = response.json()
            else:
                print('Airport codes can not be obtained over internet.', log_type='error', color='red')
                sys.exit(1)

    # Find location
    found_airports = []
    for airport in airports:
        # result = re.search(search_pattern.lower(), airport['name'].lower())
        if airport['municipality'] is not None:
            if search_city.lower() in airport['municipality'].lower():
                result = True
            else:
                result = False
        elif airport['municipality'] is None or airport['municipality'] == 'null':
            result = False
        else:
            pass

        if result:
            found_airports.append(airport)

    # Sort out only the airports
    airport_table_headers = ['Airport Name', 'City', 'IATA Code']
    airport_table_rows = []
    for airport in found_airports:
        if airport['iata_code'] == 'null' or airport['iata_code'] == 'None' or airport['iata_code'] is None:
            pass
        else:
            airport_table_row = [airport['name'], airport['municipality'], airport['iata_code']]
            airport_table_rows.append(airport_table_row)
    print(tabulate(airport_table_rows, headers=airport_table_headers, tablefmt='grid'), color='green')
