# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.13, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_13 import models

class BucketPatch(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'destroyed': 'bool',
        'hard_limit_enabled': 'bool',
        'object_lock_config': 'ObjectLockConfigRequestBody',
        'quota_limit': 'str',
        'retention_lock': 'str',
        'versioning': 'str',
        'public_access_config': 'PublicAccessConfig',
        'eradication_config': 'BucketEradicationConfig'
    }

    attribute_map = {
        'destroyed': 'destroyed',
        'hard_limit_enabled': 'hard_limit_enabled',
        'object_lock_config': 'object_lock_config',
        'quota_limit': 'quota_limit',
        'retention_lock': 'retention_lock',
        'versioning': 'versioning',
        'public_access_config': 'public_access_config',
        'eradication_config': 'eradication_config'
    }

    required_args = {
    }

    def __init__(
        self,
        destroyed=None,  # type: bool
        hard_limit_enabled=None,  # type: bool
        object_lock_config=None,  # type: models.ObjectLockConfigRequestBody
        quota_limit=None,  # type: str
        retention_lock=None,  # type: str
        versioning=None,  # type: str
        public_access_config=None,  # type: models.PublicAccessConfig
        eradication_config=None,  # type: models.BucketEradicationConfig
    ):
        """
        Keyword args:
            destroyed (bool): Is the bucket destroyed?
            hard_limit_enabled (bool): If set to `true`, the bucket's size, as defined by `quota_limit`, is used as a hard limit quota. If set to `false`, a hard limit quota will not be applied to the bucket, but soft quota alerts will still be sent if the bucket has a value set for `quota_limit`.
            object_lock_config (ObjectLockConfigRequestBody)
            quota_limit (str): The effective quota limit applied against the size of the bucket, displayed in bytes. If set to an empty string (`\"\"`), the bucket is unlimited in size.
            retention_lock (str): If set to `ratcheted`, then `object_lock_config.default_retention_mode` cannot be changed if set to `compliance`. In this case, the value of `object_lock_config.default_retention` can only be increased and `object_lock_config.default_retention_mode` cannot be changed once set to `compliance`. Valid values are `unlocked` and `ratcheted`. Contact Pure Technical Services to change `ratcheted` to `unlocked`.
            versioning (str): The versioning state for objects within the bucket. Valid values are `none`, `enabled`, and `suspended`.
            public_access_config (PublicAccessConfig)
            eradication_config (BucketEradicationConfig)
        """
        if destroyed is not None:
            self.destroyed = destroyed
        if hard_limit_enabled is not None:
            self.hard_limit_enabled = hard_limit_enabled
        if object_lock_config is not None:
            self.object_lock_config = object_lock_config
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if retention_lock is not None:
            self.retention_lock = retention_lock
        if versioning is not None:
            self.versioning = versioning
        if public_access_config is not None:
            self.public_access_config = public_access_config
        if eradication_config is not None:
            self.eradication_config = eradication_config

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `BucketPatch`".format(key))
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
        if issubclass(BucketPatch, dict):
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
        if not isinstance(other, BucketPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
