I2C HDC1080 Sample Application
==============================

This example demonstrates the usage of the I2C API by giving an example of how
to read the temperature and humidity values from the HDC1080 I2C sensor.

Demo requirements
-----------------

To run this example you need:

* One XBee3 radio module with MicroPython support.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
* One standalone HDC1080 humidity and temperature sensor (not necessary if you
  are using an XBIB-C carrier board).

Demo setup
----------

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.
2. Connect the HDC1080 device to the I2C interface of the XBee module. The way
   to connect the sensor changes depending on the carrier board you have:

   * XBIB-U-DEV board:

     * Isolate the pins configured as SDA and SCL so they do not use the
       functionality provided by the board.
     * Connect the HDC1080 device to VCC, to the pins configured as SDA and SCL
       and to GND. See the following table for more information about the pins
       layout::

           +--------+------------+----------+-----------+-----------+
           | Signal | Pin ID     | Pin # TH | Pin # SMT | Pin # MMT |
           +--------+------------+----------+-----------+-----------+
           | SDA    | PWM1/DIO11 | 7        | 8         | 8         |
           +--------+------------+----------+-----------+-----------+
           | SCL    | AD1/DIO1   | 19       | 32        | 30        |
           +--------+------------+----------+-----------+-----------+

   * XBIB-C board:

     * XBIB-C boards already come with an HDC1080 I2C sensor connected to the
       I2C interface of the XBee module, so you don't need to connect anything.

   **NOTE**: It is recommended to verify the capabilities of the pins used in
   the example as well as the electrical characteristics in the product manual
   of your XBee Device to ensure that everything is configured correctly.

Demo run
--------

The example is already configured, so all you need to do is build and launch
the project.

The application reads and displays the value of temperature and humidity from
the HDC1080 every 5 seconds. Verify that the XBee REPL console display them::

    - Temperature: 24.5C
    - Humidity: 29.44%

    - Temperature: 24.55C
    - Humidity: 32.62%

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