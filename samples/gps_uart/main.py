# Copyright 2019, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import time
from machine import UART

# Constants
GNGGA_MARK = "$GNGGA"
GNGSA_MARK = "$GNGSA"


def extract_gps(serial_data):
    """
    Extracts the GPS data from the provided text.

    :param serial_data: Text to extract the GPS data from.

    :return: GPS data or and empty string if data could not be found.
    """

    if GNGGA_MARK in serial_data and GNGSA_MARK in serial_data:
        # Find repeating GPS sentence mark "$GNGGA", ignore it
        # and everything before it.
        _, after_gngga = serial_data.split(GNGGA_MARK, 1)
        # Now find mark "$GNGSA" in the result and ignore it
        # and everything after it.
        reading, _ = after_gngga.split(GNGSA_MARK, 1)

        return reading
    else:
        return ""


def extract_latitude(input_string):
    """
    Extracts the latitude from the provided text, value is all in degrees and
    negative if South of Equator.

    :param input_string: Text to extract the latitude from.

    :return: Latitude
    """

    if "N" in input_string:
        find_me = "N"
    elif "S" in input_string:
        find_me = "S"
    else:
        # 9999 is a non-sensical value for Lat or Lon, allowing the user to
        # know that the GPS unit was unable to take an accurate reading.
        return 9999

    index = input_string.index(find_me)
    deg_start = index - 11
    deg_end = index - 9
    deg = input_string[deg_start:deg_end]
    min_start = index - 9
    min_end = index - 1
    deg_decimal = input_string[min_start:min_end]
    latitude = (float(deg)) + ((float(deg_decimal)) / 60)

    if find_me == "S":
        latitude *= -1

    return latitude


def extract_longitude(input_string):
    """
    Extracts the longitude from the provided text, value is all in degrees and
    negative if West of London.

    :param input_string: Text to extract the longitude from.

    :return: Longitude
    """

    if "E" in input_string:
        find_me = "E"
    elif "W" in input_string:
        find_me = "W"
    else:
        # 9999 is a non-sensical value for Lat or Lon, allowing the user to
        # know that the GPS unit was unable to take an accurate reading.
        return 9999

    index = input_string.index(find_me)
    deg_start = index - 12
    deg_end = index - 9
    deg = input_string[deg_start:deg_end]
    min_start = index - 9
    min_end = index - 1
    deg_decimal = input_string[min_start:min_end]
    longitude = (float(deg)) + ((float(deg_decimal)) / 60)

    if find_me == "W":
        longitude *= -1

    return longitude


def read_gps_sample():
    """
    Attempts to read GPS and print the latest GPS values.
    """

    try:
        # Attempt to read GPS data up to 3 times.
        for i in range(3):
            print("- Reading GPS data... ",  end="")
            # Configure the UART to the GPS required parameters.
            u.init(9600, bits=8, parity=None, stop=1)
            time.sleep(1)
            # Ensures that there will only be a print if the UART
            # receives information from the GPS module.
            while not u.any():
                if u.any():
                    break
            # Read data from the GPS.
            gps_data = str(u.read(), 'utf8')
            # Close the UART.
            u.deinit()
            # Get latitude and longitude from the read GPS data.
            lat = extract_latitude(extract_gps(gps_data))
            lon = extract_longitude(extract_gps(gps_data))
            # Print location.
            if lon != 9999 and lat != 9999:
                print("[OK]")
                print("- Latitude: %s" % lat)
                print("- Longitude: %s" % lon)
                print(32 * "-")
                break
            else:
                print("[ERROR]")
                print("   * Bad GPS signal. Retrying...")

    except Exception as E:
        print("[ERROR]")
        print("   * There was a problem getting GPS data: %s", str(E))


print(" +----------------------------------+")
print(" | XBee MicroPython GPS UART Sample |")
print(" +----------------------------------+\n")

# Create a UART instance (this will talk to the GPS module).
u = UART(1, 9600)

# Start reading GPS samples every 30 seconds.
while True:
    read_gps_sample()
    time.sleep(30)
