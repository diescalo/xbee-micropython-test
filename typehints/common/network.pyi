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

from typing import Any, Optional, Tuple


class Cellular:
    """
    Class that provides a driver for the cellular modem in an XBee cellular
    device.
    """

    def config(self, param: Optional[str]=None, **kwargs: Any) -> \
            Optional[Any]:
        """
        Gets or sets general network interface parameters. This methods allows
        to work with additional parameters beyond standard IP configuration.

        * For **setting** parameters, keyword argument syntax should be used,
          multiple parameters can be set at once.
        * For **querying** parameters, name should be quoted as a string, and
          only one parameter can be queries at time.

        Available network parameters are:

        * ``apn`` - Access Point Name
        * ``iccid`` - SIM card number
        * ``imei`` - International Mobile Equipment Identity
        * ``operating_apn`` - Operating Access Point Name
        * ``operator`` - Network operator
        * ``phone`` - Phone number

        :param param: When querying a parameter, the name of the parameter.
            Example::

                c = network.Cellular()
                print('Phone:', c.config('phone'))
        :param kwargs: When setting parameters, the name of each parameter to
            set with its corresponding value. Example::

                c = network.Cellular()
                c.config(apn='ac.vodafone.es')

        :return: When querying a parameter, the value of that parameter.
        """
        ...

    def ifconfig(self) -> Tuple[str, str, str, str]:
        """
        Gets the IP-level network interface parameters:

        * IP address
        * Subnet mask
        * Gateway
        * DNS server

        :return: A 4-tuple containing the IP addressing information including:

            * IP address
            * Subnet mask
            * Gateway
            * DNS server
        """
        ...

    def isconnected(self) -> bool:
        """
        Determines whether the XBee Cellular Modem is connected to a network.

        :return: ``True`` if the XBee Cellular Modem is connected to a cellular
            network and has a valid IP address, ``False`` otherwise.
        """
        ...

    def active(self, mode: bool) -> None:
        """
        Sets whether the XBee Cellular Modem is powered on or in
        airplane mode.

        If ``mode`` parameter is provided, the method sets the airplane mode,
        otherwise the method returns the status of the airplane mode.

        :param mode: ``True to make the XBee Cellular modem enter airplane
            mode, ``False`` to make it leave airplane mode.

        :return: ``True`` if the XBee Cellular Modem is powered on or ``False``
            if the XBee Cellular Modem is in airplane mode.
        """
        ...

    def sms_receive(self) -> Optional[dict]:
        """
        Returns the latest SMS message received or ``None`` if there is no
            message

        :return: The latest SMS message received or ``None`` if there is no
            message. Message is returned as a dictionary with the following
            keys:

            * ``message`` - The message text, which is converted to a 7-bit
              ASCII with extended Unicode characters changed to spaces.
            * ``sender`` - The phone number from which the message was sent.
            * ``timestamp`` - The number of seconds since 1/1/2000, which is
              passed to ``time.localtime()`` and then converted into a tuple
              of datetime elements.
        """
        ...

    def sms_send(self, phone: Any, message: Any) -> None:
        """
        Sends a message to a phone using SMS.

        The method can throw any of the following exceptions if an error occurs
        sending the SMS message:

        * ``ValueError`` - For invalid parameters
        * ``OSError``:

          * ``ENOTCONN`` - The cellular mode has not connected.
          * ``ETIMEDOUT`` - If the network doesn't acknowledge the message in
            a reasonable amount of time.
          * ``EIO```- If there was some other error in sending the message.

        :param phone: The phone number of the device to which the message
            should be sent. This variable can be a string or an integer.
        :param message: The contents of the message. The message should be a
            string or a bytes object of 7-bit ASCII characters.
        """
        ...
