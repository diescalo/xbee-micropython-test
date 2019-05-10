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

import urequests

TLS_SERVER = "https://auth.pizza"

PRIVATE_KEY = "cert/pizza-client.key"
CLIENT_CERTIFICATE = "cert/pizza-client.pem"
CA_CERTIFICATE = "cert/pizza-server-ca.pem"


print(" +-----------------------------------------------+")
print(" | XBee MicroPython TLS Connect URequests Sample |")
print(" +-----------------------------------------------+\n")

# Connect to the server and get the request answer.
print("Connecting with TLS server...")
r = urequests.get(TLS_SERVER,
                  headers={'Accept': 'application/json'},
                  verify=CA_CERTIFICATE,
                  cert=(CLIENT_CERTIFICATE, PRIVATE_KEY))

print("Answer:\n%s" % r.text)
