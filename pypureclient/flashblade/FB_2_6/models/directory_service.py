# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.6, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_6 import models

class DirectoryService(object):
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
        'base_dn': 'str',
        'bind_password': 'str',
        'bind_user': 'str',
        'ca_certificate': 'Reference',
        'ca_certificate_group': 'Reference',
        'enabled': 'bool',
        'management': 'DirectoryServiceManagement',
        'nfs': 'DirectoryServiceNfs',
        'services': 'list[str]',
        'smb': 'DirectoryServiceSmb',
        'uris': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'base_dn': 'base_dn',
        'bind_password': 'bind_password',
        'bind_user': 'bind_user',
        'ca_certificate': 'ca_certificate',
        'ca_certificate_group': 'ca_certificate_group',
        'enabled': 'enabled',
        'management': 'management',
        'nfs': 'nfs',
        'services': 'services',
        'smb': 'smb',
        'uris': 'uris'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        base_dn=None,  # type: str
        bind_password=None,  # type: str
        bind_user=None,  # type: str
        ca_certificate=None,  # type: models.Reference
        ca_certificate_group=None,  # type: models.Reference
        enabled=None,  # type: bool
        management=None,  # type: models.DirectoryServiceManagement
        nfs=None,  # type: models.DirectoryServiceNfs
        services=None,  # type: List[str]
        smb=None,  # type: models.DirectoryServiceSmb
        uris=None,  # type: List[str]
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            base_dn (str): Base of the Distinguished Name (DN) of the directory service groups.
            bind_password (str): Obfuscated password used to query the directory.
            bind_user (str): Username used to query the directory.
            ca_certificate (Reference): CA certificate used to validate the authenticity of the configured servers.
            ca_certificate_group (Reference): A certificate group containing CA certificates that can be used to validate the authenticity of the configured servers.
            enabled (bool): Is the directory service enabled or not?
            management (DirectoryServiceManagement)
            nfs (DirectoryServiceNfs)
            services (list[str]): Services that the directory service configuration is used for.
            smb (DirectoryServiceSmb)
            uris (list[str]): List of URIs for the configured directory servers.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if base_dn is not None:
            self.base_dn = base_dn
        if bind_password is not None:
            self.bind_password = bind_password
        if bind_user is not None:
            self.bind_user = bind_user
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate
        if ca_certificate_group is not None:
            self.ca_certificate_group = ca_certificate_group
        if enabled is not None:
            self.enabled = enabled
        if management is not None:
            self.management = management
        if nfs is not None:
            self.nfs = nfs
        if services is not None:
            self.services = services
        if smb is not None:
            self.smb = smb
        if uris is not None:
            self.uris = uris

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryService`".format(key))
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
        if issubclass(DirectoryService, dict):
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
        if not isinstance(other, DirectoryService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
