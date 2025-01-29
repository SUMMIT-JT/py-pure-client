# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_21 import models

class NetworkInterface(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'enabled': 'bool',
        'interface_type': 'str',
        'services': 'list[str]',
        'speed': 'int',
        'eth': 'NetworkInterfaceEth',
        'fc': 'NetworkInterfaceFc'
    }

    attribute_map = {
        'name': 'name',
        'enabled': 'enabled',
        'interface_type': 'interface_type',
        'services': 'services',
        'speed': 'speed',
        'eth': 'eth',
        'fc': 'fc'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        enabled=None,  # type: bool
        interface_type=None,  # type: str
        services=None,  # type: List[str]
        speed=None,  # type: int
        eth=None,  # type: models.NetworkInterfaceEth
        fc=None,  # type: models.NetworkInterfaceFc
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified.
            enabled (bool): Returns a value of `true` if the specified network interface or Fibre Channel port is enabled. Returns a value of `false` if the specified network interface or Fibre Channel port is disabled.
            interface_type (str): The interface type. Valid values are `eth` and `fc`.
            services (list[str]): The services provided by the specified network interface or Fibre Channel port.
            speed (int): Configured speed of the specified network interface or Fibre Channel port (in Gb/s). Typically this is the maximum speed of the port or bond represented by the network interface.
            eth (NetworkInterfaceEth)
            fc (NetworkInterfaceFc)
        """
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if interface_type is not None:
            self.interface_type = interface_type
        if services is not None:
            self.services = services
        if speed is not None:
            self.speed = speed
        if eth is not None:
            self.eth = eth
        if fc is not None:
            self.fc = fc

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterface`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterface`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterface`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterface`".format(key))
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
        if issubclass(NetworkInterface, dict):
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
        if not isinstance(other, NetworkInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
