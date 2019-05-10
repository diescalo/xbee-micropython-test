AWS HTTPS Sample Application
============================

This example tests that AWS certificates loaded in the XBee module allows you
to create an SSL connection with AWS to send HTTP requests.

The example connects with AWS using the SSL certificates and requests the
shadow information of a thing sending an HTTP request, then prints it.

Requirements
------------

To run this example you need:

* One XBee3 Cellular module with MicroPython support and a micro SIM card
  inserted with Internet capabilities.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
* An AWS account with your XBee Cellular device added as a Thing. For more
  information on how to get started with AWS see
  [Connecting an XBee Cellular device to AWS IoT](../) guide.

Setup
-----

Make sure the hardware is set up correctly and the code is configured and
ready:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.
2. Ensure that the AWS SSL certificate files are in the `/flash/cert` directory
   on the XBee filesystem.
   * `SSL_PARAMS` constant within the code shows which SSL parameters are
     required, and gives examples for referencing the files.
   * If needed, replace the file paths to match the certificates you're
     using.
3. The policy attached to the SSL certificates must allow for connecting,
   and getting a **Thing's Shadow**
4. Configure the value of constants `HOST`, `REGION`, and `THING_NAME` needed
   to create a valid AWS endpoint to connect to.

Run
---

The example is already configured, so all you need to do is to compile and
launch the application.

When the module has joined the cellular network, you should see the output of
the AWS operations executed by the module such as the connection, as well as the shadow  :

    - Waiting for the module to be connected to the cellular network... [OK] 
    - Connecting to AWS... [OK]
    - Sending shadow request for thing '<YOUR_THING_NAME>'... [OK]
    - Waiting for data... [OK]
    - Received shadow for thing '<YOUR_THING_NAME>':
    ----------------------------------------------------------------
    HTTP/1.1 200 OK
    content-type: application/json
    content-length: 61
    date: Thu, 09 May 2019 08:08:51 GMT
    x-amzn-RequestId: 53ff83f2-0577-85f1-0235-4885cfcd86fe
    connection: keep-alive
    
    {"state":{},"metadata":{},"version":1,"timestamp":1557389331}
    ----------------------------------------------------------------
    - Done

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