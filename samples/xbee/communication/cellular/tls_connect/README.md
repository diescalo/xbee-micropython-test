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