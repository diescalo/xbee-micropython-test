MQTT Publish Subscribe Sample Application
=========================================

This example uses the 'mqtt' library to connect with an MQTT server and 
test both the subscribe and publish topic operations. 

The example connects with the server and subscribes to the 'xbee_topic' topic.
Then, monitors the value of the `D0` button of the board and, whenever the 
button is pressed, it publishes a message to the same topic it subscribed
before. This way, the subscribe and publish features are demonstrated in the
same sample.

The sample uses the publicly 'test.mosquitto.org' MQTT server.

Requirements
------------

To run this example you need:

* One XBee3 Cellular module with MicroPython support and a micro SIM card
  inserted with Internet capabilities.
* One carrier board for the radio module (XBIB-U-DEV or XBIB-C board).
 
Setup
-----

Make sure the hardware is set up correctly and the code is configured and
ready:

1. Plug the XBee3 radio module into the XBee adapter and connect it to your
   computer's USB port.

Run
---

The example is already configured, so all you need to do is to compile and
launch the application.

When the module has joined the cellular network, you should see the output of
the sample. In this case it displays the result of the MQTT connection and 
subscribing operations:

    - Waiting for the module to be connected to the cellular network... [OK]
    - Connecting to 'test.mosquitto.org'... [OK]
    - Subscribing to topic 'xbee_topic'... [OK]
    - Press 'D0' button to publish a message.
    
Now you need press the button corresponding to the 'D0'. By default the button
corresponds to **SW2** in XBIB-U-DEV carrier boards and **Comm DIO0** in XBIB-C
carrier boards.

Once the button is pressed, the application sends the message 'Test from XBee!'
to the topic 'xbee_topic' (the one it subscribed before). The application
should receive and print the message immediately: 

    - Publishing message... [OK]
    - Message received!
       * xbee_topic: Test from XBee!

Press the button more times and verify every time the button is pressed a
message is published and received by the XBee module.  

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