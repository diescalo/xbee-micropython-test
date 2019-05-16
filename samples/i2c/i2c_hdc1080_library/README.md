I2C HDC1080 Library Sample Application
======================================

This example demonstrates the usage of the I2C API and 'hdc1080' library by
giving an example of how to communicate with the HDC1080 temperature and
humidity sensor.

The example reads the temperature and humidity values from the sensor and
prints them every 5 seconds.  

Requirements
------------

To run this example you need:

* One XBee3 radio module with MicroPython support.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
* One standalone HDC1080 humidity and temperature sensor (not necessary if you
  are using an XBIB-C carrier board).

Setup
-----

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
       layout:

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

Run
---

The example is already configured, so all you need to do is to compile and
launch the application.

The application reads and displays the value of temperature and humidity from
the HDC1080 every 5 seconds. Verify that the XBee REPL console display them:

    - Temperature: 24.5 C
    - Humidity: 29.44 %

    - Temperature: 24.55 C
    - Humidity: 32.62 %

Required libraries
--------------------

* hdc1080

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