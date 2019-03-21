Blinking LED Sample Application
===============================

This example demonstrates the usage of the I/O pins API by giving an example
of how to initialize and manage the status of an I/O pin.

The example toggles the status of an LED every second.

Demo requirements
-----------------

To run this example you need:

* One XBee3 radio module with MicroPython support.
* One carrier board for the radio module (XBIB or XBee Grove Development Board)

Demo setup
----------

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.

Demo run
--------

The example is already configured, so all you need to do is build and launch
the project.

Verify the LED corresponding to the configured pin in the carrier board starts
blinking (toggles its status every second). Every time the LED toggles, the
application indicates it through the REPL console:

 - Turn on LED
 - Turn off LED

Compatible with
---------------

* Digi XBee3 Zigbee 3
* Digi XBee3 802.15.4
* Digi XBee3 DigiMesh 2.4
* Digi XBee3 Cellular LTE-M/NB-IoT
* Digi XBee3 Cellular LTE CAT 1

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