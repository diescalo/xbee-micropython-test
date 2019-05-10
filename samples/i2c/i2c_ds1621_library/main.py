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

from ds1621 import Ds1621
from machine import I2C
import utime

# Constants
DS1621_ADDR = 0x48  # Assumes A0-2 are low.

print(" +--------------------------------------------+")
print(" | XBee MicroPython I2C DS1621 Library Sample |")
print(" +--------------------------------------------+\n")

# Instantiate an I2C peripheral.
i2c = I2C(1)

# Instantiate a DS1621 device.
ds = Ds1621(i2c, DS1621_ADDR)

# Read the temperature value.
temp_c = ds.read_temperature()
print("- Temperature: %.1f C (%.1f F)" % (temp_c, temp_c * 9 / 10 + 32))

# Configure the high temperature value register.
print("- Setting high temperature register to '22'... ", end="")
ds.set_high_temp_register(22)
print("[OK]")
# Verify the written value.
print("- Verifying the written value... ", end="")
r = ds.read_high_temp_register()
if r != 22:
    print("[ERROR]")
    print("   Set TH to '22' but read back '%d'" % r)
else:
    print("[OK]")

# Wait 10ms between writes (per data sheet).
utime.sleep_ms(10)

# Configure the low temperature value register.
print("- Setting low temperature register to '17'... ", end="")
ds.set_low_temp_register(17)
print("[OK]")
# Verify the written value.
print("- Verifying the written value... ", end="")
r = ds.read_low_temp_register()
if r != 17:
    print("[ERROR]")
    print("   Set TL to '17' but read back '%d'" % r)
else:
    print("[OK]")

print("- Done")
