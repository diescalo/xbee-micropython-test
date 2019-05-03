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


SERIAL: int = ...
BLUETOOTH: int = ...
MICROPYTHON: int = ...
MAX_DATA_LENGTH: int = ...

def receive() -> dict:
    """
    Returns a relay data entry.

    :return: A received relay data entry as a dictionary containing the
        following elements:

        * ``sender``: The source interface. One of:

            * ``relay.SERIAL``
            * ``relay.BLUETOOTH``
            * ``relay.MICROPYTHON``
        * ``message``: The received data in bytearray format.
    """
    ...

def send(dest: int, data: Any) -> None:
    """
    Sends data to a destination interface. You can send a maximum of
    ``relay.MAX_DATA_LENGTH`` bytes in a single frame.

    The ``send()`` method throws exceptions in at least the following cases:

    * ``ValueError`` or ``TypeError`` for invalid parameters.
    * ``OSError(ENOBUFS)`` if unable to allocate a buffer for the frame.
    * ``OSError(ENODEV)`` for invalid ``dest`` parameter.
    * ``OSError(ECONNREFUSED)`` when destination is not accepting frames (for
      example, the serial interface is not in API mode, Bluetooth is not
      connected and unlocked, the queue is full or delivery failed).

    :param dest: Destination interface to transmit the data. One of:

        * ``relay.SERIAL``
        * ``relay.BLUETOOTH``
        * ``relay.MICROPYTHON`` (for loopback)
    :param data: Data to send in bytearray or string format or any other object
        that implements the **buffer** protocol.
    """
    ...
