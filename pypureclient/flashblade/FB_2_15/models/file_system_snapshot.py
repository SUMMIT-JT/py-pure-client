# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.15, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_15 import models

class FileSystemSnapshot(object):
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
        'created': 'int',
        'destroyed': 'bool',
        'owner': 'FixedReference',
        'owner_destroyed': 'bool',
        'policy': 'FixedLocationReference',
        'policies': 'list[FixedLocationReference]',
        'source': 'FixedLocationReference',
        'suffix': 'str',
        'time_remaining': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'created': 'created',
        'destroyed': 'destroyed',
        'owner': 'owner',
        'owner_destroyed': 'owner_destroyed',
        'policy': 'policy',
        'policies': 'policies',
        'source': 'source',
        'suffix': 'suffix',
        'time_remaining': 'time_remaining'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        created=None,  # type: int
        destroyed=None,  # type: bool
        owner=None,  # type: models.FixedReference
        owner_destroyed=None,  # type: bool
        policy=None,  # type: models.FixedLocationReference
        policies=None,  # type: List[models.FixedLocationReference]
        source=None,  # type: models.FixedLocationReference
        suffix=None,  # type: str
        time_remaining=None,  # type: int
    ):
        """
        Keyword args:
            name (str): A name chosen by the user. Can be changed. Must be locally unique.
            id (str): A non-modifiable, globally unique ID chosen by the system.
            created (int): Creation timestamp of the object.
            destroyed (bool): Is the file system snapshot destroyed? If not specified, defaults to `false`.
            owner (FixedReference): A reference to the file system that owns this snapshot. If the owner is destroyed, this will be destroyed.
            owner_destroyed (bool): Is the owning file system destroyed?
            policy (FixedLocationReference): A reference to the associated policy that drives the behavior of the snapshot.
            policies (list[FixedLocationReference]): An array of references to the associated policies.
            source (FixedLocationReference): A reference to the file system that was the source of the data in this snapshot. Normally this is the same as the owner, but if the snapshot is replicated, the source is the original file system.
            suffix (str): The suffix of the snapshot, e.g., `snap1`.
            time_remaining (int): Time in milliseconds before the file system snapshot is eradicated. `null` if not destroyed.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if owner is not None:
            self.owner = owner
        if owner_destroyed is not None:
            self.owner_destroyed = owner_destroyed
        if policy is not None:
            self.policy = policy
        if policies is not None:
            self.policies = policies
        if source is not None:
            self.source = source
        if suffix is not None:
            self.suffix = suffix
        if time_remaining is not None:
            self.time_remaining = time_remaining

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FileSystemSnapshot`".format(key))
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
        if issubclass(FileSystemSnapshot, dict):
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
        if not isinstance(other, FileSystemSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
