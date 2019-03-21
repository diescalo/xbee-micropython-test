Digital Input Read
==================

This example demonstrates the usage of the I/O pins API by giving an example
of how to check the present value on a pin set up to be in input mode.

The example uses the polling technique to monitor the value of the pin.

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
2. Configure the IO lines in the example. Depending on the carrier board you
   are using you may need to change a couple of lines in the example code:

   * XBIB-U-DEV board:

     * The example is already configured to use this carrier board. The input
       line is configured to use the SW5 user button of the board. No further
       changes are necessary.

   * XBee Development Board:

     * If you are using the XBee Development Board, update the ``INPUT_PIN_ID``
       constant accordingly.

   **NOTE**: It is recommended to verify the capabilities of the pins used in
   the example in the product manual of your XBee Device to ensure that
   everything is configured correctly.

Demo run
--------

The example is already configured, so all you need to do is build and launch
the project. To test the functionality, follow these steps:

1. Press the button corresponding to the digital input line. In the XBIB boards
   it is the DIO3.
2. Verify the value displayed in the REPL console changes from 1 to 0 when
   the button is pressed.

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