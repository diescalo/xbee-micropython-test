TLS Connect Sample Application
==============================

This example demonstrates the usage of the TLS (Transport Layer Security) API
by giving an example of how to connect to a server that authenticates that the
client connecting to is authorized to connect.

The example demonstrates use of `ussl.wrap_socket()` with ca_certs (to only
connect to servers with certificates signed by a single CA) and certfile/keyfile
as the client certificate to authenticate with the server.

Demo requirements
-----------------

To run this example you need:

* One XBee3 cellular radio module with a Micro SIM card inserted.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).

Demo setup
----------

Make sure the hardware is set up correctly:

1. Plug the XBee3 cellular module into the XBee adapter and connect it to your
   computer's USB port.
2. Make sure the XBee3 cellular device is connected to Internet. To do so,
   verify that the Connection status LED is blinking or the value of the
   **AI** parameter is **0**.

Demo run
--------

The example is already configured, so all you need to do is to compile and 
launch the application. When executed, the application tries to connect with
the **auth.pizza**. If the connection succeeds, it prints the JSON answer:

    

Supported platforms
-------------------

* Digi XBee3 Cellular LTE-M/NB-IoT - minimum firmware version: 11410
* Digi XBee3 Cellular LTE CAT 1 - minimum firmware version: 31010

License
-------

Copyright (c) 2019, Digi International, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.