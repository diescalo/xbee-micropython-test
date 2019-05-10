Connection Status Application
=============================

This example demonstrates how to monitor the **AI** AT command to detect
and report changes until the modem registered to the cellular network.

Requirements
------------

To run this example you need:

* One XBee3 Cellular module with MicroPython support and a micro SIM card
  inserted with SMS capabilities.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).

Setup
-----

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.

Run
---

The example is already configured, so all you need to do is to compile and
launch the application.

Once it is running, restart your module. The application will be executed
again and it will display all the AI changes taking place until the module
registers again to the cellular network: 

    - AI Changed!
       * New AI: 0xFF (MODEM_INITIALIZING)
    - AI Changed!
       * New AI: 0x22 (REGISTERING_TO_NETWORK)
    - AI Changed!
       * New AI: 0xFF (MODEM_INITIALIZING)
    - AI Changed!
       * New AI: 0x22 (REGISTERING_TO_NETWORK)
    - AI Changed!
       * New AI: 0x23 (CONNECTING_TO_INTERNET)
    - AI Changed!
       * New AI: 0x00 (CONNECTED)

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