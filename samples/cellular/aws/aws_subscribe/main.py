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

from umqtt.simple import MQTTClient
import network
import time

# AWS endpoint parameters.
HOST = b'FILL_ME_IN'    # ex: b'abcdefg1234567'
REGION = b'FILL_ME_IN'  # ex: b'us-east-1'

CLIENT_ID = "clientID"  # Should be unique for each device connected.
AWS_ENDPOINT = b'%s.iot.%s.amazonaws.com' % (HOST, REGION)

# SSL certificates.
SSL_PARAMS = {'keyfile': "/flash/cert/aws.key",
              'certfile': "/flash/cert/aws.crt",
              'ca_certs': "/flash/cert/aws.ca"}

TOPIC = "sample/xbee"


def sub_cb(topic, msg):
    """
    Callback executed when messages from subscriptions are received. Prints
    the topic and the message.

    :param topic: Topic of the message.
    :param msg: Received message.
    """

    global msgs_received

    msgs_received += 1
    print("- Message received!")
    print("   * %s: %s" % (topic.decode("utf-8"), msg.decode("utf-8")))


def subscribe_test(client_id=CLIENT_ID, hostname=AWS_ENDPOINT, sslp=SSL_PARAMS,
                   msg_limit=2):
    """
    Connects to AWS, subscribes to a topic and starts listening for messages.

    :param client_id: Unique identifier for the device connected.
    :param hostname: AWS hostname to connect to.
    :param sslp: SSL certificate parameters.
    :param msg_limit: Maximum number of messages to receive before
        disconnecting from AWS..
    """

    global msgs_received

    # Connect to AWS.
    client = MQTTClient(client_id, hostname, ssl=True, ssl_params=sslp)
    client.set_callback(sub_cb)
    print("- Connecting to AWS... ", end="")
    client.connect()
    print("[OK]")
    # Subscribe to topic.
    print("- Subscribing to topic '%s'... " % TOPIC, end="")
    client.subscribe(TOPIC)
    print("[OK]")
    # Wait for messages.
    msgs_received = 0
    print('- Waiting for messages...')
    while msgs_received < msg_limit:
        client.check_msg()
        time.sleep(1)
    # Disconnect.
    client.disconnect()
    print("- Done")


print(" +---------------------------------------+")
print(" | XBee MicroPython AWS Subscribe Sample |")
print(" +---------------------------------------+\n")

msgs_received = 0
conn = network.Cellular()

print("- Waiting for the module to be connected to the cellular network... ",
      end="")
while not conn.isconnected():
    time.sleep(5)
print("[OK]")

subscribe_test()
