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

class NetworkInterfaceNeighbor(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'local_port': 'FixedReferenceNoId',
        'neighbor_chassis': 'NetworkInterfaceNeighborNeighborChassis',
        'neighbor_port': 'NetworkInterfaceNeighborNeighborPort',
        'initial_ttl_in_sec': 'int'
    }

    attribute_map = {
        'local_port': 'local_port',
        'neighbor_chassis': 'neighbor_chassis',
        'neighbor_port': 'neighbor_port',
        'initial_ttl_in_sec': 'initial_ttl_in_sec'
    }

    required_args = {
    }

    def __init__(
        self,
        local_port=None,  # type: models.FixedReferenceNoId
        neighbor_chassis=None,  # type: models.NetworkInterfaceNeighborNeighborChassis
        neighbor_port=None,  # type: models.NetworkInterfaceNeighborNeighborPort
        initial_ttl_in_sec=None,  # type: int
    ):
        """
        Keyword args:
            local_port (FixedReferenceNoId): A reference to the local network interface the neighbor is connected to.
            neighbor_chassis (NetworkInterfaceNeighborNeighborChassis)
            neighbor_port (NetworkInterfaceNeighborNeighborPort)
            initial_ttl_in_sec (int): The initial time to live in seconds from when the local port received notice that the neighbor information is regarded as valid. The time is not measured from when this endpoint was queried.
        """
        if local_port is not None:
            self.local_port = local_port
        if neighbor_chassis is not None:
            self.neighbor_chassis = neighbor_chassis
        if neighbor_port is not None:
            self.neighbor_port = neighbor_port
        if initial_ttl_in_sec is not None:
            self.initial_ttl_in_sec = initial_ttl_in_sec

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceNeighbor`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceNeighbor`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceNeighbor`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkInterfaceNeighbor`".format(key))
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
        if issubclass(NetworkInterfaceNeighbor, dict):
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
        if not isinstance(other, NetworkInterfaceNeighbor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
