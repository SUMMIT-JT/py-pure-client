# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_5 import models

class NetworkinterfacepostEth(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'str',
        'subinterfaces': 'list[ReferenceNoId]',
        'subnet': 'ReferenceNoId',
        'subtype': 'str'
    }

    attribute_map = {
        'address': 'address',
        'subinterfaces': 'subinterfaces',
        'subnet': 'subnet',
        'subtype': 'subtype'
    }

    required_args = {
    }

    def __init__(
        self,
        address=None,  # type: str
        subinterfaces=None,  # type: List[models.ReferenceNoId]
        subnet=None,  # type: models.ReferenceNoId
        subtype=None,  # type: str
    ):
        """
        Keyword args:
            address (str): The IPv4 or IPv6 address to be associated with the specified network interface.
            subinterfaces (list[ReferenceNoId]): List of network interfaces configured to be a subinterface of the specified network interface.
            subnet (ReferenceNoId): Subnet that is associated with the specified network interface.
            subtype (str): The subtype of the specified network interface. Only interfaces of subtype `vif` and `lacp_bond` can be created. Configurable on POST only. Valid values are `failover_bond`, `lacp_bond`, `physical`, and `vif`. If the subtype is `vif`, the services parameter must not be set.
        """
        if address is not None:
            self.address = address
        if subinterfaces is not None:
            self.subinterfaces = subinterfaces
        if subnet is not None:
            self.subnet = subnet
        if subtype is not None:
            self.subtype = subtype

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkinterfacepostEth`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkinterfacepostEth`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkinterfacepostEth`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkinterfacepostEth`".format(key))
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
        if issubclass(NetworkinterfacepostEth, dict):
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
        if not isinstance(other, NetworkinterfacepostEth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
