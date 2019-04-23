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

# TODO: replace with the address of your I2C EEPROM.
EEPROM_ADDR = 0x54
# TODO: replace with the addressing size.
ADDR_SIZE = 16
# TODO: replace with the maximum read/write operation size.
MAX_SIZE = 128
# TODO: replace with the time to wait between operations.
WAIT_TIME = 0.005

ADDR_START = 0x00
DATA_TO_WRITE = "Hello World!"


print(" +------------------------------------+")
print(" | XBee MicroPython I2C EEPROM Sample |")
print(" +------------------------------------+\n")

# Instantiate an I2C peripheral.
i2c = I2C(1)

# Verify that the I2C EEPROM is connected to the I2C interface.
if EEPROM_ADDR not in i2c.scan():
    print("Could not find the EEPROM!")
    sys.exit(1)

print("Erasing flash...\n")

# Erase the memory by writing 0xFF bytes.
i2c.writeto_mem(EEPROM_ADDR, ADDR_START, bytearray([0xFF] * MAX_SIZE), addrsize=ADDR_SIZE)

# Wait some time between write and read operations (specified in the EEPROM datasheet).
time.sleep(WAIT_TIME)

# Read 128 bytes starting at 0x00.
print(i2c.readfrom_mem(EEPROM_ADDR, ADDR_START, MAX_SIZE, addrsize=ADDR_SIZE))

print("\nWriting '%s' to flash...\n" % DATA_TO_WRITE)

# Write the specified data starting at 0x00.
i2c.writeto_mem(EEPROM_ADDR, ADDR_START, DATA_TO_WRITE.encode(), addrsize=ADDR_SIZE)

# Wait some time between write and read operations (specified in the EEPROM datasheet).
time.sleep(WAIT_TIME)

# Read 128 bytes starting at 0x00.
print(i2c.readfrom_mem(EEPROM_ADDR, ADDR_START, MAX_SIZE, addrsize=ADDR_SIZE))
