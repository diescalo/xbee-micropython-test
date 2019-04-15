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

import sys
import xbee


# TODO: replace with the node identifier of your target device.
TARGET_NODE_ID = "RECEIVER"
MESSAGE = "Hello XBee!"


def find_device(node_id):
    """
    Finds the XBee device with the given node identifier in the network and
    returns it.

    :param node_id: Node identifier of the XBee device to find.

    :return: The XBee device with the given node identifier or ``None`` if it
        could not be found.
    """
    for dev in xbee.discover():
        if dev['node_id'] == node_id:
            return dev
    return None


print(" +--------------------------------------------+")
print(" | XBee MicroPython Transmit Data (NI) Sample |")
print(" +--------------------------------------------+\n")

# Find the device with the configure node identifier.
device = find_device(TARGET_NODE_ID)
if not device:
    print("Could not find the device with node identifier '%s'" % TARGET_NODE_ID)
    sys.exit(-1)

addr16 = device['sender_nwk']
addr64 = device['sender_eui64']

print("Sending data to %s >> %s" % (TARGET_NODE_ID, MESSAGE))

try:
    # Some protocols do not have 16-bit address. In those cases, use the 64-bit one.
    xbee.transmit(addr16 if addr16 else addr64, MESSAGE)
    print("Data sent successfully")
except Exception as e:
    print("Transmit failure: %s" % str(e))
