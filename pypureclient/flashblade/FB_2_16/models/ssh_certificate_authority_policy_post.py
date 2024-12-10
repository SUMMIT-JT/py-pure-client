# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.16, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_16 import models

class SshCertificateAuthorityPolicyPost(object):
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
        'enabled': 'bool',
        'is_local': 'bool',
        'location': 'FixedReference',
        'policy_type': 'str',
        'signing_authority': 'ReferenceWritable',
        'static_authorized_principals': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'enabled': 'enabled',
        'is_local': 'is_local',
        'location': 'location',
        'policy_type': 'policy_type',
        'signing_authority': 'signing_authority',
        'static_authorized_principals': 'static_authorized_principals'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        enabled=None,  # type: bool
        is_local=None,  # type: bool
        location=None,  # type: models.FixedReference
        policy_type=None,  # type: str
        signing_authority=None,  # type: models.ReferenceWritable
        static_authorized_principals=None,  # type: List[str]
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            enabled (bool): If `true`, the policy is enabled. If not specified, defaults to `true`.
            is_local (bool): Whether the policy is defined on the local array.
            location (FixedReference): Reference to the array where the policy is defined.
            policy_type (str): Type of the policy. Valid values include `alert`, `audit`, `bucket-access`, `cross-origin-resource-sharing`, `network-access`, `nfs`, `object-access`, `smb-client`, `smb-share`, `snapshot`, `ssh-certificate-authority`, and `worm-data`.
            signing_authority (ReferenceWritable): A reference to the authority that will digitally sign user SSH certificates that will be used to access the system. This may be either a certificate or a public key. If a certificate is used as the signer, then its expiry period will be honored and user SSH certificates signed by the certificate will no longer be accepted after the certificate has expired.
            static_authorized_principals (list[str]): If not specified - users affected by this policy can only log into the system when they present an SSH certificate containing their own username as a principle. If specified - users affected by this policy can only log into the system when they present an SSH certificate containing at least one username from this list as a principle.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if enabled is not None:
            self.enabled = enabled
        if is_local is not None:
            self.is_local = is_local
        if location is not None:
            self.location = location
        if policy_type is not None:
            self.policy_type = policy_type
        if signing_authority is not None:
            self.signing_authority = signing_authority
        if static_authorized_principals is not None:
            self.static_authorized_principals = static_authorized_principals

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SshCertificateAuthorityPolicyPost`".format(key))
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
        if issubclass(SshCertificateAuthorityPolicyPost, dict):
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
        if not isinstance(other, SshCertificateAuthorityPolicyPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
