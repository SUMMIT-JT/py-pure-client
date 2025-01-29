# coding: utf-8

"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](https://www.purestorage.com)  The Pure1 REST API 2.0 offers one single form of authentication: OAuth 2.0 via the [Token Exchange protocol](https://datatracker.ietf.org/doc/draft-ietf-oauth-token-exchange).  OAuth 2.0 is an open protocol to allow secure authorization in a simple and standard method from web, mobile, desktop and background applications.  Note that the [Authentication](#section/Authentication) section below mentions 'API Key' as the security scheme type. This is solely for the purpose of allowing testing this API with [Swagger UI](https://static.pure1.purestorage.com/api-swagger/index.html).  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_2 import models

class PodReplicaLink(object):
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
        'lag': 'int',
        'paused': 'bool',
        'recovery_point': 'int',
        'status': 'str',
        'members': 'list[ResourceWithLocations]',
        'sources': 'list[ResourceWithLocations]',
        'targets': 'list[ResourceWithLocations]'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'lag': 'lag',
        'paused': 'paused',
        'recovery_point': 'recovery_point',
        'status': 'status',
        'members': 'members',
        'sources': 'sources',
        'targets': 'targets'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        lag=None,  # type: int
        paused=None,  # type: bool
        recovery_point=None,  # type: int
        status=None,  # type: str
        members=None,  # type: List[models.ResourceWithLocations]
        sources=None,  # type: List[models.ResourceWithLocations]
        targets=None,  # type: List[models.ResourceWithLocations]
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            lag (int): Duration, in milliseconds, which represents how far behind the replication `target` is from the `source`.
            paused (bool): Returns `true` if the replica link is paused.
            recovery_point (int): Time when the last piece of data was replicated, in milliseconds since the UNIX epoch, and the recovery point if the target pod is promoted. If the pod is currently baselining then the value is `null`.
            status (str): Status of the replica link. Values include `replicating`, `idle`, `baselining`, `paused`, `quiescing`, `quiesced`, and `unhealthy`.
            members (list[ResourceWithLocations]): The union of source and target pods in the replica link.
            sources (list[ResourceWithLocations]): The source pods in the replica link.
            targets (list[ResourceWithLocations]): The target pods in the replica link.
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if lag is not None:
            self.lag = lag
        if paused is not None:
            self.paused = paused
        if recovery_point is not None:
            self.recovery_point = recovery_point
        if status is not None:
            self.status = status
        if members is not None:
            self.members = members
        if sources is not None:
            self.sources = sources
        if targets is not None:
            self.targets = targets

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLink`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLink`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLink`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLink`".format(key))
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
        if issubclass(PodReplicaLink, dict):
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
        if not isinstance(other, PodReplicaLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
