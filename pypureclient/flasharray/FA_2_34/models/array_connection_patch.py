# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.34
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_34 import models

class ArrayConnectionPatch(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_limit': 'int',
        'window': 'TimeWindow',
        'window_limit': 'int',
        'management_address': 'str',
        'replication_addresses': 'list[str]',
        'type': 'str',
        'connection_key': 'str',
        'encryption': 'str',
        'throttle': 'Throttle'
    }

    attribute_map = {
        'default_limit': 'default_limit',
        'window': 'window',
        'window_limit': 'window_limit',
        'management_address': 'management_address',
        'replication_addresses': 'replication_addresses',
        'type': 'type',
        'connection_key': 'connection_key',
        'encryption': 'encryption',
        'throttle': 'throttle'
    }

    required_args = {
    }

    def __init__(
        self,
        default_limit=None,  # type: int
        window=None,  # type: models.TimeWindow
        window_limit=None,  # type: int
        management_address=None,  # type: str
        replication_addresses=None,  # type: List[str]
        type=None,  # type: str
        connection_key=None,  # type: str
        encryption=None,  # type: str
        throttle=None,  # type: models.Throttle
    ):
        """
        Keyword args:
            default_limit (int): Deprecated. Default maximum bandwidth threshold for outbound traffic in bytes. Once exceeded, bandwidth throttling occurs.
            window (TimeWindow): Deprecated. The time during which the `window_limit` threshold is in effect.
            window_limit (int): Deprecated. Maximum bandwidth threshold for outbound traffic during the specified `window_limit` time range in bytes. Once exceeded, bandwidth throttling occurs.
            management_address (str): Management IP address of the target array.
            replication_addresses (list[str]): IP addresses and FQDNs of the target arrays. Configurable only when `replication_transport` is set to `ip`.
            type (str): The type of replication. Valid values are `async-replication` and `sync-replication`.
            connection_key (str): The connection key of the target array. It is only required when `encryption` is changed from `unencrypted` to `encrypted`, or when `type` is changed from `async-replication` to `sync-replication`.
            encryption (str): If `encrypted`, encryption will be enabled for all traffic over this array connection. `connection_key` must be specified when encrypted is set to `true`. If `unencrypted`, encryption will be disabled for all traffic over this array connection. If not specified, the current encryption option for the array connection will remain unchanged.
            throttle (Throttle)
        """
        if default_limit is not None:
            self.default_limit = default_limit
        if window is not None:
            self.window = window
        if window_limit is not None:
            self.window_limit = window_limit
        if management_address is not None:
            self.management_address = management_address
        if replication_addresses is not None:
            self.replication_addresses = replication_addresses
        if type is not None:
            self.type = type
        if connection_key is not None:
            self.connection_key = connection_key
        if encryption is not None:
            self.encryption = encryption
        if throttle is not None:
            self.throttle = throttle

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnectionPatch`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnectionPatch`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnectionPatch`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnectionPatch`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

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
        if issubclass(ArrayConnectionPatch, dict):
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
        if not isinstance(other, ArrayConnectionPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
