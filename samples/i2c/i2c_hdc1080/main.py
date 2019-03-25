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

from machine import I2C
import sys
import time

# Constants
HDC1080_ADDR = 0x40

REG_TMP = 0x00
REG_HUM = 0x01


def main():
    print(" +-------------------------------------+")
    print(" | XBee MicroPython I2C HDC1080 Sample |")
    print(" +-------------------------------------+\n")

    # Instantiate an I2C peripheral.
    i2c = I2C(1)

    # Verify that the sensor is connected to the I2C interface.
    if HDC1080_ADDR not in i2c.scan():
        print("Could not find the sensor!")
        sys.exit(1)

    # Start reading temperature and humidity measures.
    while True:
        # Change the pointer to 0x00 (Temperature register)
        i2c.writeto(HDC1080_ADDR, bytearray([REG_TMP]))
        # Wait for the temperature measure to complete (per data sheet).
        time.sleep(0.0635)
        # Read the temperature value (2 bytes).
        temp_bytes = i2c.readfrom(HDC1080_ADDR, 2)
        # Calculate the temperature in Celsius.
        temp_celsius = (int.from_bytes(temp_bytes, "big") / 2 ** 16) * 165 - 40

        # Change the pointer to 0x01 (Temperature register)
        i2c.writeto(HDC1080_ADDR, bytearray([REG_HUM]))
        # Wait for the humidity measure to complete (per data sheet).
        time.sleep(0.065)
        # Read the humidity value (2 bytes).
        humidity_bytes = i2c.readfrom(HDC1080_ADDR, 2)
        # Calculate the humidity in HR.
        humidity_hr = (int.from_bytes(humidity_bytes, "big") / 2 ** 16) * 100

        # Print results:
        print("- Temperature: %sC" % round(temp_celsius, 2))
        print("- Humidity: %s%%" % round(humidity_hr, 2))
        print("")

        time.sleep(5)


if __name__ == '__main__':
    main()
