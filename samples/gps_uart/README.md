GPS UART Sample Application
===========================

This example demonstrates the usage of the UART API by giving an example
of how to read data from a GPS connected through the UART interface to
display the current position.

The example reads GPS data from the secondary UART of the module every 30
seconds, extracts the values of latitude and longitude from the read data
and displays them. 

Requirements
------------

To run this example you need:

* One XBee3 Cellular module with MicroPython support.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
* A GPS board.

Setup
-----

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.
2. Connect the secondary UART interface of the XBee device to the serial
   interface of the GPS board. See the following table for more information
   about the secondary UART pins layout on the XBee modules:

           +--------+------------+----------+-----------+-----------+
           | Signal | Pin ID     | Pin # TH | Pin # SMT | Pin # MMT |
           +--------+------------+----------+-----------+-----------+
           | TX     | DIO4       | 11       | 24        | 23        |
           +--------+------------+----------+-----------+-----------+
           | RX     | DIO12      | 4        | 5         | 5         |
           +--------+------------+----------+-----------+-----------+
           | RTS    | AD2/DIO2   | 18       | 31        | 29        |
           +--------+------------+----------+-----------+-----------+
           | CTS    | AD3/DIO3   | 17       | 30        | 28        |
           +--------+------------+----------+-----------+-----------+

Run
---

The example is already configured, so all you need to do is to compile and
launch the application.

The application displays the values of latitude and longitude every 10 seconds:

    - Reading GPS data... [OK]
    - Latitude:
    - Longitude:
    --------------------------------
    - Reading GPS data... [OK]
    - Latitude:
    - Longitude:
    --------------------------------
    - Reading GPS data... [OK]
    - Latitude:
    - Longitude:
    --------------------------------

Supported platforms
-------------------

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