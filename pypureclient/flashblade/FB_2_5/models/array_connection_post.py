# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.5, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_5 import models

class ArrayConnectionPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'ca_certificate_group': 'FixedReference',
        'encrypted': 'bool',
        'management_address': 'str',
        'remote': 'FixedReferenceNoResourceType',
        'replication_addresses': 'list[str]',
        'status': 'str',
        'version': 'str',
        'throttle': 'Throttle',
        'connection_key': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ca_certificate_group': 'ca_certificate_group',
        'encrypted': 'encrypted',
        'management_address': 'management_address',
        'remote': 'remote',
        'replication_addresses': 'replication_addresses',
        'status': 'status',
        'version': 'version',
        'throttle': 'throttle',
        'connection_key': 'connection_key'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        ca_certificate_group=None,  # type: models.FixedReference
        encrypted=None,  # type: bool
        management_address=None,  # type: str
        remote=None,  # type: models.FixedReferenceNoResourceType
        replication_addresses=None,  # type: List[str]
        status=None,  # type: str
        version=None,  # type: str
        throttle=None,  # type: models.Throttle
        connection_key=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A non-modifiable, globally unique ID chosen by the system.
            ca_certificate_group (FixedReference): The group of CA certificates that can be used, in addition to well-known Certificate Authority certificates, in order to establish a secure connection to the target array. Defaults to a reference to the `_default_replication_certs` group if `secure_connection` is `true`, or `null` otherwise.
            encrypted (bool): If this is set to `true`, then all customer data replicated over the connection will be sent over an encrypted connection using TLS, or will not be sent if a secure connection cannot be established. If this is set to `false`, then all customer data replicated over the connection will be sent over an unencrypted connection. Defaults to `false`.
            management_address (str): Management address of the target array. Settable on POST only.
            remote (FixedReferenceNoResourceType): The remote array.
            replication_addresses (list[str]): IP addresses and/or FQDNs of the target arrays. Settable on POST only. If not set on POST, will be set to all the replication addresses available on the target array at the time of the POST.
            status (str): Status of the connection. Valid values are `connected`, `partially_connected`, `connecting`, and `incompatible`. `connected` - The connection is OK. `partially_connected` - Some replication addresses are working, but others are not. `connecting` - No connection exists and the array is trying to reconnect. `incompatible` - The target array is not compatible.
            version (str): The version of the target array.
            throttle (Throttle)
            connection_key (str): The connection key of the target array. Settable on POST only.
        """
        if id is not None:
            self.id = id
        if ca_certificate_group is not None:
            self.ca_certificate_group = ca_certificate_group
        if encrypted is not None:
            self.encrypted = encrypted
        if management_address is not None:
            self.management_address = management_address
        if remote is not None:
            self.remote = remote
        if replication_addresses is not None:
            self.replication_addresses = replication_addresses
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if throttle is not None:
            self.throttle = throttle
        if connection_key is not None:
            self.connection_key = connection_key

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnectionPost`".format(key))
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
        if issubclass(ArrayConnectionPost, dict):
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
        if not isinstance(other, ArrayConnectionPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
