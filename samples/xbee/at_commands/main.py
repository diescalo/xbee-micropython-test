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

import xbee


print(" +-------------------------------------+")
print(" | XBee MicroPython AT Commands Sample |")
print(" +-------------------------------------+\n")

# Read the module's firmware version.
fw_version = hex(xbee.atcmd("VR"))
print("Firmware version: " + fw_version)

# Read the module's hardware version.
hw_version = hex(xbee.atcmd("HV"))
print("Hardware version: " + hw_version)

# Read the module's temperature.
temperature = xbee.atcmd("TP")
print("The XBee is %.1F °C (%.1F °F)" % (temperature, temperature * 9.0 / 5.0 + 32.0))

# Configure the module's node identifier and read it.
xbee.atcmd("NI", "XBee3 module")
print("Configured node identifier: " + xbee.atcmd("NI"))
