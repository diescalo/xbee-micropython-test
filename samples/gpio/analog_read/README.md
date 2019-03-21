Analog Read Sample Application
==============================

This example demonstrates the usage of the I/O pins API by giving an example
of how to initialize an I/O pin to read analog values.

The example configures an IO line of the XBee device as ADC. Then, it
periodically reads its value and prints it.

Demo requirements
-----------------

To run this example you need:

* One XBee3 radio module with MicroPython support.
* One carrier board for the radio module (XBIB or XBee Grove Development Board)
* One potentiometer

Demo setup
----------

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.
2. Connect a voltage variable source to the pin configured as ADC (light
   sensor, temperature sensor, etc). For testing purposes we recommend using a
   potentiometer. Depending on the carrier board you are using you will need to
   follow a different set of instructions to connect it:

     * XBIB-U-DEV board:

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
         potentiometer, you can still test the example. The IO line configured
         as ADC (DIO1/AD1) is connected to the SW3 user button of the
         XBIB-U-DEV board, so the analog value will change from nothing to all
         depending on the status of the button.

     * XBee Development Board:

       * Connect a voltage to VRef pin of the device (you can take it from the
         Vcc pin).
       * Configure the micro-switch of AD1 line to "Potentiometer", this way
         the DIO1/AD1 line of the device will be connected to the board's
         potentiometer

  **NOTE**: It is recommended to verify the capabilities of the pins used in
  the example as well as the electrical characteristics in the product manual
  of your XBee Device to ensure that everything is configured correctly.

Demo run
--------

The example is already configured, so all you need to do is build and launch
the project.

To test the functionality, follow these steps:

1. Rotate the potentiometer.
2. Verify that the value displayed in the REPL console is changing.

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