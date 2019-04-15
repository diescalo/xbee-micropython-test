# Copyright 2019, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import time
from digi import cloud
from machine import Pin

# Pin D9 (ON/SLEEP/DIO9)
LED_PIN_ID = "D9"
# Toggle LED command.
DR_CMD_TOGGLE = "TOGGLE LED"
# Toggle LED answer.
DR_ANSWER_TOGGLE = "LED TOGGLED"
# Unknown command answer.
DR_ANSWER_UNKNOWN = "UNKNOWN COMMAND"


print(" +---------------------------------------------+")
print(" | XBee MicroPython Read Device Request Sample |")
print(" +---------------------------------------------+\n")

# Set up the LED pin object to manage the LED status. Configure the pin
# as output and set its initial value to off (0).
led_pin = Pin(LED_PIN_ID, Pin.OUT, value=0)

# Start reading device requests.
while True:
    request = cloud.device_request_receive()
    if request is not None:
        # A device request has been received, process it.
        data = request.read()
        if data.decode("utf-8").strip() == DR_CMD_TOGGLE:
            print("- Toggle LED device request received.")
            led_pin.toggle()
            written = request.write(bytes(DR_ANSWER_TOGGLE, "utf-8"))
        else:
            written = request.write(bytes(DR_ANSWER_UNKNOWN, "utf-8"))
        request.close()

    time.sleep(5)
