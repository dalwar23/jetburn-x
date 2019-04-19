#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import future print function and unicode literals for python2.7 support
from __future__ import print_function, unicode_literals

# Import builtin python libraries
import sys
import datetime

# Import external python libraries
from pyfiglet import Figlet
from tabulate import tabulate
from datapackage import Package
import requests
import PyInquirer
import wasabi
from wasabi import color

# Import local custom python libraries
from . import _version as release_info
from . import _questions as questions

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'

# Take care of character encoding for python2
if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    pass  # noqa


# List valid Currencies
valid_currencies = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT",
                    "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYR", "BZD",
                    "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF",
                    "DKK", "DOP", "DZD", "EEK", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP",
                    "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS",
                    "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF",
                    "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD",
                    "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MTL", "MUR", "MVR", "MWK", "MXN",
                    "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP",
                    "PKR", "PLN", "PYG", "QAR", "QUN", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG",
                    "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT",
                    "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND",
                    "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "YER", "ZAR",
                    "ZMK", "ZMW", "ZWL"]

# Create msg from wasabi printer class
msg = wasabi.Printer()


# Create initial message
def initial_message():
    """
    This function creates initial message and prints it

    """

    # Assign marker
    horizontal_marker = "-"
    vertical_marker = "|"

    # Print a general help message
    text_to_render = " "*2 + "jetburn"
    fig_let = Figlet(font="speed")

    date_time = datetime.datetime.now()
    _print_string = "Airline ticket explorer program"
    _print_string += " [" + date_time.strftime("%d-%B-%Y %H:%M:%S") + "]"
    # Author message display
    _author_string = "Author: {} ({})".format(release_info.__author__, release_info.__author_email__)
    # Help message
    _help_string = "Need help? jetburn -h/--help"
    # Warning message
    _warn_line0 = "..:: DISCLAIMER ::.."
    _warn_line1 = "This program is not an airline ticket booking system and"
    _warn_line2 = "has no affiliation with any airlines or ticketing agents"
    # Create prefix and suffix
    prefix = vertical_marker + " "
    suffix = " " + vertical_marker
    print_string = prefix + _print_string
    version_release = release_info.__full_version__
    license_ = release_info.__app_license__
    version_message = prefix + "Version: " + version_release + " / " + "License: " + license_
    author_string = prefix + _author_string
    help_string = prefix + _help_string
    warn_line1 = prefix + _warn_line1
    warn_line2 = prefix + _warn_line2
    # Take max
    str_length = max([len(print_string), len(version_message), len(author_string), len(help_string),
                      len(warn_line1), len(warn_line2)]) + 2
    blank_space = str_length - (len(prefix) + len(suffix))
    warn_space = blank_space - len(_warn_line0)
    if warn_space % 2 == 0:
        warn_space_before = int(warn_space/2)
        warn_space_after = int(warn_space/2)
    else:
        warn_space_before = int(warn_space/2)
        warn_space_after = int(warn_space/2 + 1)
    # Create padding
    print_string = print_string + " " * (str_length - len(print_string) - len(suffix)) + suffix
    version_message = version_message + " " * (str_length - len(version_message) - len(suffix)) + suffix
    author_string = author_string + " " * (str_length - len(author_string) - len(suffix)) + suffix
    help_string = help_string + " " * (str_length - len(help_string) - len(suffix)) + suffix
    warn_line1_padding = " " * (str_length - len(warn_line1) - len(suffix))
    warn_line2_padding = " " * (str_length - len(warn_line2) - len(suffix))

    # Print information
    line_block = "+" + horizontal_marker * (str_length-2) + "+"
    header = color(fig_let.renderText(text_to_render), fg="green")
    print(header)
    print(line_block, print_string, author_string, version_message, help_string, line_block, sep="\n")
    # Disclaimer
    print(prefix, end="")
    print(" " * warn_space_before, end="")
    line_0 = color(_warn_line0, fg="yellow")
    line_1 = color(_warn_line1 + warn_line1_padding, fg="yellow")
    line_2 = color(_warn_line2 + warn_line2_padding, fg="yellow")
    print(line_0, end="")
    print(" " * warn_space_after, end="")
    print(suffix)
    print(prefix, end="")
    print(line_1, end="")
    print(suffix)
    print(prefix, end="")
    print(line_2, end="")
    print(suffix, line_block, sep="\n")


