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

from machine import ADC
import time

# Pin D1 (DIO1/AD1)
ANALOG_PIN_ID = "D1"


def main():
    print(" +-------------------------------------+")
    print(" | XBee MicroPython Analog Read Sample |")
    print(" +-------------------------------------+\n")

    # Create an ADC object for pin AD1.
    adc_pin = ADC(ANALOG_PIN_ID)

    # Start reading the analog voltage value present at the pin.
    while True:
        print("- ADC value:", adc_pin.read())
        time.sleep(1)


if __name__ == '__main__':
    main()
