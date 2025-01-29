# coding: utf-8

"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](https://www.purestorage.com)  The Pure1 REST API 2.0 offers one single form of authentication: OAuth 2.0 via the [Token Exchange protocol](https://datatracker.ietf.org/doc/draft-ietf-oauth-token-exchange).  OAuth 2.0 is an open protocol to allow secure authorization in a simple and standard method from web, mobile, desktop and background applications.  Note that the [Authentication](#section/Authentication) section below mentions 'API Key' as the security scheme type. This is solely for the purpose of allowing testing this API with [Swagger UI](https://static.pure1.purestorage.com/api-swagger/index.html).  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)

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

class InvoiceLine(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'item': 'str',
        'quantity': 'int',
        'description': 'str',
        'start_date': 'int',
        'end_date': 'int',
        'components': 'list[InvoiceLineComponent]',
        'unit_price': 'float',
        'amount': 'float',
        'tax': 'Tax'
    }

    attribute_map = {
        'item': 'item',
        'quantity': 'quantity',
        'description': 'description',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'components': 'components',
        'unit_price': 'unit_price',
        'amount': 'amount',
        'tax': 'tax'
    }

    required_args = {
    }

    def __init__(
        self,
        item=None,  # type: str
        quantity=None,  # type: int
        description=None,  # type: str
        start_date=None,  # type: int
        end_date=None,  # type: int
        components=None,  # type: List[models.InvoiceLineComponent]
        unit_price=None,  # type: float
        amount=None,  # type: float
        tax=None,  # type: models.Tax
    ):
        """
        Keyword args:
            item (str): The name of invoice item.
            quantity (int): The quantity of current invoice item.
            description (str)
            start_date (int): The invoice item start date. Represented as a timestamp of 00:00 on that date in UTC, in milliseconds since UNIX epoch.
            end_date (int): The invoice item end date. Represented as a timestamp of 00:00 on that date in UTC, in milliseconds since UNIX epoch.
            components (list[InvoiceLineComponent]): The sub-components of current invoice item.
            unit_price (float): The unit price of current invoice item, currency is specified in invoice currency.
            amount (float): The total price of current invoice item, currency is specified in invoice currency.
            tax (Tax)
        """
        if item is not None:
            self.item = item
        if quantity is not None:
            self.quantity = quantity
        if description is not None:
            self.description = description
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if components is not None:
            self.components = components
        if unit_price is not None:
            self.unit_price = unit_price
        if amount is not None:
            self.amount = amount
        if tax is not None:
            self.tax = tax

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `InvoiceLine`".format(key))
        if key == "quantity" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `InvoiceLine`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `InvoiceLine`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `InvoiceLine`".format(key))
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
        if issubclass(InvoiceLine, dict):
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
        if not isinstance(other, InvoiceLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
