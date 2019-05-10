AWS Publish Sample Application
==============================

This example uses the 'mqtt' library to connect with AWS using the SSL
certificates and publish data to a specific MQTT topic.

You can monitor the messages sent to the topic by subscribing to it in the AWS
IoT console.

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
3. The policy attached to the SSL certificates must allow for publishing,
   subscribing, connecting, and receiving data.
4. Configure the value of constants `HOST`, `REGION` needed to create a valid
   AWS endpoint to connect to.

Run
---

Before executing the application you should open the AWS IoT console and
subscribe the corresponding topic to see the message sent by the application.
Follow these steps to do so:

1. Sign in to the **AWS Management Console** and open the **AWS IoT console**.
2. Click the **Test** option from the left menu to open the MQTT client panel.
3. Write the name of the topic you want to subscribe ('sample/xbee' by default)
   in the **Subscription topic** field.
4. Click **Subscribe topic** button to start monitoring messages sent to that
   topic.

Now you can compile and launch the example to publish data to the configured
MQTT topic. 

When the module has joined the cellular network, you should see the output of
the sample. In this case it displays the result of the AWS connection and 
publishing operations:

    - Waiting for the module to be connected to the cellular network... [OK] 
    - Connecting to AWS... [OK]
    - Publishing message... [OK]
    - Done

Verify that the MQTT client panel displays the message sent from the XBee3 
Cellular device to the configured topic:

    {
      "message": "AWS Sample Message"
    }

Required libraries
--------------------

* umqtt

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