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


class sha256(object):
    """
    SHA256 hasher object. The current generation, modern hashing algorithm
    (of SHA2 series). It is suitable for cryptographically-secure purposes.
    """

    def __init__(self, data: Any=None) -> None:
        """
        Class constructor. Instantiates a ``sha256`` hasher object and
        optionally feeds data into it.

        :param data: Initial binary data to add to hash.
        """
        ...

    def update(self, data: Any) -> None:
        """
        Feeds more binary data into hash.

        :param data: Binary data to add to hash.
        """
        ...

    def digest(self) -> bytes:
        """
        Returns hash for all data passed through hash, as a bytes object. After
        this method is called, more data cannot be fed into hash any longer.

        :return: Bytes object with hash for all data passed.
        """
        ...
