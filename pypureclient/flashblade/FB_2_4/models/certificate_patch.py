# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.4, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_4 import models

class CertificatePatch(object):
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
        'certificate': 'str',
        'intermediate_certificate': 'str',
        'passphrase': 'str',
        'private_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'certificate': 'certificate',
        'intermediate_certificate': 'intermediate_certificate',
        'passphrase': 'passphrase',
        'private_key': 'private_key'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        certificate=None,  # type: str
        intermediate_certificate=None,  # type: str
        passphrase=None,  # type: str
        private_key=None,  # type: str
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            certificate (str): The text of the certificate.
            intermediate_certificate (str): Intermediate certificate chains.
            passphrase (str): The passphrase used to encrypt `private_key`.
            private_key (str): The private key used to sign the certificate.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if certificate is not None:
            self.certificate = certificate
        if intermediate_certificate is not None:
            self.intermediate_certificate = intermediate_certificate
        if passphrase is not None:
            self.passphrase = passphrase
        if private_key is not None:
            self.private_key = private_key

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `CertificatePatch`".format(key))
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
        if issubclass(CertificatePatch, dict):
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
        if not isinstance(other, CertificatePatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
