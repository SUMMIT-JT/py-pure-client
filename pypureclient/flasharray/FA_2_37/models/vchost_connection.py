# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.37
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_37 import models

class VchostConnection(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'protocol_endpoint': 'FixedReference',
        'vchost': 'FixedReference',
        'all_vchosts': 'bool'
    }

    attribute_map = {
        'protocol_endpoint': 'protocol_endpoint',
        'vchost': 'vchost',
        'all_vchosts': 'all_vchosts'
    }

    required_args = {
    }

    def __init__(
        self,
        protocol_endpoint=None,  # type: models.FixedReference
        vchost=None,  # type: models.FixedReference
        all_vchosts=None,  # type: bool
    ):
        """
        Keyword args:
            protocol_endpoint (FixedReference): A reference to the protocol endpoint, representing a storage container that vCenter can use.
            vchost (FixedReference): For vchost-connections, a vchost represents a vCenter. By connecting to a protocol endpoint, the corresponding vCenter gets the access to the storage container represented by this protocol endpoint. The vchost name should be null if `all_vchosts` is set to `true`, which means the storage container is accessible to all vchosts.
            all_vchosts (bool): If set to `true`, the storage container represented by the protocol endpoint is accessible to all vchosts. If set to `false`, the storage container represented by the protocol endpoint is only accesible to the vchosts that have explicit vchost-connections to this protocol endpoint. The default is `false`.
        """
        if protocol_endpoint is not None:
            self.protocol_endpoint = protocol_endpoint
        if vchost is not None:
            self.vchost = vchost
        if all_vchosts is not None:
            self.all_vchosts = all_vchosts

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VchostConnection`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VchostConnection`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VchostConnection`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VchostConnection`".format(key))
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
        if issubclass(VchostConnection, dict):
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
        if not isinstance(other, VchostConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
