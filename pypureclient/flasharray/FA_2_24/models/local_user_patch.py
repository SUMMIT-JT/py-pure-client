# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.24
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_24 import models

class LocalUserPatch(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'email': 'str',
        'name': 'str',
        'password': 'str',
        'primary_group': 'ReferenceWithType',
        'uid': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'email': 'email',
        'name': 'name',
        'password': 'password',
        'primary_group': 'primary_group',
        'uid': 'uid'
    }

    required_args = {
    }

    def __init__(
        self,
        enabled=None,  # type: bool
        email=None,  # type: str
        name=None,  # type: str
        password=None,  # type: str
        primary_group=None,  # type: models.ReferenceWithType
        uid=None,  # type: int
    ):
        """
        Keyword args:
            enabled (bool): If this field is `false`, the local user will be disabled on creation. Otherwise, the local user will be enabled and functional from the beginning.
            email (str): Optional field to set the email of the local user.
            name (str): The local user name.
            password (str): The password of the local user. This field is only required if the `enabled` field is true.
            primary_group (ReferenceWithType): Local group that would be assigned as the primary group of the local user.
            uid (int): Optional field to set the UID of the local user.
        """
        if enabled is not None:
            self.enabled = enabled
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if primary_group is not None:
            self.primary_group = primary_group
        if uid is not None:
            self.uid = uid

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalUserPatch`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalUserPatch`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalUserPatch`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalUserPatch`".format(key))
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
        if issubclass(LocalUserPatch, dict):
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
        if not isinstance(other, LocalUserPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