# Get version info
def get_info():
    """
    This function will show the current version

    :return: (str) Package information
    """

    package_author = release_info.__author__
    author_email = release_info.__author_email__
    package_name = release_info.__package_name__
    package_license = release_info.__app_license__
    current_version = release_info.__full_version__

    msg.good("Package: {}".format(package_name))
    msg.good("Version: {}".format(current_version))
    msg.good("License: {}".format(package_license))
    msg.info("Author: {} ({})".format(package_author, author_email))


# Create a list of questions
def get_trip_info(round_trip=None):
    """
    This function generates a set of questions for the user

    :param round_trip: (boolean) True or False for round trip
    :return: (dict) A python dict
    """

    # Get flight search questions
    flight_search_questions = questions.get_questions(round_trip=round_trip)

    # Prompt the questions
    _answers = PyInquirer.prompt(flight_search_questions)

    # assign empty date for one way
    if round_trip:
        answers = _answers
    else:
        _answers["fly_back_date"] = ""
        answers = _answers

    # Return
    return answers


# Create trip status question
def trip_status():
    """
    This function helps to determine trip status (one way or round trip)

    :return: (dict) Python dictionary
    """

    # Create trip type [one way, round trip] question
    question = [
        {
            "type": "confirm",
            "message": "Round Trip?",
            "name": "trip_status",
            "default": True
        }
    ]
    answer = PyInquirer.prompt(question)

    if answer["trip_status"]:
        return True
    else:
        return False


# Check if currency is a valid currency or not
def is_valid_currency(currency=None):
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
def get_currency_names():
    """
    This function generates human readable names for the valid currency codes

    :return: (list) Currency name
    """

    # Create a package for currency data
    msg.info("Collecting currency information.....")
    package = Package("https://datahub.io/core/currency-codes/datapackage.json")
    for resource in package.resources:
        if resource.descriptor["datahub"]["type"] == "derived/json":
            url = resource.descriptor["path"]
            msg.info("Requesting ISO 4217 currency codes.....")
            response = requests.get(url)
            if response.status_code == 200:
                msg.good("ISO 4217 currency codes received")
                currencies = response.json()
            else:
                msg.fail("Currency codes can not be obtained at this moment.")
                sys.exit(-1)
    # Currency table
    currency_table_header = ["Country", "Currency"]
    currency_table_rows = []
    msg.info("Creating valid currency table.....")
    for currency_code in valid_currencies:
        for entry in currencies:
            if entry["AlphabeticCode"] == currency_code:
                country = entry["Entity"]
                currency = entry["Currency"]
                currency_with_code = currency_code + " (" + currency + ")"
            else:
                pass  # noqa
        currency_table_row = [country, currency_with_code]
        currency_table_rows.append(currency_table_row)
    formatted_table = color(tabulate(currency_table_rows, headers=currency_table_header, tablefmt="grid"), fg="cyan")
    print(formatted_table)


# List all the valid airport codes and full airport names
def get_airport_names_by_city(search_city=None):
    """
    This function searches for IATA codes

    :param search_city: (str) pattern to search for in airport names for IATA code
    :return: (str) three letter IATA code
    """

    # TODO Add country name
    # Create a package for currency data
    msg.info("Collecting airport information.....")
    package = Package("https://datahub.io/core/airport-codes/datapackage.json")
    for resource in package.resources:
        if resource.descriptor["datahub"]["type"] == "derived/json":
            url = resource.descriptor["path"]
            msg.info("Requesting IATA airport codes.....")
            response = requests.get(url)
            if response.status_code == 200:
                msg.good("IATA airport codes received")
                airports = response.json()
            else:
                msg.fail("Airport IATA codes can not be obtained at this moment!")
                sys.exit(-1)

    # Find location
    found_airports = []
    for airport in airports:
        if airport["municipality"] is not None:
            if search_city.lower() in airport["municipality"].lower():
                result = True
            else:
                result = False
        elif airport["municipality"] is None or airport["municipality"] == "null":
            result = False
        else:
            pass  # noqa

        if result:
            found_airports.append(airport)

    # Sort out only the airports
    airport_table_headers = ["Airport Name", "City", "IATA Code"]
    airport_table_rows = []
    for airport in found_airports:
        if airport["iata_code"] == "null" or airport["iata_code"] == "None" or airport["iata_code"] is None:
            pass  # noqa
        else:
            airport_table_row = [airport["name"], airport["municipality"], airport["iata_code"]]
            airport_table_rows.append(airport_table_row)
    formatted_table = color(tabulate(airport_table_rows, headers=airport_table_headers, tablefmt="grid"), fg="cyan")
    print(formatted_table)
