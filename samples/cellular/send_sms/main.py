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

import network
import time

# TODO: replace with the target mobile number.
NUMBER = "+18779123444"
MESSAGE = "MicroPython on XBee Cellular is the best!"


print(" +----------------------------------+")
print(" | XBee MicroPython Send SMS Sample |")
print(" +----------------------------------+\n")

cellular = network.Cellular()

print("Waiting for the module to be connected to the cellular network...")

# Before sending the SMS, wait until the module is connected to the cellular network.
while not cellular.isconnected():
    time.sleep(1)

print("Sending SMS to %s >> %s" % (NUMBER, MESSAGE))

try:
    cellular.sms_send(NUMBER, MESSAGE)
    print("Message sent successfully")
except Exception as e:
    print("Send failure: %s" % str(e))
