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

from typing import Any


def hexlify(data: Any, sep: Any="") -> bytes:
    """
    Returns the hexadecimal representation of the provided binary data.

    :param data: Binary data to convert.
    :param sep: If supplied, this parameter is used as separator between
        hexadecimal values.

    :return: Bytes string with the hexadecimal representation.
    """
    ...

def unhexlify(data: Any) -> bytes:
    """
    Converts hexadecimal data to binary representation. Inverse of
    ``ubinascii.hexlify()``.

    :param data: Hexadecimal data to convert.

    :return: Bytes string with the binary representation.
    """
    ...

def a2b_base64(data: Any) -> bytes:
    """
    Decodes base64-encoded data, ignoring invalid characters in the input and
    returns the decoded data. Conforms to RFC 2045 s.6.8.

    :param data: The base64-encoded data to decode.

    :return: Bytes string with the decoded data.
    """
    ...

def b2a_base64(data: Any) -> bytes:
    """
    Encodes binary data in base64 format, as in RFC 3548 and returns the
    encoded data followed by a newline character, as a bytes object.

    :param data: Binary data to encode in base64 format.

    :return: Bytes string with the encoded data.
    """
    ...

def crc32(data: Any, crc: int=0) -> int:
    """
    Computes CRC-32 incrementally, the 32-bit checksum of ``data``, starting
    with an initial CRC of ``crc``.

    :param data: Data to obtain its 32-bit checksum.
    :param crc: Starting CRC value.

    :return: 32-bit checksum of the provided data.
    """
    ...
