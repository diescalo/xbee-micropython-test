# Copyright 2019, Digi International Inc.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import socket
from ssl import SSLSocket
from typing import Optional


def wrap_socket(sock: socket, *, keyfile: Optional[str] = None,
                certfile: Optional[str] = None, ca_certs: Optional[str] = None,
                server_side: bool = False,
                server_hostname: Optional[str] = None) -> SSLSocket:
    """
    Takes a ``stream`` sock (usually ``usocket.socket`` instance of
    ``SOCK_STREAM`` type), and returns an instance of ``ssl.SSLSocket``, which
    wraps the underlying stream in an SSL context.

    Returned object has the usual ``stream`` interface methods like ``read()``,
    ``write()``, etc. In MicroPython, the returned object does not expose
    socket interface and methods like ``recv()``, ``send()``. In particular, a
    server-side SSL socket should be created from a normal socket returned from
    ``accept()`` on a non-SSL listening server socket.

    **Note**: Filenames provided in the method are relative to MicroPython's
    current working directory, which defaults to **/flash** and changes via the
    ``uos.chdir()`` method. Use an absolute path like
    **/flash/cert/server.pem** to ignore the current working directory when
    resolving the filename.

    :param sock: ``socket`` object created with ``IPPROTO_SEC`` and not already
        wrapped.
    :param keyfile: Name of a file containing the private key for certfile
        (also stored as a Base64 PEM file).
    :param certfile: Name of a file containing this device's public X.509
        certificate as a Base64 PEM file. When specifying ``certfile``, you
        must also specify ``keyfile`` and ``ca_certs``.
    :param ca_certs: Name of a file containing a single public X.509
        certificate of the trusted certificate authority (CA) for the remote
        host. Connections with remote devices only succeed if they have a
        certificate signed by the CA listed in ``ca_certs``. Unlike Python3,
        which supports multiple certificates in ``ca_certs``, MicroPython on
        the XBee Cellular Modem only supports a single certificate in this
        file. In order to authenticate a server not participating in a PKI
        (using CAs) the server must present a self-signed certificate. That
        certificate can be used in the ``ca_certs`` field to authenticate that
        single server.
    :param server_side: Currently ignored.
    :param server_hostname: Reserved for future support of Server Name
        Indication (SNI).

    :return: The wrapped socket object as a ``SSLSocket`` object.
    """
    ...
