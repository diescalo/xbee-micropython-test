Network Discovery Sample Application
====================================

This example demonstrates the usage of the network discovery functionality by
giving an example of how to discover the devices that compose the network.

The example prints out in the console the 64-bit address, node identifier and
RSSI of the network devices as soon as they are found during the discovery.

Requirements
------------

To run this example you need:

* At least two XBee3 radio modules with MicroPython support.
* At least two carrier boards for the radio modules (XBIB-U-DEV or XBIB-C board).
* The XCTU application (available at www.digi.com/xctu).

Setup
-----

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio modules into the XBee adapters and connect them to your
   computer's USB ports.
2. Ensure that the modules are on the same network.

Run
---

The example is already configured, so all you need to do is to compile and
launch the application.

Verify that the application prints out the 64-bit address, node identifier and
RSSI of the network devices in the console as soon as they are discovered:

    New discovered device:
      - 64-bit address: 0013A200XXXXXXXX
      - Node identifier: MY_REMOTE_DEVICE
      - RSSI: -33

Supported platforms
-------------------

* Digi XBee3 Zigbee 3 - minimum firmware version: 1006
* Digi XBee3 802.15.4 - minimum firmware version: 2003
* Digi XBee3 DigiMesh 2.4 - minimum firmware version: 3002

License
-------

Copyright (c) 2019, Digi International Inc. <support@digi.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.