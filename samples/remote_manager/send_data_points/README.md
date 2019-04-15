Send Data Points Sample Application
===================================

This example demonstrates the usage of the Digi Remote Manager API by giving
an example of how to upload data points to your Digi Remote Manager account.

The example reads the temperature of the module every 5 seconds, creates a
`DataPoints` object and uploads it to your Digi Remote Manager account.

Requirements
------------

To run this example you need:

* One XBee3 cellular module with MicroPython support.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
* A Digi Remote Manager account with the XBee3 cellular device registered in.
* The XCTU application (available at www.digi.com/xctu).

Setup
-----

Make sure the hardware is set up correctly:

1. Plug the XBee3 cellular module into the XBee adapter and connect it to your
   computer's USB port.
2. Make sure the XBee3 cellular device is connected to Internet. To do so,
   verify that the Connection status LED is blinking or the value of the
   **AI** parameter is **0**.
3. Make sure the XBee3 cellular device is connected to Digi Remote Manager. To
   do so, verify that the value of the **RI** parameter is **0**.

Run
---

The example is already configured, so all you need to do is to compile and 
launch the application. When executed, it starts reading and uploading the
temperature of the XBee module to your Digi Remote Manager account every 5
seconds.

Follow these steps to verify the temperature is being uploaded to your Digi
Remote Manager account:

1. Log in your Digi Remote Manager account using your credentials: 
   https://remotemanager.digi.com/login.do
2. Within the Digi Remote Manager platfotm, go to the **Data Services** tab
   and select the **Data Streams** option.
3. Look for the stream **<device_id>/mp_xbee_temperature** where `<device_id>`
   is the ID of your XBee3 cellular device within your account.
4. Select the stream and verify the chart displays the temperature of the
   module as it is being sent.

Supported platforms
-------------------

* Digi XBee3 Cellular LTE-M/NB-IoT - minimum firmware version: 11411
* Digi XBee3 Cellular LTE CAT 1 - minimum firmware version: 31011

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