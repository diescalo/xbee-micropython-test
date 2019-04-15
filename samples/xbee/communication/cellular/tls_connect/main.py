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
