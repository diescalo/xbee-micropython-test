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

# Pin D3 (AD3/DIO3)
ADC_PIN_ID = "D3"


print(" +-------------------------------------+")
print(" | XBee MicroPython ADC Polling Sample |")
print(" +-------------------------------------+\n")

# Create an ADC object for pin DIO0/AD0.
adc_pin = ADC(ADC_PIN_ID)

# Start reading the analog voltage value present at the pin.
while True:
    print("- ADC value:", adc_pin.read())
    time.sleep(1)
