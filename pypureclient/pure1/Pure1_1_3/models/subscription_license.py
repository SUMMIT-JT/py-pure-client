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

class SubscriptionLicense(object):
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
        'average_on_demand': 'CurrentMetric',
        'expiration_date': 'int',
        'marketplace_partner': 'MarketplacePartner',
        'reservation': 'CurrentMetric',
        'resources': 'list[LicenseResourceReference]',
        'service_tier': 'str',
        'start_date': 'int',
        'subscription': 'FixedReference',
        'usage': 'CurrentMetric',
        'last_updated_date': 'int',
        'pre_ratio': 'object',
        'quarter_on_demand': 'CurrentMetric',
        'site_address': 'BaseAddress'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'average_on_demand': 'average_on_demand',
        'expiration_date': 'expiration_date',
        'marketplace_partner': 'marketplace_partner',
        'reservation': 'reservation',
        'resources': 'resources',
        'service_tier': 'service_tier',
        'start_date': 'start_date',
        'subscription': 'subscription',
        'usage': 'usage',
        'last_updated_date': 'last_updated_date',
        'pre_ratio': 'pre_ratio',
        'quarter_on_demand': 'quarter_on_demand',
        'site_address': 'site_address'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        name=None,  # type: str
        average_on_demand=None,  # type: models.CurrentMetric
        expiration_date=None,  # type: int
        marketplace_partner=None,  # type: models.MarketplacePartner
        reservation=None,  # type: models.CurrentMetric
        resources=None,  # type: List[models.LicenseResourceReference]
        service_tier=None,  # type: str
        start_date=None,  # type: int
        subscription=None,  # type: models.FixedReference
        usage=None,  # type: models.CurrentMetric
        last_updated_date=None,  # type: int
        pre_ratio=None,  # type: object
        quarter_on_demand=None,  # type: models.CurrentMetric
        site_address=None,  # type: models.BaseAddress
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A non-modifiable, locally unique name chosen by the system.
            average_on_demand (CurrentMetric): Estimated daily on-demand usage of the license from the current calendar quarter to date.
            expiration_date (int): Date when the license expires. Represented as a timestamp of 00:00 on that date in UTC, in milliseconds since UNIX epoch.
            marketplace_partner (MarketplacePartner): Reference information about the marketplace partner of this license.
            reservation (CurrentMetric): Current reservation amount of the license.
            resources (list[LicenseResourceReference])
            service_tier (str): The tier of the service for the license.
            start_date (int): Date when the license starts. Represented as a timestamp of 00:00 on that date in UTC, in milliseconds since UNIX epoch.
            subscription (FixedReference): A reference to which subscription this license belongs.
            usage (CurrentMetric): Usage of the license, averaged over the last day.
            last_updated_date (int): The date of the last amendment to the current license. Represented as a timestamp of 00:00 on that date in UTC, in milliseconds since UNIX epoch.
            pre_ratio (object): The pre-reduced & encrypted ratio calculated at license level.
            quarter_on_demand (CurrentMetric): Estimated total on-demand usage of the license of the current calendar quarter to date.
            site_address (BaseAddress): The license site address.
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if average_on_demand is not None:
            self.average_on_demand = average_on_demand
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if marketplace_partner is not None:
            self.marketplace_partner = marketplace_partner
        if reservation is not None:
            self.reservation = reservation
        if resources is not None:
            self.resources = resources
        if service_tier is not None:
            self.service_tier = service_tier
        if start_date is not None:
            self.start_date = start_date
        if subscription is not None:
            self.subscription = subscription
        if usage is not None:
            self.usage = usage
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if pre_ratio is not None:
            self.pre_ratio = pre_ratio
        if quarter_on_demand is not None:
            self.quarter_on_demand = quarter_on_demand
        if site_address is not None:
            self.site_address = site_address

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SubscriptionLicense`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SubscriptionLicense`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SubscriptionLicense`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SubscriptionLicense`".format(key))
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
        if issubclass(SubscriptionLicense, dict):
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
        if not isinstance(other, SubscriptionLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
