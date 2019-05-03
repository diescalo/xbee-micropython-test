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


def dump(obj: Any, stream: Any) -> None:
    """
    Serialises ``obj`` to a JSON string, writing it to the given ``stream``.

    :param obj: Object to serialise to a JSON string.
    :param stream: Destination stream to write the serialised object (a
        .write()-supporting file-like object)
    """
    ...

def dumps(obj: Any) -> str:
    """
    Returns object ``obj`` represented as a JSON string.

    :param obj: Object to serialise to a JSON string.

    :return: Object ``obj`` represented as a JSON string.
    """
    ...

def load(stream: Any) -> Any:
    """
    Parses the given stream, interpreting it as a JSON string and deserialising
    the data to a Python object. The resulting object is returned.

    Parsing continues until end-of-file is encountered. A ValueError is raised
    if the data in stream is not correctly formed.

    :param stream: Source stream to read the JSON string to deserialise (a
        .read()-supporting text file or binary file containing a JSON document)

    :return: A Python object corresponding to the read JSON string.
    """
    ...

def loads(json_string: str) -> Any:
    """
    Parses the given JSON string and returns a Python object. Raises
    ``ValueError`` if the string is not correctly formed.

    :param json_string: String containing the JSON document to deserialise.

    :return: A Python object corresponding to the given JSON string.
    """
    ...
