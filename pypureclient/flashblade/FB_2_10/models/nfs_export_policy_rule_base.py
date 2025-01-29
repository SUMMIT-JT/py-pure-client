# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.10, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_10 import models

class NfsExportPolicyRuleBase(object):
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
        'access': 'str',
        'anongid': 'str',
        'anonuid': 'str',
        'atime': 'bool',
        'client': 'str',
        'fileid_32bit': 'bool',
        'policy': 'FixedReference',
        'policy_version': 'str',
        'permission': 'str',
        'secure': 'bool',
        'security': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'access': 'access',
        'anongid': 'anongid',
        'anonuid': 'anonuid',
        'atime': 'atime',
        'client': 'client',
        'fileid_32bit': 'fileid_32bit',
        'policy': 'policy',
        'policy_version': 'policy_version',
        'permission': 'permission',
        'secure': 'secure',
        'security': 'security'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        access=None,  # type: str
        anongid=None,  # type: str
        anonuid=None,  # type: str
        atime=None,  # type: bool
        client=None,  # type: str
        fileid_32bit=None,  # type: bool
        policy=None,  # type: models.FixedReference
        policy_version=None,  # type: str
        permission=None,  # type: str
        secure=None,  # type: bool
        security=None,  # type: List[str]
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            access (str): Specifies access control for the export. Valid values are `root-squash`, `all-squash`, and `no-squash`. `root-squash` prevents client users and groups with root privilege from mapping their root privilege to a file system. All users with UID 0 will have their UID mapped to anonuid. All users with GID 0 will have their GID mapped to anongid. `all-squash` maps all UIDs (including root) to anonuid and all GIDs (including root) to anongid. `no-squash` allows users and groups to access the file system with their UIDs and GIDs. The default is `root-squash` if not specified.
            anongid (str): Any user whose GID is affected by an `access` of `root_squash` or `all_squash` will have their GID mapped to `anongid`. The default `anongid` is null, which means 65534. Use \"\" to clear.
            anonuid (str): Any user whose UID is affected by an `access` of `root_squash` or `all_squash` will have their UID mapped to `anonuid`. The default `anonuid` is null, which means 65534. Use \"\" to clear.
            atime (bool): If `true`, after a read operation has occurred, the inode access time is updated only if any of the following conditions is true: the previous access time is less than the inode modify time, the previous access time is less than the inode change time, or the previous access time is more than 24 hours ago. If `false`, disables the update of inode access times after read operations. Defaults to `true`.
            client (str): Specifies the clients that will be permitted to access the export. Accepted notation is a single IP address, subnet in CIDR notation, netgroup, hostname (see RFC-1123 part 2.1), fully qualified domain name (see RFC-1123 part 2.1, RFC 2181 part 11), wildcards with fully qualified domain name or hostname, or anonymous (`*`). The default is `*` if not specified.
            fileid_32bit (bool): Whether the file id is 32 bits or not. Defaults to `false`.
            policy (FixedReference): The policy to which this rule belongs.
            policy_version (str): The policy's version. This can be used when updating the resource to ensure there aren't any updates to the policy since the resource was read.
            permission (str): Specifies which read-write client access permissions are allowed for the export. Valid values are `rw` and `ro`. The default is `ro` if not specified.
            secure (bool): If `true`, prevents NFS access to client connections coming from non-reserved ports. Applies to NFSv3, NFSv4.1, and auxiliary protocols MOUNT and NLM. If `false`, allows NFS access to client connections coming from non-reserved ports. Applies to NFSv3, NFSv4.1, and auxiliary protocols MOUNT and NLM. The default is `false` if not specified.
            security (list[str]): The security flavors to use for accessing files on this mount point.  If the server does not support the requested flavor, the mount operation fails. If `sys`, trusts the client to specify user's identity. If `krb5`, provides cryptographic proof of a user's identity in each RPC request. This provides  strong verification of the identity of users accessing data on the server. Note that additional configuration besides adding this mount option is required in order to enable Kerberos security. If `krb5i`, adds integrity checking to krb5, to ensure the data has not been tampered with. If `krb5p`, adds integrity checking and encryption to krb5. This is the most secure setting, but it also involves the most performance overhead. The default is `sys` if not specified.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if access is not None:
            self.access = access
        if anongid is not None:
            self.anongid = anongid
        if anonuid is not None:
            self.anonuid = anonuid
        if atime is not None:
            self.atime = atime
        if client is not None:
            self.client = client
        if fileid_32bit is not None:
            self.fileid_32bit = fileid_32bit
        if policy is not None:
            self.policy = policy
        if policy_version is not None:
            self.policy_version = policy_version
        if permission is not None:
            self.permission = permission
        if secure is not None:
            self.secure = secure
        if security is not None:
            self.security = security

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NfsExportPolicyRuleBase`".format(key))
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
        if issubclass(NfsExportPolicyRuleBase, dict):
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
        if not isinstance(other, NfsExportPolicyRuleBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
