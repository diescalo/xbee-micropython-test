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

from typing import Any, Tuple


def calcsize(fmt: str) -> int:
    """
    Returns the number of bytes needed to store the given ``fmt``.

    :param fmt: Identifier of the typecode to get its size.

    :return: The number of bytes needed.
    """
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """
    Returns a bytes object containing the values v1, v2, ... packed according
    to the format string ``fmt``.

    :param fmt: Format string sequence of the values to pack.
    :param v1: Value to pack.
    :param vn: Additional values to pack.

    :return: Bytes object with the values packed according to the given format.
    """
    ...

def pack_into(fmt: str, buff: Any, offset: int, v1: Any, *vn: Any) -> None:
    """
    Packs the values v1, v2, ... according to the format string ``fmt`` and
    writes the packed bytes into the writable buffer ``buf`` starting at
    ``offset``.

    **Note**: The offset is a required argument.

    :param fmt: Format string sequence of the values to pack.
    :param buff: Buffer to write the packed values into.
    :param offset: Starting offset to pack values within the buffer.
    :param v1: Value to pack.
    :param vn: Additional values to pack.
    """
    ...

def unpack(fmt: str, buffer: Any) -> Tuple:
    """
    Returns a tuple containing values unpacked according to the format string
    ``fmt``. The buffer's size in bytes must be ``calcsize(fmt)``.

    :param fmt: Format string sequence of the packed values.
    :param buffer: Buffer containing the packed values to unpack.

    :return: Tuple containing the unpacked values.
    """
    ...

def unpack_from(fmt: str, buffer: Any, offset: int=0) -> None:
    """
    Returns a tuple containing values unpacked according to the format string
    ``fmt``.  The buffer's size, minus ``offset``, must be at least
    ``calcsize(fmt)``.

    :param fmt: Format string sequence of the packed values.
    :param buffer: Buffer containing the packed values to unpack.
    :param offset: Offset within buffer to start unpacking values.

    :return: Tuple containing the unpacked values.
    """
    ...
