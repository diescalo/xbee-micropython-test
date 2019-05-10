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
import uio
import uos
import xbee


# Pin D0 (AD0/DIO0)
BUTTON = "D0"
LOG_FILE = "temperature.log"


print(" +-------------------------------------+")
print(" | XBee MicroPython File System Sample |")
print(" +-------------------------------------+\n")

button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)

# If the log file exists, remove it.
try:
    log = uio.open(LOG_FILE)
    log.close()
    uos.remove(LOG_FILE)
except OSError:
    # Do nothing, the file does not exist.
    pass

print("Reading XBee's temperature, press the %s button to stop...\n" % BUTTON)

# Create and open the log file in the XBee's file system.
with uio.open(LOG_FILE, mode="a") as log:
    stopped = False
    while not stopped:
        temperature = xbee.atcmd("TP")
        # Write the current temperature in the log file.
        dummy = log.write("Current temperature: %.1F C (%.1F F)\n" % (temperature, temperature * 9.0 / 5.0 + 32.0))
        # Wait 1 second until the next reading.
        for x in range(10):
            if button.value() == 0:
                stopped = True
                break
            time.sleep(0.1)

print("Displaying log...\n")

# Open again the log file to read its contents.
with uio.open(LOG_FILE) as log:
    while True:
        line = log.readline()
        if not line:
            break
        print(line, end="")

print("\nLog file read")
