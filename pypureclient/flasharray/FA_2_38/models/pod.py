# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.38
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_38 import models

class Pod(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'context': 'FixedReference',
        'arrays': 'list[PodArrayStatus]',
        'destroyed': 'bool',
        'failover_preferences': 'list[Reference]',
        'footprint': 'int',
        'mediator': 'str',
        'mediator_version': 'str',
        'source': 'FixedReference',
        'time_remaining': 'int',
        'requested_promotion_state': 'str',
        'promotion_status': 'str',
        'link_source_count': 'int',
        'link_target_count': 'int',
        'array_count': 'int',
        'eradication_config': 'ContainerEradicationConfig',
        'quota_limit': 'int',
        'space': 'PodSpace',
        'members': 'list[ReferenceWithType]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'context': 'context',
        'arrays': 'arrays',
        'destroyed': 'destroyed',
        'failover_preferences': 'failover_preferences',
        'footprint': 'footprint',
        'mediator': 'mediator',
        'mediator_version': 'mediator_version',
        'source': 'source',
        'time_remaining': 'time_remaining',
        'requested_promotion_state': 'requested_promotion_state',
        'promotion_status': 'promotion_status',
        'link_source_count': 'link_source_count',
        'link_target_count': 'link_target_count',
        'array_count': 'array_count',
        'eradication_config': 'eradication_config',
        'quota_limit': 'quota_limit',
        'space': 'space',
        'members': 'members'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        context=None,  # type: models.FixedReference
        arrays=None,  # type: List[models.PodArrayStatus]
        destroyed=None,  # type: bool
        failover_preferences=None,  # type: List[models.Reference]
        footprint=None,  # type: int
        mediator=None,  # type: str
        mediator_version=None,  # type: str
        source=None,  # type: models.FixedReference
        time_remaining=None,  # type: int
        requested_promotion_state=None,  # type: str
        promotion_status=None,  # type: str
        link_source_count=None,  # type: int
        link_target_count=None,  # type: int
        array_count=None,  # type: int
        eradication_config=None,  # type: models.ContainerEradicationConfig
        quota_limit=None,  # type: int
        space=None,  # type: models.PodSpace
        members=None,  # type: List[models.ReferenceWithType]
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            context (FixedReference): The context in which the operation was performed. Valid values include a reference to any array which is a member of the same fleet. If the array is not a member of a fleet, `context` will always implicitly be set to the array that received the request. Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`.
            arrays (list[PodArrayStatus]): A list of arrays over which the pod is stretched. If there are two or more arrays in the stretched pod, all data in the pod is synchronously replicated between all of the arrays within the pod.
            destroyed (bool): Returns a value of `true` if the pod has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed pod is permanently eradicated. Before the `time_remaining` period has elapsed, the destroyed pod can be recovered by setting `destroyed=false`. Once the `time_remaining` period has elapsed, the pod is permanently eradicated and can no longer be recovered.
            failover_preferences (list[Reference]): Determines which array within a stretched pod should be given priority to stay online should the arrays ever lose contact with each other. The current array and any peer arrays that are connected to the current array for synchronous replication can be added to a pod for failover preference. By default, `failover_preferences=null`, meaning no arrays have been configured for failover preference.
            footprint (int): This field has been deprecated. Use the `space.footprint` field in the future, as it contains the same information. The maximum amount of space the pod would take up on any array, ignoring any data shared outside the pod. Measured in bytes. The footprint metric is mostly used for capacity planning.
            mediator (str): The URL of the mediator for the pod. By default, the Pure1 Cloud Mediator (`purestorage`) serves as the mediator.
            mediator_version (str): The mediator version.
            source (FixedReference): The source pod from where data is cloned to create the new pod.
            time_remaining (int): The amount of time left until the destroyed pod is permanently eradicated, measured in milliseconds. Before the `time_remaining` period has elapsed, the destroyed pod can be recovered by setting `destroyed=false`.
            requested_promotion_state (str): Values include `promoted` and `demoted`. Patch `requested_promotion_state` to `demoted` to demote the pod so that it can be used as a link target for continuous replication between pods. Demoted pods do not accept write requests, and a destroyed version of the pod with `undo-demote` appended to the pod name is created on the array with the state of the pod when it was in the promoted state. Patch `requested_promotion_state` to `promoted` to start the process of promoting the pod. The `promotion_status` indicates when the pod has been successfully promoted. Promoted pods stop incorporating replicated data from the source pod and start accepting write requests. The replication process does not stop as the source pod continues replicating data to the pod. The space consumed by the unique replicated data is tracked by the `space.journal` field of the pod.
            promotion_status (str): Current promotion status of a pod. Values include `promoted`, `demoted`, and `promoting`. The `promoted` status indicates that the pod has been promoted. The pod takes writes from hosts instead of incorporating replicated data. This is the default mode for a pod when it is created. The `demoted` status indicates that the pod has been demoted. The pod does not accept write requests and is ready to be used as a link target. The `promoting` status indicates that the pod is in an intermediate status between `demoted` and `promoted` while the promotion process is taking place.
            link_source_count (int): The number of source pods that link to the pod.
            link_target_count (int): The number of target pods that link to the pod.
            array_count (int): The number of arrays a pod connects to.
            eradication_config (ContainerEradicationConfig)
            quota_limit (int): The logical quota limit of the pod, measured in bytes.
            space (PodSpace): Displays provisioned size and physical storage consumption information for the sum of all volumes connected to the specified host.
            members (list[ReferenceWithType]): A list of arrays or realms over which the pod is stretched. If there are two or more members in the stretched pod, all data in the pod is synchronously replicated between all of the members within the pod.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if context is not None:
            self.context = context
        if arrays is not None:
            self.arrays = arrays
        if destroyed is not None:
            self.destroyed = destroyed
        if failover_preferences is not None:
            self.failover_preferences = failover_preferences
        if footprint is not None:
            self.footprint = footprint
        if mediator is not None:
            self.mediator = mediator
        if mediator_version is not None:
            self.mediator_version = mediator_version
        if source is not None:
            self.source = source
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if requested_promotion_state is not None:
            self.requested_promotion_state = requested_promotion_state
        if promotion_status is not None:
            self.promotion_status = promotion_status
        if link_source_count is not None:
            self.link_source_count = link_source_count
        if link_target_count is not None:
            self.link_target_count = link_target_count
        if array_count is not None:
            self.array_count = array_count
        if eradication_config is not None:
            self.eradication_config = eradication_config
        if quota_limit is not None:
            self.quota_limit = quota_limit
        if space is not None:
            self.space = space
        if members is not None:
            self.members = members

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Pod`".format(key))
        if key == "footprint" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `footprint`, must be a value greater than or equal to `0`")
        if key == "quota_limit" and value is not None:
            if value > 4503599627370496:
                raise ValueError("Invalid value for `quota_limit`, value must be less than or equal to `4503599627370496`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Pod`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Pod`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Pod`".format(key))
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
        if issubclass(Pod, dict):
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
        if not isinstance(other, Pod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
