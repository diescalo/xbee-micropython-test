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

# Pin D4 (DIO4/SPI_MOSI)
LED_PIN_ID = "D4"


def main():
    print(" +--------------------------------------+")
    print(" | XBee MicroPython Blinking LED Sample |")
    print(" +--------------------------------------+\n")

    # Set up the LED pin object to manage the LED status. Configure the pin
    # as output and set its initial value to off (0).
    led_pin = Pin(LED_PIN_ID, Pin.OUT, value=0)

    # Start blinking the LED by toggling its value every second.
    while True:
        print("- Turn Off LED")
        led_pin.value(0)
        time.sleep(1)

        print("- Turn on LED")
        led_pin.value(1)
        time.sleep(1)


if __name__ == '__main__':
    main()
