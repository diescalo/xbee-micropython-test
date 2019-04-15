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
import xbee

# Pin D0 (AD0/DIO0)
INPUT_PIN_ID = "D0"


print(" +---------------------------------------+")
print(" | XBee MicroPython Prevent Sleep Sample |")
print(" +---------------------------------------+\n")

# Set up the pin object to check the input value of the user button. Configure
# the pin as input and enable the internal pull-up.
input_pin = Pin(INPUT_PIN_ID, Pin.IN, Pin.PULL_UP)

xb = xbee.XBee()

print("How to use this example:")
print("* Option 1")
print("  1. Press 'User button' (SW2 in XBIB-U-DEV board and COMM DIO0 in "
      "XBIB-C board).")
print("  2. Wait for the module to go to sleep (ON SLEEP LED turns off)")
print("  3. Try to send a ^C (cancel) to exit example program while the "
      "module is sleeping. Nothing happens because the module does not "
      "listen REPL events while it sleeps.")
print("  4. Let the program run until it wakes from 30 seconds sleep. Just "
      "after that time the module wakes and application displays the amount "
      "of ms the module was sleeping.")
print("* Option 2")
print("  1. Press 'User button' (SW2 in XBIB-U-DEV board and COMM DIO0 in "
      "XBIB-C board).")
print("  2. Just after pressing the button disconnect the XBee REPL Console "
      "(this is necessary to free the **DTR** pin of the module, which "
      "controls the early wake feature).")
print("  3. Wait for the module to go to sleep (ON SLEEP LED turns off).")
print("  4. While its sleeping, toggle DTR pin by connecting the XBee REPL "
      "console.")
print("  5. Module wakes as soon as the connection with the REPL is "
      "established. Application displays the amount of ms the module was "
      "sleeping and an early wake notification.")

print("\nWaiting for 'User button' to be pressed to Sleep...")

while True:
    # Check if the switch is pressed.
    if input_pin.value() == 0:
        # Sleep for 30 seconds and enable the early wake up with DTR pin.
        print("  - Sleeping for 30 seconds...")
        sleep_ms = xb.sleep_now(30000, True)
        # Module woke up.
        print("  - Woke up! Slept for %u ms" % sleep_ms)
        if xb.wake_reason() is xbee.PIN_WAKE:
            print("      * Woke early on DTR toggle")

        print("\nWaiting for 'User button' to be pressed to Sleep...")
