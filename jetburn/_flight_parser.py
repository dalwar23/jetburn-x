#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import future print function and unicode literals for python2.7 support
from __future__ import print_function, unicode_literals

# Import builtin python libraries
from datetime import datetime

# Import external python libraries
from tabulate import tabulate
import requests
import wasabi
from wasabi import color

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar.hossain@protonmail.com"

# Create msg from wasabi printer class
msg = wasabi.Printer()


# Get airline information from the Internet
def _get_airline_info():
    """
    This function gets airline info from the Internet

    :return: (json)(list) List of dictionary objects
    """

    url = "https://api.skypicker.com/airlines"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            airlines = response.json()
        else:
            response.raise_for_status()
    except requests.ConnectionError as err:
        airlines = "undefined"
        err_msg = "Airline information service is offline! ERROR: {}".format(err)
        msg.fail(err_msg)

    # Return
    return airlines


# Calculate total flight time in a flight leg
def _calculate_layover_time(arrival_time=None, departure_time=None):
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
def _calculate_flight_time(departure_time=None, arrival_time=None):
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
def itinerary_parser(flight_search_data=None, execution_mode=None):
    """
    This function parses flight search data

    :param flight_search_data: (list) List of dictionaries with flight information
    :returns: (list) Shows a girded table
    """

    # Assign data for the search
    data = flight_search_data

    # Get the airline information data
    airlines = _get_airline_info()

    fly_duration = data["fly_duration"]
    airport_change = data["has_airport_change"]
    departure_time = datetime.utcfromtimestamp(data["dTime"]).strftime("%a %d %b %H:%M")
    arrival_time = datetime.utcfromtimestamp(data["aTime"]).strftime("%a %d %b %H:%M")
    price = ""
    for currency, amount in data["conversion"].items():
        tag = str(amount) + " " + currency
        price += tag
        price += " / "
    route = []
    ret_route = []
    for index, item in enumerate(data["route"]):
        flight_leg = dict()
        flight_leg["leg_no"] = index + 1
        flight_leg["origin_city"] = "{}".format(item["cityFrom"])
        flight_leg["origin_airport"] = "{}".format(item["flyFrom"])
        flight_leg["destination_city"] = "{}".format(item["cityTo"])
        flight_leg["destination_airport"] = "{}".format(item["flyTo"])
        flight_leg["departure_time"] = datetime.utcfromtimestamp(
            item["dTime"]
        ).strftime("%a %d %b %H:%M")
        flight_leg["arrival_time"] = datetime.utcfromtimestamp(item["aTime"]).strftime(
            "%a %d %b %H:%M"
        )
        if index == 0:
            flight_leg["layover"] = str(0)
        else:
            layover_time = _calculate_layover_time(
                arrival_time=data["route"][index - 1]["aTime"],
                departure_time=data["route"][index]["dTime"],
            )
            flight_leg["layover"] = layover_time
        flight_time = _calculate_flight_time(
            departure_time=item["dTimeUTC"], arrival_time=item["aTimeUTC"]
        )
        flight_leg["flight_duration"] = flight_time
        flight_leg["airline_code"] = item["airline"]
        flight_leg["flight_number"] = item["airline"] + " " + str(item["flight_no"])
        airline_full_name = [
            entry["name"] for entry in airlines if entry["id"] == item["airline"]
        ]
        flight_leg["airline_full_name"] = airline_full_name[0]
        if item["return"] == 0:
            route.append(flight_leg)
        elif item["return"] == 1:
            ret_route.append(flight_leg)

    for index, route_leg in enumerate(route):
        if index == 0:
            outbound_leg = route_leg["origin_airport"] + "---"
            carriers = route_leg["airline_code"] + "-"
            outbound_leg += route_leg["destination_airport"] + "---"
        else:
            if route[index - 1]["destination_airport"] == route_leg["origin_airport"]:
                carriers += route_leg["airline_code"] + "-"
                outbound_leg += route_leg["destination_airport"] + "---"
            else:
                if airport_change:
                    outbound_leg += " [Change Airport] "

    outbound_itinerary = [
        departure_time,
        outbound_leg[:-3],
        fly_duration,
        arrival_time,
        price[:-3],
        carriers[:-1],
    ]

    table_rows = [outbound_itinerary]
    formatted_table = color(tabulate(table_rows, tablefmt="grid"), fg="cyan")
    print(formatted_table)
