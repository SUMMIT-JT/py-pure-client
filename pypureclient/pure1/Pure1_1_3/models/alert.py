# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_3 import models

class Alert(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'id': 'str',
        'name': 'str',
        'arrays': 'list[FixedReferenceFqdn]',
        'actual': 'str',
        'category': 'str',
        'closed': 'int',
        'code': 'int',
        'component_name': 'str',
        'component_type': 'str',
        'created': 'int',
        'description': 'str',
        'expected': 'str',
        'knowledge_base_url': 'str',
        'notified': 'int',
        'origin': 'str',
        'severity': 'str',
        'state': 'str',
        'summary': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'arrays': 'arrays',
        'actual': 'actual',
        'category': 'category',
        'closed': 'closed',
        'code': 'code',
        'component_name': 'component_name',
        'component_type': 'component_type',
        'created': 'created',
        'description': 'description',
        'expected': 'expected',
        'knowledge_base_url': 'knowledge_base_url',
        'notified': 'notified',
        'origin': 'origin',
        'severity': 'severity',
        'state': 'state',
        'summary': 'summary',
        'updated': 'updated'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        name=None,  # type: str
        arrays=None,  # type: List[models.FixedReferenceFqdn]
        actual=None,  # type: str
        category=None,  # type: str
        closed=None,  # type: int
        code=None,  # type: int
        component_name=None,  # type: str
        component_type=None,  # type: str
        created=None,  # type: int
        description=None,  # type: str
        expected=None,  # type: str
        knowledge_base_url=None,  # type: str
        notified=None,  # type: int
        origin=None,  # type: str
        severity=None,  # type: str
        state=None,  # type: str
        summary=None,  # type: str
        updated=None,  # type: int
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A modifiable, locally unique name chosen by the user.
            arrays (list[FixedReferenceFqdn]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays.
            actual (str): Actual condition at the time of the alert.
            category (str): Category of the alert. Valid values are `array`, `hardware`, and `software`.
            closed (int): Time when the alert was closed, in milliseconds since UNIX epoch.
            code (int): Code associated with the alert.
            component_name (str): Name of the component alerted about.
            component_type (str): Type of the component alerted about.
            created (int): Time when the alert was created, in milliseconds since UNIX epoch.
            description (str): Short description of the alert.
            expected (str): Expected state/threshold under normal conditions.
            knowledge_base_url (str): URL of the relevant Knowledge Base page.
            notified (int): Time when the user was notified of the alert, in milliseconds since UNIX epoch.
            origin (str): Origin of the alert. Valid values are `array` and `Pure1`.
            severity (str): Current severity level. Valid values are `info`, `warning`, `critical`, and `hidden`.
            state (str): Current state of the alert. Valid values are `open`, `closing`, and `closed`.
            summary (str): Summary of the alert.
            updated (int): Time when the alert was last updated, in milliseconds since UNIX epoch.
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if arrays is not None:
            self.arrays = arrays
        if actual is not None:
            self.actual = actual
        if category is not None:
            self.category = category
        if closed is not None:
            self.closed = closed
        if code is not None:
            self.code = code
        if component_name is not None:
            self.component_name = component_name
        if component_type is not None:
            self.component_type = component_type
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if expected is not None:
            self.expected = expected
        if knowledge_base_url is not None:
            self.knowledge_base_url = knowledge_base_url
        if notified is not None:
            self.notified = notified
        if origin is not None:
            self.origin = origin
        if severity is not None:
            self.severity = severity
        if state is not None:
            self.state = state
        if summary is not None:
            self.summary = summary
        if updated is not None:
            self.updated = updated

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
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
        if issubclass(Alert, dict):
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
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
