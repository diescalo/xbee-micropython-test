Digital Input Read Sample Application
=====================================

This example demonstrates the usage of the I/O pins API by giving an example
of how to check the present value on a pin set up to be in input mode.

The example uses the polling technique to monitor the value of the pin
associated to a button of the XBee carrier board.

Demo requirements
-----------------

To run this example you need:

* One XBee3 radio module with MicroPython support.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).

Demo setup
----------

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.
2. Configure the IO line corresponding to the button in the example. Depending
   on the carrier board you are using you may need to change the value of the
   ``INPUT_PIN_ID`` variable:

   * XBIB-U-DEV board:

     * The example is already configured to use this carrier board. The input
       pin configured is ``D3`` (AD3/DIO3), which corresponds to the SW5 user
       button of the board. No further changes are necessary.

   * XBIB-C board:

     * If you are using the XBIB-C, update the ``INPUT_PIN_ID`` variable to
       ``D0`` (AD0/DIO0), which corresponds to the Comm DIO0 user button of the
       board.

   **NOTE**: It is recommended to verify the capabilities of the pins used in
   the example as well as the electrical characteristics in the product manual
   of your XBee Device to ensure that everything is configured correctly.

Demo run
--------

The example is already configured, so all you need to do is build and launch
the project. To test the functionality, follow these steps:

1. Press the button corresponding to the digital input line.
2. Verify the value displayed in the XBee REPL console changes from 1 to 0 when
   the button is pressed::

       - Digital input value: 1
       - Digital input value: 1
       - Digital input value: 0
       - Digital input value: 1

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