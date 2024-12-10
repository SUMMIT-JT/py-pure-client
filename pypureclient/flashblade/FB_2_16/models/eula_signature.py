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

class EulaSignature(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'accepted': 'int',
        'name': 'str',
        'title': 'str',
        'company': 'str'
    }

    attribute_map = {
        'accepted': 'accepted',
        'name': 'name',
        'title': 'title',
        'company': 'company'
    }

    required_args = {
    }

    def __init__(
        self,
        accepted=None,  # type: int
        name=None,  # type: str
        title=None,  # type: str
        company=None,  # type: str
    ):
        """
        Keyword args:
            accepted (int): Accepted time in milliseconds since the UNIX epoch.
            name (str): Name of the person who accepted the End User Agreement. This field is deprecated and the response will be `null`. Modification to this field will be ignored.
            title (str): Title of the person who accepted the End User Agreement. This field is deprecated and the response will be `null`. Modification to this field will be ignored.
            company (str): Company of the person who accepted the End User Agreement. This field is deprecated and the response will be `null`. Modification to this field will be ignored.
        """
        if accepted is not None:
            self.accepted = accepted
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if company is not None:
            self.company = company

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `EulaSignature`".format(key))
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
        if issubclass(EulaSignature, dict):
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
        if not isinstance(other, EulaSignature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
