# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.12, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_12 import models

class FileSession(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'authentication': 'str',
        'client': 'FixedReferenceNameOnly',
        'connection_time': 'int',
        'idle_time': 'int',
        'opens': 'int',
        'protocol': 'str',
        'port': 'int',
        'time': 'int',
        'user': 'UserNoId'
    }

    attribute_map = {
        'name': 'name',
        'authentication': 'authentication',
        'client': 'client',
        'connection_time': 'connection_time',
        'idle_time': 'idle_time',
        'opens': 'opens',
        'protocol': 'protocol',
        'port': 'port',
        'time': 'time',
        'user': 'user'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        authentication=None,  # type: str
        client=None,  # type: models.FixedReferenceNameOnly
        connection_time=None,  # type: int
        idle_time=None,  # type: int
        opens=None,  # type: int
        protocol=None,  # type: str
        port=None,  # type: int
        time=None,  # type: int
        user=None,  # type: models.UserNoId
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            authentication (str): Describes how was the user authenticated. Valid values include `KRB` and `NTLMv2`.
            client (FixedReferenceNameOnly): Client that holds the session.
            connection_time (int): Connection time in milliseconds since UNIX epoch.
            idle_time (int): Duration in milliseconds that indicates how long the session has been idle.
            opens (int): Number of opens for the given session.
            protocol (str): The protocol utilized for obtaining and managing the session. Valid values include `nfs` and `smb`.
            port (int): Port number the client is connected from.
            time (int): Current time in milliseconds since UNIX epoch.
            user (UserNoId): The user who has created the session.
        """
        if name is not None:
            self.name = name
        if authentication is not None:
            self.authentication = authentication
        if client is not None:
            self.client = client
        if connection_time is not None:
            self.connection_time = connection_time
        if idle_time is not None:
            self.idle_time = idle_time
        if opens is not None:
            self.opens = opens
        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if time is not None:
            self.time = time
        if user is not None:
            self.user = user

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FileSession`".format(key))
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
        if issubclass(FileSession, dict):
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
        if not isinstance(other, FileSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
