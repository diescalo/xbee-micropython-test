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

from hdc1080 import HDC1080
from machine import I2C
import time

print(" +---------------------------------------------+")
print(" | XBee MicroPython I2C HDC1080 library Sample |")
print(" +---------------------------------------------+\n")

# Instantiate the HDC1080 peripheral.
sensor = HDC1080(I2C(1))

# Start reading temperature and humidity measures.
while True:
    temp_celsius = sensor.read_temperature(True)
    humidity_hr = sensor.read_humidity()

    # Print results:
    print("- Temperature: %s C" % round(temp_celsius, 2))
    print("- Humidity: %s %%" % round(humidity_hr, 2))
    print("")

    time.sleep(5)
