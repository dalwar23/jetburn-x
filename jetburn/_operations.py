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
from tabulate import tabulate
from datapackage import Package
import requests

# Import local python libraries
import _release_info as release_info

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
            inquirer.Text(name='origin', message='Origin airport \U0001f6eb ',
                          validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
            inquirer.Text(name='destination', message='Destination airport \U0001f6ec ',
                          validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
            inquirer.Text(name='fly_out_date', message='Fly out date (dd/mm/yyyy) \U0001f4c5 ',
                          validate=lambda _, x: re.match(date_reg_ex, x)),
            inquirer.Text(name='fly_back_date', message='Fly back date (dd/mm/yyyy) \U0001f4c5 ',
                          validate=lambda _, x: re.match(date_reg_ex, x)),
            inquirer.Text(name='adults', message='Adults (>16 Years)? \U0001f468 ', default='1'),
            inquirer.Text(name='teens', message='Teens (12-15 Years)? \U0001f466 ', default='0'),
            inquirer.Text(name='children', message='Children (2-11 Years)? \U0001f9d2 ', default='0'),
            inquirer.Text(name='infants', message='Infants (<2 Years)? \U0001f476 ', default='0'),
        ]
    else:
        questions = [
            inquirer.Text(name='origin', message='Origin airport \U0001f6eb ',
                          validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
            inquirer.Text(name='destination', message='Destination airport \U0001f6ec ',
                          validate=lambda _, x: re.match('^[a-zA-Z]{3}$', x)),
            inquirer.Text(name='fly_out_date', message='Fly out date (dd/mm/yyyy) \U0001f4c5 ',
                          validate=lambda _, x: re.match(date_reg_ex, x)),
            inquirer.Text(name='adults', message='Adults (>16 Years)? \U0001f468 ', default='1'),
            inquirer.Text(name='teens', message='Teens (12-15 Years)? \U0001f466 ', default='0'),
            inquirer.Text(name='children', message='Children (2-11 Years)? \U0001f9d2 ', default='0'),
            inquirer.Text(name='infants', message='Infants (<2 Years)? \U0001f476 ', default='0'),
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
