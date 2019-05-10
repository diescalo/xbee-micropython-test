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


print(" +-------------------------------------+")
print(" | XBee MicroPython Receive SMS Sample |")
print(" +-------------------------------------+\n")

cellular = network.Cellular()

print("Waiting for SMS...\n")

while True:
    # Check if the XBee has received any SMS.
    sms = cellular.sms_receive()
    if sms:
        print("SMS received from %s >> %s" % (sms['sender'], sms['message']))

    # Wait 100 ms before checking for data again.
    time.sleep(0.1)
