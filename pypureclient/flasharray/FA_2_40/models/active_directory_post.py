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

class ActiveDirectoryPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'computer_name': 'str',
        'directory_servers': 'list[str]',
        'domain': 'str',
        'kerberos_servers': 'list[str]',
        'password': 'str',
        'user': 'str',
        'join_ou': 'str',
        'tls': 'str'
    }

    attribute_map = {
        'computer_name': 'computer_name',
        'directory_servers': 'directory_servers',
        'domain': 'domain',
        'kerberos_servers': 'kerberos_servers',
        'password': 'password',
        'user': 'user',
        'join_ou': 'join_ou',
        'tls': 'tls'
    }

    required_args = {
    }

    def __init__(
        self,
        computer_name=None,  # type: str
        directory_servers=None,  # type: List[str]
        domain=None,  # type: str
        kerberos_servers=None,  # type: List[str]
        password=None,  # type: str
        user=None,  # type: str
        join_ou=None,  # type: str
        tls=None,  # type: str
    ):
        """
        Keyword args:
            computer_name (str): The name of the computer account to be created in the Active Directory domain. If not specified, defaults to the name of the Active Directory configuration.
            directory_servers (list[str]): A list of directory servers used for lookups related to user authorization. Servers must be specified in FQDN format. All specified servers must be registered to the domain appropriately in the configured DNS of the array and are only communicated with over the secure LDAP (LDAPS) protocol. If not specified, servers are resolved for the domain in DNS.
            domain (str): The Active Directory domain to join.
            kerberos_servers (list[str]): A list of key distribution servers to use for Kerberos protocol. Servers must be specified in FQDN format. All specified servers must be registered to the domain appropriately in the configured DNS of the array. If not specified, servers are resolved for the domain in DNS.
            password (str): The login password of the user with privileges to create the computer account in the domain. This is not persisted on the array.
            user (str): The login name of the user with privileges to create the computer account in the domain. This is not persisted on the array.
            join_ou (str): The distinguished name of the organizational unit in which the computer account should be created when joining the domain. The `DC=...` components of the distinguished name can be optionally omitted. If not specified, defaults to `CN=Computers`.
            tls (str): TLS mode for communication with domain controllers. Valid values are `required` and `optional`. `required` forces TLS communication with a domain controller. `optional` allows the use of non-TLS communication, TLS will still be preferred, if available. If not specified, defaults to `required`.
        """
        if computer_name is not None:
            self.computer_name = computer_name
        if directory_servers is not None:
            self.directory_servers = directory_servers
        if domain is not None:
            self.domain = domain
        if kerberos_servers is not None:
            self.kerberos_servers = kerberos_servers
        if password is not None:
            self.password = password
        if user is not None:
            self.user = user
        if join_ou is not None:
            self.join_ou = join_ou
        if tls is not None:
            self.tls = tls

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectoryPost`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectoryPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectoryPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ActiveDirectoryPost`".format(key))
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
        if issubclass(ActiveDirectoryPost, dict):
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
        if not isinstance(other, ActiveDirectoryPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
