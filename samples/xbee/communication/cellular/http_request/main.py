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

import network
import socket
import time


HOST = "http://www.micropython.org/ks/test.html"


print(" +--------------------------------------+")
print(" | XBee MicroPython HTTP Request Sample |")
print(" +--------------------------------------+\n")

cellular = network.Cellular()

print("Waiting for the module to be connected to the cellular network...")

# Before sending HTTP request, wait until the module is connected to the cellular network.
while not cellular.isconnected():
    time.sleep(1)

scheme, _, host, path = HOST.split("/", 3)

# Create the socket.
s = socket.socket()

try:
    # Connect to the host using the port 80 (HTTP).
    s.connect((host, 80))

    request = bytes("GET /%s HTTP/1.1\r\nHost: %s...\r\n\r\n" % (path, host), "utf8")
    print("Requesting /%s from host %s\n" % (path, host))

    # Send the HTTP request.
    s.send(request)

    while True:
        # Receive data from the socket.
        data = s.recv(500)
        print(str(data, "utf8"), end="")
finally:
    s.close()
