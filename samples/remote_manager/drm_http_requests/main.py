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

import time
import xbee
from remotemanager import RemoteManagerConnection

# Constants
DRM_USER = "USER"
DRM_PASS = "PASSWORD"

STREAM_ID = "xbee_temperature"
STREAM_DESC = "Temperature of the XBee device"
STREAM_TYPE = "DOUBLE"
STREAM_UNITS = "Celsius"


def create_datastream(id, description, type, units=""):
    """
    Creates a datastream in Digi Remote Manager.

    :param id: The identifier of the datastream to create.
    :param description: The description of the datastream.
    :param type: Data type of the datastream.
    :param units: The units of the datastream.

    :return: `True` if the datastream is created successfully, `False`
        otherwise.
    """
    stream_info = {"description": description,
                   "id": id,
                   "type": type,
                   "units": units}
    try:
        response = rm.create_datastream(stream_info)
        return response is not None
    except OSError:
        return False


def upload_datapoint(stream_id, data):
    """
    Uploads a datapoint containing the given data to the datastream specified.

    :param stream_id: ID of the datastream to upload the datapoint to.
    :param data: Value of the datapoint to upload.

    :return: `True` if the datapoint is uploaded successfully, `False`
        otherwise.
    """
    try:
        response = rm.add_datapoint(stream_id, data)
        return response is not None
    except OSError:
        return False


print(" +-------------------------------------------+")
print(" | XBee MicroPython DRM HTTP Requests Sample |")
print(" +-------------------------------------------+\n")

# Create the connection with Digi Remote Manager.
credentials = {'username': DRM_USER, 'password': DRM_PASS}
rm = RemoteManagerConnection(credentials=credentials)

# Create the temperature datastream.
print("- Creating datastream '%s'... " % STREAM_ID, end="")
if create_datastream(STREAM_ID, STREAM_DESC, STREAM_TYPE, STREAM_UNITS):
    print("[OK]")
else:
    print("[ERROR]")

# Start uploading temperature samples.
while True:
    temperature = int(xbee.atcmd('TP') * 9.0 / 5.0 + 32.0)
    print("- Uploading datapoint to datastream '%s'... " % STREAM_ID, end="")
    if create_datastream(STREAM_ID, STREAM_DESC, STREAM_TYPE, STREAM_UNITS):
        print("[OK]")
    else:
        print("[ERROR]")
    time.sleep(30)
