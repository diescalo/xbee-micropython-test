Transmit Data with Node Identifier Sample Application
=====================================================

This example demonstrates the usage of the RF communication API by giving an
example of how to transmit data to other XBee device in the same network using
its node identifier.

Requirements
------------

To run this example you need:

* Two XBee3 radio modules with MicroPython support.
* Two carrier boards for the radio modules (XBIB-U-DEV or XBIB-C board).
* The XCTU application (available at www.digi.com/xctu).

Setup
-----

The XBee3 module that runs this sample will act as sender, while the other
one will act as receiver.

Make sure the hardware is set up correctly:

1. Plug the XBee3 radio modules into the XBee adapters and connect them to your
   computer's USB ports.
2. Ensure that the receiver module is in API mode and both modules are on the
   same network.
3. Set the node identifier (**NI**) of the receiver module to `RECEIVER`.

Run
---

Before launching the application, you need to set up XCTU to see the data
received by the receiver module. Follow these steps to do so:

1. Launch the XCTU application.
2. Add the receiver XBee module to XCTU.
3. Once the module is added, change to the **Consoles** working mode and open
   the serial connection.
   
Finally, compile and launch the MicroPython application. It prints out the
status of the operation in the console:

    Sending data to RECEIVER >> Hello XBee!
    Data sent successfully

Verify that a new **Receive packet** has been received in the XCTU console.
Select it and review the details, some of them similar to:

    - Start delimiter:         7E
    - Length:                  Depends on the XBee protocol
    - Frame type:              90 (Receive Packet)
    - 64-bit source address:   The XBee sender's 64-bit address
    - RF data (ASCII):         Hello XBee!

Supported platforms
-------------------

* Digi XBee3 Zigbee 3 - minimum firmware version: 1006
* Digi XBee3 802.15.4 - minimum firmware version: 2003
* Digi XBee3 DigiMesh 2.4 - minimum firmware version: 3002

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