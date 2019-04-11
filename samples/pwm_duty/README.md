PWM Duty Cycle Sample Application
=================================

This example demonstrates the usage of the PWM API by giving an example of
how to control the duty cycle of the PWM channel of the XBee device.

The example waits for a button press to start the duty cycle sequence. This
sequence increases gradually the value of the duty cycle to its maximum and
then decreases it gradually to its minimum.

Requirements
------------

To run this example you need:

* One XBee3 radio module with MicroPython support.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
* One PWM peripheral (RGB LED, buzzer, DC servo, etc.)

Setup
-----

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.
2. Connect the PWM device to the ``RSSI PWM/DIO10`` pin of the XBee module. The
   way to connect it changes depending on the carrier board you have:

   * XBIB-U-DEV board:

     * In XBIB-U-DEV boards the ``RSSI PWM/DIO10`` is already connected to the
       RSSI LEDs tower of the board. So, you don't need to connect anything in
       order to test the sample.

   * XBIB-C board:

     * Isolate the ``RSSI PWM/DIO10`` pin so it does not use the
       functionality provided by the board.
     * Connect the PWM device to the ``RSSI PWM/DIO10`` pin and to GND.

   **NOTE**: It is recommended to verify the capabilities of the pins used in
   the example as well as the electrical characteristics in the product manual
   of your XBee Device to ensure that everything is configured correctly.

Run
---

The example is already configured, so all you need to do is to compile and 
launch the application. Follow these steps to test the sample:

1. Press the start button (**SW2** in XBIB-U-DEV carrier board or **Comm DIO0
   in XBIB-C carrier board) to start the duty cycle sequence. This sequence
   increases gradually the value of the duty cycle to its maximum and then
   decreases it gradually to its minimum.
2. Verify that the output of the peripheral varies during the sequence. In the
   case of the RSSI LEDs tower of the XBIB-U-DEV board, LEDs should start
   turning on gradually from the bottom to the top and then turning off from
   the top to the bottom. 

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