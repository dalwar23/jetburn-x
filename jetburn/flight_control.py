#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Import python libraries
import sys
from pyrainbowterm import *
import requests
import json
import argparse

# Import local python library
import _operations as operations

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


# Create mission control
def mission_control(execution_mode=None, currency_code=None):
    """
    This function controls the program

    :param execution_mode: (str) Execution mode for the program
    :param currency_code: (str) Currency of ticket price
    :return: (list) List of responses from python requests
    """
    # Print initial message
    operations.__initial_message()
    print('Initializing program.....', log_type='info')
    print('Preparing airbase.....', log_type='info')

    # Check currency
    valid_currency = operations.__is_valid_currency(currency=currency_code)
    if valid_currency:
        currency = currency_code
    else:
        currency = 'EUR'

    # Get the trip status - one way or round trip
    trip_status = operations.__trip_status()

    # Get questions according to trip status
    trip_info = operations.__get_trip_info(round_trip=trip_status)

    # Construct URL
    print('Getting ready for take off.....', log_type='info')
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
        'partner': 'picky'
    }

    # Construct api endpoint with flights
    url = api_endpoint + flights

    # Send request to web page
    print('Requesting to takeoff.....', log_type='info')
    response = requests.get(url, params=payload)

    # Check the received response
    if response.status_code == 200:
        print('Cleared for takeoff', log_type='info')
        try:
            json_data = response.json()
            print(json.dumps(json_data['data'][0], indent=4))
        except ValueError as err:
            print('Flight aborted due to JSON failure! ERROR: {}'.format(err))
            sys.exit(1)
    else:
        print('Flight suspended. Contact ATC!', log_type='error', color='red')
        sys.exit(1)

    # Parse the response


# CLI entrypoint of jetburn
def jetburn_cli():
    """
    This function is the boiler plate to run this program and also parses argument and follow
    through to mission control
    """

    # Create parser
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-m', '--mode', action='store', dest='mode', required=False,
                        help='Execution mode of the program. Compact[c/compact](default) and Extended [e/extended]')
    parser.add_argument('-c', '--currency', action='store', dest='currency_code', required=False,
                        help='Three letter currency code.[EUR, USD, AUD, CAD, RON, PLN] etc.')
    parser.add_argument('-s', '--show', action='store', dest='display', required=False,
                        help='Displays information. Usage: jetburn --show currency')
    parser.add_argument('-f', '--find', action='store', dest='pattern', required=False,
                        help='Finds airport names and IATA code. Usage: jetburn --find <city_name>')
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

    # Check if the currency display is provided or not
    if args.display is None:
        pass
    elif args.display == 'currency':
        operations.__initial_message()
        operations.__get_currency_names()
    else:
        print('Invalid input: {}'.format(args.display), log_type='error', color='red')
        sys.exit(1)

    # Check if the search patter is given or not
    if args.pattern is None:
        pass
    else:
        operations.__initial_message()
        pattern = args.pattern
        operations.__get_airport_names(search_pattern=pattern)

    # Passover the control to mission control if no info check arguments are provided
    if args.display is None and args.pattern is None:
        # Pass the control to mission control
        mission_control(execution_mode=exec_mode, currency_code=_currency_code)
