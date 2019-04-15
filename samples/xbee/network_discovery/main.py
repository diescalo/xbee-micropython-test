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


print(" +-------------------------------------------+")
print(" | XBee MicroPython Network Discovery Sample |")
print(" +-------------------------------------------+\n")

print("Discovering network devices...\n")

# Discover the network devices and print their basic information.
for device in xbee.discover():
    addr64 = device['sender_eui64']
    node_id = device['node_id']
    rssi = device['rssi']

    print("New discovered device:\n"
          "  - 64-bit address: %s\n"
          "  - Node identifier: %s\n"
          "  - RSSI: %d\n"
          % (''.join('{:02x}'.format(x).upper() for x in addr64), node_id, rssi))

print("Network discovery finished")
