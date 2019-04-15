UART Echo
=========

This example demonstrates the usage of the UART API by giving an example of
how to read data from the secondary serial port of the XBee module and write
it back.

The example sends out to the serial port an echo of the received data.

Requirements
------------

To run this example you need:

* One XBee3 radio module with MicroPython and secondary UART support. At the
  moment only XBee Cellular modules support secondary UART feature.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
* A serial terminal application installed in your computer.

Setup
-----

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.
2. Connect the secondary UART interface of the XBee device to one serial port
   of your computer. See the following table for more information about the
   secondary UART pins layout on the XBee modules:

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

3. This demo requires a serial console terminal in order to see the echo from
   the XBee module. Configure the terminal and open a serial connection with
   the XBee module.

   The baud rate of the serial console must be **9600**, as the sample will
   configure the UART of the XBee module with that baud rate.

Run
---

The example is already configured, so all you need to do is to compile and
launch the application.

While it is running, type some data in the serial console terminal you
configured previously. You should see the echo from the XBee module
corresponding to the data you have written.

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