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

class LocalUser(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'built_in': 'bool',
        'enabled': 'bool',
        'email': 'str',
        'name': 'str',
        'primary_group': 'ReferenceWithType',
        'sid': 'str',
        'uid': 'int'
    }

    attribute_map = {
        'built_in': 'built_in',
        'enabled': 'enabled',
        'email': 'email',
        'name': 'name',
        'primary_group': 'primary_group',
        'sid': 'sid',
        'uid': 'uid'
    }

    required_args = {
    }

    def __init__(
        self,
        built_in=None,  # type: bool
        enabled=None,  # type: bool
        email=None,  # type: str
        name=None,  # type: str
        primary_group=None,  # type: models.ReferenceWithType
        sid=None,  # type: str
        uid=None,  # type: int
    ):
        """
        Keyword args:
            built_in (bool): Returns a value of `true` if the local user is built in. Otherwise returns a value of `false` if the user has been created manually.
            enabled (bool): Returns a value of `true` if the local user is enabled.
            email (str): The email address of the local user.
            name (str): The name of the local user.
            primary_group (ReferenceWithType): Primary group of the local user.
            sid (str): The SID (security ID) of the local user.
            uid (int): The POSIX user ID of this object (user ID).
        """
        if built_in is not None:
            self.built_in = built_in
        if enabled is not None:
            self.enabled = enabled
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if primary_group is not None:
            self.primary_group = primary_group
        if sid is not None:
            self.sid = sid
        if uid is not None:
            self.uid = uid

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalUser`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalUser`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalUser`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `LocalUser`".format(key))
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
        if issubclass(LocalUser, dict):
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
        if not isinstance(other, LocalUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
