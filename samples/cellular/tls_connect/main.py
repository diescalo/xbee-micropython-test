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

import usocket, ussl

TLS_SERVER = "pizza.auth"

PRIVATE_KEY = "cert/pizza-client.key"
CLIENT_CERTIFICATE = "cert/pizza-client.pem"
CA_CERTIFICATE = "cert/pizza-server-ca.pem"


print(" +-------------------------------------+")
print(" | XBee MicroPython TLS Connect Sample |")
print(" +-------------------------------------+\n")

proto = usocket.IPPROTO_SEC

s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM, proto)
w = ussl.wrap_socket(s,
                     keyfile=PRIVATE_KEY,
                     certfile=CLIENT_CERTIFICATE,
                     ca_certs=CA_CERTIFICATE)

# Connect to the server and get the request answer.
print("Connecting with TLS server...")
w.connect((TLS_SERVER, 443))
w.write(b'GET / HTTP/1.0\r\n'
        b'Host: auth.pizza\r\n'
        b'Accept: application/json\r\n\r\n')

print("Answer:\n%s" % str(w.read(4096), 'utf-8'))

w.close()
