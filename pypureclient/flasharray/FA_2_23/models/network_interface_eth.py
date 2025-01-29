# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_23 import models

class NetworkInterfaceEth(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'str',
        'gateway': 'str',
        'mac_address': 'str',
        'mtu': 'int',
        'netmask': 'str',
        'subtype': 'str',
        'subinterfaces': 'list[FixedReferenceNoId]',
        'subnet': 'ReferenceNoId',
        'vlan': 'int'
    }

    attribute_map = {
        'address': 'address',
        'gateway': 'gateway',
        'mac_address': 'mac_address',
        'mtu': 'mtu',
        'netmask': 'netmask',
        'subtype': 'subtype',
        'subinterfaces': 'subinterfaces',
        'subnet': 'subnet',
        'vlan': 'vlan'
    }

    required_args = {
    }

    def __init__(
        self,
        address=None,  # type: str
        gateway=None,  # type: str
        mac_address=None,  # type: str
        mtu=None,  # type: int
        netmask=None,  # type: str
        subtype=None,  # type: str
        subinterfaces=None,  # type: List[models.FixedReferenceNoId]
        subnet=None,  # type: models.ReferenceNoId
        vlan=None,  # type: int
    ):
        """
        Keyword args:
            address (str): The IPv4 or IPv6 address to be associated with the specified network interface.
            gateway (str): The IPv4 or IPv6 address of the gateway through which the specified network interface is to communicate with the network.
            mac_address (str): The media access control address associated with the specified network interface.
            mtu (int): Maximum message transfer unit (packet) size for the network interface, in bytes. MTU setting cannot exceed the MTU of the corresponding physical interface.
            netmask (str): Netmask of the specified network interface that, when combined with the address of the interface, determines the network address of the interface.
            subtype (str): The subtype of the specified network interface. Only interfaces of subtype `virtual` can be created. Configurable on POST only. Valid values are `failover_bond`, `lacp_bond`, `physical`, and `virtual`.
            subinterfaces (list[FixedReferenceNoId]): List of network interfaces configured to be a subinterface of the specified network interface.
            subnet (ReferenceNoId): Subnet that is associated with the specified network interface.
            vlan (int): VLAN ID
        """
        if address is not None:
            self.address = address
        if gateway is not None:
            self.gateway = gateway
        if mac_address is not None:
            self.mac_address = mac_address
        if mtu is not None:
            self.mtu = mtu
        if netmask is not None:
            self.netmask = netmask
        if subtype is not None:
            self.subtype = subtype
        if subinterfaces is not None:
            self.subinterfaces = subinterfaces
        if subnet is not None:
            self.subnet = subnet
        if vlan is not None:
            self.vlan = vlan

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceEth`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceEth`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceEth`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceEth`".format(key))
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
        if issubclass(NetworkInterfaceEth, dict):
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
        if not isinstance(other, NetworkInterfaceEth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
