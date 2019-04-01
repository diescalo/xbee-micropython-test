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

from machine import UART
import time


def main():
    print(" +-----------------------------------+")
    print(" | XBee MicroPython UART Echo Sample |")
    print(" +-----------------------------------+\n")

    # Instantiate a UART object with a baudrate of 9600.
    uart = UART(1, 9600)

    # Start echoing the read data.
    while True:
        if uart.any() > 0:
            read_text = uart.read(uart.any())
            uart.write(bytearray(read_text))
        time.sleep(0.1)


if __name__ == '__main__':
    main()
