# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.16, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_16 import models

class Audit(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'arguments': 'str',
        'command': 'str',
        'ip_address': 'str',
        'subcommand': 'str',
        'time': 'int',
        'user': 'str',
        'user_agent': 'str',
        'user_interface': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'arguments': 'arguments',
        'command': 'command',
        'ip_address': 'ip_address',
        'subcommand': 'subcommand',
        'time': 'time',
        'user': 'user',
        'user_agent': 'user_agent',
        'user_interface': 'user_interface'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        arguments=None,  # type: str
        command=None,  # type: str
        ip_address=None,  # type: str
        subcommand=None,  # type: str
        time=None,  # type: int
        user=None,  # type: str
        user_agent=None,  # type: str
        user_interface=None,  # type: str
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            arguments (str)
            command (str)
            ip_address (str)
            subcommand (str)
            time (int)
            user (str)
            user_agent (str)
            user_interface (str): The user interface through which the user session event was performed. Valid values are `CLI`, `GUI`, and `REST`.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if arguments is not None:
            self.arguments = arguments
        if command is not None:
            self.command = command
        if ip_address is not None:
            self.ip_address = ip_address
        if subcommand is not None:
            self.subcommand = subcommand
        if time is not None:
            self.time = time
        if user is not None:
            self.user = user
        if user_agent is not None:
            self.user_agent = user_agent
        if user_interface is not None:
            self.user_interface = user_interface

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Audit`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(Audit, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Audit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
