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
import xbee


print(" +---------------------------------------+")
print(" | XBee MicroPython Prevent Sleep Sample |")
print(" +---------------------------------------+\n")

xb = xbee.XBee()

while True:
    # Interruptable stuff.
    print("-" * 20)
    interruptable_counter = 0
    while interruptable_counter < 10:
        interruptable_counter += 1
        print("Interruptable counter: %s" %
              interruptable_counter)
        time.sleep(1)

    with xb.wake_lock:
        # Not interruptable (important) stuff.
        print("-" * 20)
        not_interruptable_counter = 0
        while not_interruptable_counter < 10:
            not_interruptable_counter += 1
            print("Not interruptable counter: %s" %
                  not_interruptable_counter)
            time.sleep(1)
