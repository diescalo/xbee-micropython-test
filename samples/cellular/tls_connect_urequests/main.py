# Copyright (c) 2019, Digi International, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
