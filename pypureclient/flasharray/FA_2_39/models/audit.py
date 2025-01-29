# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.39
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_39 import models

class Audit(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'context': 'FixedReference',
        'arguments': 'str',
        'command': 'str',
        'subcommand': 'str',
        'time': 'int',
        'user': 'str',
        'origin': 'FixedReference',
        'user_interface': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'context': 'context',
        'arguments': 'arguments',
        'command': 'command',
        'subcommand': 'subcommand',
        'time': 'time',
        'user': 'user',
        'origin': 'origin',
        'user_interface': 'user_interface'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        context=None,  # type: models.FixedReference
        arguments=None,  # type: str
        command=None,  # type: str
        subcommand=None,  # type: str
        time=None,  # type: int
        user=None,  # type: str
        origin=None,  # type: models.FixedReference
        user_interface=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A locally unique, system-generated name. The name cannot be modified.
            context (FixedReference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request. Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`.
            arguments (str): The arguments provided to the command.
            command (str): The top level command that starts with the string \"pure\" as a convention.
            subcommand (str): The `command` and `subcommand` combination determines which action the user attempted to perform.
            time (int): The time at which the command was run in milliseconds since the UNIX epoch.
            user (str): The user who ran the command.
            origin (FixedReference): The array from which the command originated.
            user_interface (str): The user interface through which the user session event was performed. Valid values are `CLI`, `GUI`, and `REST`.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if context is not None:
            self.context = context
        if arguments is not None:
            self.arguments = arguments
        if command is not None:
            self.command = command
        if subcommand is not None:
            self.subcommand = subcommand
        if time is not None:
            self.time = time
        if user is not None:
            self.user = user
        if origin is not None:
            self.origin = origin
        if user_interface is not None:
            self.user_interface = user_interface

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Audit`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Audit`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Audit`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Audit`".format(key))
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
        if issubclass(Audit, dict):
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
        if not isinstance(other, Audit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
