ADC polling Sample Application
==============================

This example demonstrates the usage of the I/O pins API by giving an example
of how to initialize an I/O pin to read analog values.

The example configures an IO line of the XBee device as ADC. Then, it
periodically reads its value and prints it.

Requirements
------------

To run this example you need:

* One XBee3 radio module with MicroPython support.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
* One voltage variable peripheral (for example a potentiometer).

Setup
-----

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.
2. Connect a voltage variable source to the pin configured as ADC (light
   sensor, temperature sensor, etc). For testing purposes we recommend using a
   potentiometer. Follow these steps to connect it:

     * Isolate the pin configured as ADC so it does not use the functionality
       provided by the board.
     * Connect the potentiometer to VCC, to the pin configured as ADC and to
       GND. Something similar to this::

            O   VCC
            |
            <
            >___ XBee device pin (ADC)
            >
            <
            |
           ---
            -   GND

     * If you prefer not to isolate the pin of the board and not to use a
       potentiometer, you can still test the example using one of the user
       buttons from the carrier board. In this case the analog value will
       change from all to nothing depending on the status of the button. This
       step depends on the carrier board you are using:

       * XBIB-U-DEV board:

         * The example is already configured to use this carrier board. The
           ADC pin configured is ``D3`` (AD3/DIO3), which corresponds to the
           SW5 user button of the board. No further changes are necessary.

       * XBIB-C board:

         * If you are using the XBIB-C, update the ``ADC_PIN_ID`` variable to
           ``D0`` (AD0/DIO0), which corresponds to the Comm DIO0 user button of
           the board.

   **NOTE**: It is recommended to verify the capabilities of the pins used in
   the example as well as the electrical characteristics in the product manual
   of your XBee Device to ensure that everything is configured correctly.

Run
---

The example is already configured, so all you need to do is build and launch
the project.

To test the functionality, follow these steps:

1. Rotate the potentiometer or press and release the corresponding user button
   in case you are not using a potentiometer.
2. Verify that the value displayed in the XBee REPL console is changing::

       - ADC value: 4095
       - ADC value: 4095
       - ADC value: 2

Supported platforms
-------------------

* Digi XBee3 Zigbee 3 - minimum firmware version: 1006
* Digi XBee3 802.15.4 - minimum firmware version: 2003
* Digi XBee3 DigiMesh 2.4 - minimum firmware version: 3002
* Digi XBee3 Cellular LTE-M/NB-IoT - minimum firmware version: 11410
* Digi XBee3 Cellular LTE CAT 1 - minimum firmware version: 31010

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