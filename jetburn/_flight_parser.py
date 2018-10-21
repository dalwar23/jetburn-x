#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Import python libraries
import requests
from pyrainbowterm import print
import json
from datetime import datetime
from tabulate import tabulate

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


# Get airline information from the Internet
def __get_airline_info():
    """
    This function gets airline info from the Internet

    :return: (json)(list) List of dictionary objects
    """
    url = 'https://api.skypicker.com/airlines'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            airlines = response.json()
        else:
            response.raise_for_status()
    except requests.ConnectionError as err:
        print('Airline information service is offline!', log_type='error', color='red')

    # Return
    return airlines


# Calculate total flight time in a flight leg
def __calculate_layover_time(arrival_time=None, departure_time=None):
    """
    This function calculates layover time between flights

    :return: (str) Layover time in hour and minutes
    """
    # Removing mili seconds
    dtime = departure_time
    atime = arrival_time

    flight_time_sec = dtime - atime
    minutes, seconds = divmod(flight_time_sec, 60)
    hours, minutes = divmod(minutes, 60)
    total_flight_time = str(hours) + "h" + " " + str(minutes) + "m"

    # return
    return total_flight_time


# Calculate total flight time in a flight leg
def __calculate_flight_time(departure_time=None, arrival_time=None):
    """
    This function calculates total flight time for a single leg

    :return: (str) Flight time in hour and minutes
    """
    # Removing milli-seconds
    dtime = departure_time
    atime = arrival_time

    flight_time_sec = atime - dtime
    minutes, seconds = divmod(flight_time_sec, 60)
    hours, minutes = divmod(minutes, 60)
    total_flight_time = str(hours) + "h" + " " + str(minutes) + "m"

    # return
    return total_flight_time


# Flight search parser function
def __itinerary_parser(flight_search_data=None, execution_mode=None):
    """
    This function parses flight search data

    :param flight_search_data: (list) List of dictionaries with flight information
    :return: <>
    """
    # Assign data for the search
    data = flight_search_data

    # Get the airline information data
    airlines = __get_airline_info()

    fly_duration = data['fly_duration']
    airport_change = data['has_airport_change']
    departure_time = datetime.utcfromtimestamp(data['dTime']).strftime('%a %d %b %H:%M')
    arrival_time = datetime.utcfromtimestamp(data['aTime']).strftime('%a %d %b %H:%M')
    price = ''
    for currency, amount in data['conversion'].items():
        tag = str(amount) + " " + currency
        price += tag
        price += " / "
    route = []
    ret_route = []
    for index, item in enumerate(data['route']):
        flight_leg = {}
        flight_leg['leg_no'] = index + 1
        flight_leg['origin_city'] = "{}".format(item['cityFrom'])
        flight_leg['origin_airport'] = "{}".format(item['flyFrom'])
        flight_leg['destination_city'] = "{}".format(item['cityTo'])
        flight_leg['destination_airport'] = "{}".format(item['flyTo'])
        flight_leg['departure_time'] = datetime.utcfromtimestamp(item['dTime']).strftime('%a %d %b %H:%M')
        flight_leg['arrival_time'] = datetime.utcfromtimestamp(item['aTime']).strftime('%a %d %b %H:%M')
        if index == 0:
            flight_leg['layover'] = (str(0))
            pass
        else:
            layover_time = __calculate_layover_time(arrival_time=data['route'][index - 1]['aTime'],
                                                  departure_time=data['route'][index]['dTime'])
            flight_leg['layover'] = layover_time
        flight_time = __calculate_flight_time(departure_time=item['dTimeUTC'], arrival_time=item['aTimeUTC'])
        flight_leg['flight_duration'] = flight_time
        flight_leg['flight_number'] = item['airline'] + " " + str(item['flight_no'])
        airline = (entry['name'] for entry in airlines if entry['id'] == item['airline']).next()
        flight_leg['airline'] = airline
        if item['return'] == 0:
            route.append(flight_leg)
        elif item['return'] == 1:
            ret_route.append(flight_leg)

    # print("{}".format(json.dumps(route, indent=4)))

    for index, route_leg in enumerate(route):
        if index == 0:
            outbound_leg = route_leg['origin_airport'] + "---"
            outbound_leg += route_leg['destination_airport'] + "---"
        else:
            if route[index - 1]['destination_airport'] == route_leg['origin_airport']:
                outbound_leg += route_leg['destination_airport'] + "---"
            else:
                if airport_change:
                    outbound_leg += " [Change Airport] "
                pass

    outbound_itinerary = [departure_time, outbound_leg[:-3], fly_duration, arrival_time, price[:-3]]

    table_rows = [outbound_itinerary]
    print(tabulate(table_rows, tablefmt='grid'), color='green')
