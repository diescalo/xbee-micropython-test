FTP Client Sample Application
=============================

This example demonstrates the usage of the 'uftp' library by giving an example
of how to connect with an FTP server to download and upload files.

The example waits until the module is connected to the cellular network. After
that, it connects with a generic speed test FTP server, downloads the remote 
file '1KB.zip' and uploads the local file '2b.txt' in the 'upload' folder of
the FTP server. 

Requirements
------------

To run this example you need:

* One XBee3 Cellular module with MicroPython support and a micro SIM card
  inserted with Internet capabilities.
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

When the module has joined the cellular network, you should see the FTP
operations that take place with the FTP server:

    - Waiting for the module to be connected to the cellular network... [OK]
    - Connecting to FTP server... [OK]
    - Retrieving file '1KB.zip' (1024 bytes)... [OK]
       * Time taken: 6 seconds
    - Uploading file '2b.txt'... [OK]
       * Time taken: 5 seconds
    - Closing FTP connection... [OK]
    - Done


You can change the values of the FTP constants and file names to connect with
a different FTP server and transfer other files.

Required libraries
--------------------

* uftp

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