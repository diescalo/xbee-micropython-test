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

from machine import Pin
import time

# Pin D0 (AD0/DIO0)
INPUT_PIN_ID = "D0"


def main():
    print(" +--------------------------------------------+")
    print(" | XBee MicroPython Digital Input Read Sample |")
    print(" +--------------------------------------------+\n")

    # Set up the LED pin object to check the input value. Configure the pin
    # as input and enable the internal pull-up.
    input_pin = Pin(INPUT_PIN_ID, Pin.IN, Pin.PULL_UP)

    # Start polling the value of the pin every second.
    while True:
        print("- Digital input value:", input_pin.value())
        time.sleep(1)


if __name__ == '__main__':
    main()
