#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import print options for python2 and python3 compatibility
from __future__ import print_function

# Import builtin python libraries
import sys
import argparse

# Import external python libraries
import requests
import wasabi

# Import local python library
from . import _operations as operations
from . import _flight_parser as flight_parser

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'

# Create msg from wasabi printer class
msg = wasabi.Printer()


# Package information
def jetburn_info():
    """
    This function is the entry point for showing the current version information

    :return: (str) prints current version
    """

    operations.get_info()


# Create mission control
def mission_control(exec_mode=None, currency_code=None, number_of_results=None):
    """
    This function controls the program

    :param exec_mode: (str) Execution mode for the program
    :param currency_code: (str) Currency of ticket price
    :param number_of_results: (int) Number of results to show per search
    :return: (list) List of responses from python requests
    """

    # Print initial message
    operations.initial_message()
    msg.info("Initializing program.....")
    msg.info("Preparing airbase.....")

    # Check currency
    valid_currency = operations.is_valid_currency(currency=currency_code)
    if valid_currency:
        currency = currency_code
    else:
        currency = 'EUR'

    # Get the trip status - one way or round trip
    trip_status = operations.trip_status()

    # Get questions according to trip status
    trip_info = operations.get_trip_info(round_trip=trip_status)

    # Construct URL
    msg.info("Getting ready for take off.....")
    api_endpoint = "https://api.skypicker.com"
    flights = "/flights"
    payload = {
        'flyFrom': trip_info['origin'].upper(),
        'to': trip_info['destination'].upper(),
        'dateFrom': trip_info['fly_out_date'],
        'dateTo': trip_info['fly_out_date'],
        'returnFrom': trip_info['fly_back_date'],
        'returnTo': trip_info['fly_back_date'],
        'adults': trip_info['adults'],
        'teens': trip_info['teens'],
        'children': trip_info['children'],
        'infants': trip_info['infants'],
        'curr': currency,
        'limit': number_of_results,
        'partner': 'picky'
    }

    # Construct api endpoint with flights
    url = api_endpoint + flights

    # Send request to web page
    msg.info("Requesting to takeoff.....")
    response = requests.get(url, params=payload)

    # Check the received response
    if response.status_code == 200:
        msg.info("Cleared for takeoff.....")
        try:
            json_data = response.json()
        except ValueError as err:
            err_msg = "Flight aborted due to JSON failure! ERROR: {}".format(err)
            msg.fail(err_msg)
            sys.exit(-1)
    else:
        msg.fail("Flights are suspended. Contact ATC!")
        sys.exit(-1)

    # Parse the response
    for data in json_data['data']:
        flight_parser.itinerary_parser(flight_search_data=data, execution_mode=exec_mode)


# CLI entry point of jetburn
def jetburn_cli():
    """This function is the boiler plate to run this program

    Parses argument and follow through to mission control
    """

    # Create parser
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-m', '--mode', action='store', dest='mode', required=False,
                        help='Execution mode of the program. Compact[c/compact](default), Advanced[a/advanced] and '
                             'Expert [e/expert]. Usage: jetburn -m e OR jetburn -m expert')
    parser.add_argument('-c', '--currency', action='store', dest='currency_code', required=False,
                        help='Three letter currency code.[EUR], USD, AUD, CAD, RON, PLN etc.'
                             ' Usage: jetburn -c USD')
    parser.add_argument('-r', '--result', action='store', dest='results', required=False,
                        help='Number of results to show per search. Default is [5]'
                             ' Usage: jetburn -r 10')
    parser.add_argument('--currency-info', action='store', dest='currency_info', required=False,
                        help='Displays if the currency is valid or not for this program. (To be used with -c flag)'
                             ' Usage: jetburn --currency-info <ISO_4217_currency_code>')
    parser.add_argument('--airport-info', action='store', dest='airport_info', required=False,
                        help='Displays information about airport.'
                             ' Usage: jetburn --airport-info <iata_airport_code>')
    parser.add_argument('--airline-info', action='store', dest='airline_info', required=False,
                        help='Displays airline information.'
                             ' Usage: jetburn --airline-info <iata_airline_code>')
    parser.add_argument('--find-airport', action='store', dest='city_name', required=False,
                        help='Finds airport names and IATA code by city name.'
                             ' Usage: jetburn --find-airport <city_name>')
    parser.add_argument('--find-currency', action='store', dest='country_name', required=False,
                        help='Finds ISO 4217 currency names and codes by country name.'
                             ' Usage: jetburn --find-currency <country_name>')
    parser.add_argument('-v', '--version', action='store', dest='version', required=False,
                        help='Shows the current version of jetburn'
                             ' Usage: jetburn -v / --version')
    # Parse arguments
    args = parser.parse_args()

    # Double check passed arguments
    if args.mode is None:
        exec_mode = 'compact'
    else:
        exec_mode = args.mode.lower()

    # Check currency code
    if args.currency_code is None:
        _currency_code = 'EUR'
    else:
        _currency_code = args.currency_code.upper()

    # Check result display parameter
    if args.results is None:
        _results = 5
    else:
        _results = int(args.results)

    # Check if the currency information argument
    if args.currency_info is None:
        pass  # noqa
    elif args.currency_info == 'all':
        operations.initial_message()
        operations.get_currency_names()
    else:
        err_msg = "Invalid input: {}".format(args.currency_info)
        msg.fail(err_msg)
        sys.exit(-1)

    # Check if the search patter is given or not
    if args.city_name is None:
        pass  # noqa
    else:
        operations.initial_message()
        pattern = args.city_name
        operations.get_airport_names_by_city(search_city=pattern)

    # Passover the control to mission control if no info check arguments are provided
    if args.currency_info is None and args.city_name is None:
        # Pass the control to mission control
        mission_control(exec_mode=exec_mode, currency_code=_currency_code, number_of_results=_results)
