# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_40 import models

class PolicyPassword(object):
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
        'policy_type': 'str',
        'enabled': 'bool',
        'lockout_duration': 'int',
        'max_login_attempts': 'int',
        'min_password_length': 'int',
        'password_history': 'int',
        'min_password_age': 'int',
        'min_character_groups': 'int',
        'min_characters_per_group': 'int',
        'enforce_username_check': 'bool',
        'enforce_dictionary_check': 'bool',
        'max_password_age': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'context': 'context',
        'policy_type': 'policy_type',
        'enabled': 'enabled',
        'lockout_duration': 'lockout_duration',
        'max_login_attempts': 'max_login_attempts',
        'min_password_length': 'min_password_length',
        'password_history': 'password_history',
        'min_password_age': 'min_password_age',
        'min_character_groups': 'min_character_groups',
        'min_characters_per_group': 'min_characters_per_group',
        'enforce_username_check': 'enforce_username_check',
        'enforce_dictionary_check': 'enforce_dictionary_check',
        'max_password_age': 'max_password_age'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        context=None,  # type: models.FixedReference
        policy_type=None,  # type: str
        enabled=None,  # type: bool
        lockout_duration=None,  # type: int
        max_login_attempts=None,  # type: int
        min_password_length=None,  # type: int
        password_history=None,  # type: int
        min_password_age=None,  # type: int
        min_character_groups=None,  # type: int
        min_characters_per_group=None,  # type: int
        enforce_username_check=None,  # type: bool
        enforce_dictionary_check=None,  # type: bool
        max_password_age=None,  # type: int
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            context (FixedReference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request. Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`.
            policy_type (str): The type of policy. Valid values include `autodir`, `nfs`, `password`, `smb`, `snapshot`, and `quota`.
            enabled (bool): Returns a value of `true` if the policy is enabled.
            lockout_duration (int): The lockout duration, in milliseconds, if a user is locked out after reaching the maximum number of login attempts. Ranges from 1 second to 90 days.
            max_login_attempts (int): Maximum number of failed login attempts allowed before the user is locked out.
            min_password_length (int): Minimum password length. If not specified, defaults to 1.
            password_history (int): The number of passwords tracked to prevent reuse of passwords.
            min_password_age (int): The minimum age, in milliseconds, of password before password change is allowed. Ranges from 0 ms to 7 days
            min_character_groups (int): The minimum number of character groups ([a-z], [A-Z], [0-9], other) required to be present in a password.
            min_characters_per_group (int): The minimum number of characters per group to count the group as present. Maximum is limited by the minimum password length divided by the number of character groups (e.g. min_password_length = 9, min_character_groups = 4, then maximum is 2).
            enforce_username_check (bool): If `true`, the username cannot be a substring of the password. It only applies to usernames of 3 characters and longer.
            enforce_dictionary_check (bool): If `true`, test password against dictionary of known leaked passwords. Only applies to passwords longer than 6 characters.
            max_password_age (int): The maximum age of password before password change is required. Ranges from 1 day to 99999 days, with 0 meaning password expiration is disabled.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if context is not None:
            self.context = context
        if policy_type is not None:
            self.policy_type = policy_type
        if enabled is not None:
            self.enabled = enabled
        if lockout_duration is not None:
            self.lockout_duration = lockout_duration
        if max_login_attempts is not None:
            self.max_login_attempts = max_login_attempts
        if min_password_length is not None:
            self.min_password_length = min_password_length
        if password_history is not None:
            self.password_history = password_history
        if min_password_age is not None:
            self.min_password_age = min_password_age
        if min_character_groups is not None:
            self.min_character_groups = min_character_groups
        if min_characters_per_group is not None:
            self.min_characters_per_group = min_characters_per_group
        if enforce_username_check is not None:
            self.enforce_username_check = enforce_username_check
        if enforce_dictionary_check is not None:
            self.enforce_dictionary_check = enforce_dictionary_check
        if max_password_age is not None:
            self.max_password_age = max_password_age

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyPassword`".format(key))
        if key == "lockout_duration" and value is not None:
            if value > 7776000000:
                raise ValueError("Invalid value for `lockout_duration`, value must be less than or equal to `7776000000`")
            if value < 1000:
                raise ValueError("Invalid value for `lockout_duration`, must be a value greater than or equal to `1000`")
        if key == "max_login_attempts" and value is not None:
            if value > 100:
                raise ValueError("Invalid value for `max_login_attempts`, value must be less than or equal to `100`")
            if value < 1:
                raise ValueError("Invalid value for `max_login_attempts`, must be a value greater than or equal to `1`")
        if key == "min_password_length" and value is not None:
            if value > 100:
                raise ValueError("Invalid value for `min_password_length`, value must be less than or equal to `100`")
            if value < 1:
                raise ValueError("Invalid value for `min_password_length`, must be a value greater than or equal to `1`")
        if key == "password_history" and value is not None:
            if value > 64:
                raise ValueError("Invalid value for `password_history`, value must be less than or equal to `64`")
            if value < 0:
                raise ValueError("Invalid value for `password_history`, must be a value greater than or equal to `0`")
        if key == "min_password_age" and value is not None:
            if value > 604800000:
                raise ValueError("Invalid value for `min_password_age`, value must be less than or equal to `604800000`")
            if value < 0:
                raise ValueError("Invalid value for `min_password_age`, must be a value greater than or equal to `0`")
        if key == "min_character_groups" and value is not None:
            if value > 4:
                raise ValueError("Invalid value for `min_character_groups`, value must be less than or equal to `4`")
            if value < 0:
                raise ValueError("Invalid value for `min_character_groups`, must be a value greater than or equal to `0`")
        if key == "min_characters_per_group" and value is not None:
            if value < 1:
                raise ValueError("Invalid value for `min_characters_per_group`, must be a value greater than or equal to `1`")
        if key == "max_password_age" and value is not None:
            if value > 8639913600000:
                raise ValueError("Invalid value for `max_password_age`, value must be less than or equal to `8639913600000`")
            if value < 0:
                raise ValueError("Invalid value for `max_password_age`, must be a value greater than or equal to `0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyPassword`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyPassword`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyPassword`".format(key))
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
        if issubclass(PolicyPassword, dict):
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
        if not isinstance(other, PolicyPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
