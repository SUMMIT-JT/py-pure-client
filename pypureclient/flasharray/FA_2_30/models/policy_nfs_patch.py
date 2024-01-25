# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.30
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_30 import models

class PolicyNfsPatch(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'enabled': 'bool',
        'user_mapping_enabled': 'bool',
        'nfs_version': 'list[str]',
        'security': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'enabled': 'enabled',
        'user_mapping_enabled': 'user_mapping_enabled',
        'nfs_version': 'nfs_version',
        'security': 'security'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        enabled=None,  # type: bool
        user_mapping_enabled=None,  # type: bool
        nfs_version=None,  # type: List[str]
        security=None,  # type: List[str]
    ):
        """
        Keyword args:
            name (str): The new name for the resource.
            enabled (bool): If set to `true`, enables the policy. If set to `false`, disables the policy.
            user_mapping_enabled (bool): If set to `true`, FlashArray queries the joined AD/OpenLDAP server to find the user corresponding to the incoming UID. If set to `false`, users are defined by UID/GID pair.
            nfs_version (list[str]): NFS protocol version allowed for the export to set for the policy. This operation updates all rules of the specified policy. Valid values are `nfsv3` and `nfsv4`.
            security (list[str]): The security flavors to use for accessing files on this mount point. Values include `auth_sys`, `krb5`, `krb5i`, and `krb5p`. If the server does not support the requested flavor, the mount operation fails. This operation updates all rules of the specified policy. If `auth_sys`, the client is trusted to specify the identity of the user. If `krb5`, cryptographic proof of the identity of the user is provided in each RPC request. This provides strong verification of the identity of users accessing data on the server. Note that additional configuration besides adding this mount option is required to enable Kerberos security. If `krb5i`, integrity checking is added to krb5. This ensures the data has not been tampered with. If `krb5p`, integrity checking and encryption is added to `krb5`. This is the most secure setting, but it also involves the most performance overhead.
        """
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if user_mapping_enabled is not None:
            self.user_mapping_enabled = user_mapping_enabled
        if nfs_version is not None:
            self.nfs_version = nfs_version
        if security is not None:
            self.security = security

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyNfsPatch`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyNfsPatch`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyNfsPatch`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyNfsPatch`".format(key))
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
        if issubclass(PolicyNfsPatch, dict):
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
        if not isinstance(other, PolicyNfsPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
