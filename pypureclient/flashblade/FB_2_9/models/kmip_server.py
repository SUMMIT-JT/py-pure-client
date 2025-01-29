# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.9, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_9 import models

class KmipServer(object):
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
        'uris': 'list[str]',
        'ca_certificate': 'Reference',
        'ca_certificate_group': 'Reference'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'uris': 'uris',
        'ca_certificate': 'ca_certificate',
        'ca_certificate_group': 'ca_certificate_group'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        uris=None,  # type: List[str]
        ca_certificate=None,  # type: models.Reference
        ca_certificate_group=None,  # type: models.Reference
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            uris (list[str]): List of URIs for the configured KMIP servers in the format [protocol://]hostname:port.
            ca_certificate (Reference): CA certificate used to validate the authenticity of the configured servers.
            ca_certificate_group (Reference): A certificate group containing CA certificates that can be used to validate the authenticity of the configured servers.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if uris is not None:
            self.uris = uris
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate
        if ca_certificate_group is not None:
            self.ca_certificate_group = ca_certificate_group

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `KmipServer`".format(key))
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
        if issubclass(KmipServer, dict):
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
        if not isinstance(other, KmipServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
