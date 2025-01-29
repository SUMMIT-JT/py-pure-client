# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.39
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_39 import models

class Space(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data_reduction': 'float',
        'shared': 'int',
        'snapshots': 'int',
        'system': 'int',
        'thin_provisioning': 'float',
        'total_physical': 'int',
        'total_provisioned': 'int',
        'total_reduction': 'float',
        'unique': 'int',
        'virtual': 'int',
        'used_provisioned': 'int',
        'total_used': 'int',
        'footprint': 'int',
        'shared_effective': 'int',
        'snapshots_effective': 'int',
        'unique_effective': 'int',
        'total_effective': 'int',
        'replication': 'int'
    }

    attribute_map = {
        'data_reduction': 'data_reduction',
        'shared': 'shared',
        'snapshots': 'snapshots',
        'system': 'system',
        'thin_provisioning': 'thin_provisioning',
        'total_physical': 'total_physical',
        'total_provisioned': 'total_provisioned',
        'total_reduction': 'total_reduction',
        'unique': 'unique',
        'virtual': 'virtual',
        'used_provisioned': 'used_provisioned',
        'total_used': 'total_used',
        'footprint': 'footprint',
        'shared_effective': 'shared_effective',
        'snapshots_effective': 'snapshots_effective',
        'unique_effective': 'unique_effective',
        'total_effective': 'total_effective',
        'replication': 'replication'
    }

    required_args = {
    }

    def __init__(
        self,
        data_reduction=None,  # type: float
        shared=None,  # type: int
        snapshots=None,  # type: int
        system=None,  # type: int
        thin_provisioning=None,  # type: float
        total_physical=None,  # type: int
        total_provisioned=None,  # type: int
        total_reduction=None,  # type: float
        unique=None,  # type: int
        virtual=None,  # type: int
        used_provisioned=None,  # type: int
        total_used=None,  # type: int
        footprint=None,  # type: int
        shared_effective=None,  # type: int
        snapshots_effective=None,  # type: int
        unique_effective=None,  # type: int
        total_effective=None,  # type: int
        replication=None,  # type: int
    ):
        """
        Keyword args:
            data_reduction (float): The ratio of mapped sectors within a volume versus the amount of physical space the data occupies after data compression and deduplication. The data reduction ratio does not include thin provisioning savings. For example, a data reduction ratio of 5&#58;1 means that for every 5 MB the host writes to the array, 1 MB is stored on the array's flash modules.
            shared (int): The physical space occupied by deduplicated data, meaning that the space is shared with other volumes and snapshots as a result of data deduplication. Measured in bytes. On Evergreen//One arrays, this is the effective space contributed by data that is not unique to a specific volume, managed directory, or snapshot, measured in bytes.
            snapshots (int): The physical space occupied by data unique to one or more snapshots. Measured in bytes. On Evergreen//One arrays, this is the effective space contributed by data unique to one or more snapshots, measured in bytes.
            system (int): The physical space occupied by internal array metadata. Measured in bytes.
            thin_provisioning (float): The percentage of volume sectors that do not contain host-written data because the hosts have not written data to them or the sectors have been explicitly trimmed.
            total_physical (int): This field has been deprecated. Use the `total_used` field, as it contains the same information.
            total_provisioned (int): The provisioned size of a volume for a single volume, host or host group, protocol endpoint, managed directory, and containers can be infinite or measured in bytes. Infinite is represented by `null`. The provisioned size for a host or host group, includes all volumes that are connected to the resource. The provisioned size for a protocol endpoint is `null'. The provisioned size for a managed directory is the quota limit if it or its parent has a managed directory configured, otherwise it defaults to `null`. The provisioned size for a container is the sum of the total_provisioned of the object it contains, capped by the container's quota limit (or the container's used_provisioned if current usage is above the quota limit), if any. Provisioned size represents the storage capacity reported to hosts.
            total_reduction (float): The ratio of provisioned sectors within a volume versus the amount of physical space the data occupies after reduction via data compression and deduplication and with thin provisioning savings. Total reduction is data reduction with thin provisioning savings. For example, a total reduction ratio of 10&#58;1 means that for every 10 MB of provisioned space, 1 MB is stored on the array's flash modules.
            unique (int): The unique physical space occupied by customer data. Unique physical space does not include shared space, snapshots, and internal array metadata. Measured in bytes. On Evergreen//One arrays, this is the effective space contributed by unique customer data, measured in bytes. Unique data does not include shared space, snapshots, and internal array metadata.
            virtual (int): The amount of logically written data that a volume or a snapshot references. Measured in bytes.
            used_provisioned (int): The amount of logical space a container has consumed, compared against the quota limit if the container has one configured. Used provisioned does not include destroyed objects inside the container. Used provisioned can include destroyed objects for a destroyed container and represents how much logical space it would take to recover the container.
            total_used (int): The total space contributed by customer data, measured in bytes.
            footprint (int): The maximum amount of physical space the container consumes on an array, ignoring any data shared outside the container, measured in bytes. On Evergreen//One arrays, this is the maximum amount of effective used space. The footprint metric is mostly used for capacity planning. This field will be null in non-container contexts.
            shared_effective (int): This field has been deprecated. It will return `null`. Use the `shared` field in the future, as it contains the same information for Evergreen//One arrays.
            snapshots_effective (int): This field has deprecated. It will return `null`. Use the `snapshots` field in the future, as it contains the same information for Evergreen//One arrays.
            unique_effective (int): This field has been deprecated. It will return `null`. Use the `unique` field in the future, as it contains the same information for Evergreen//One arrays.
            total_effective (int): This field has been deprecated. It will return `null`. PUse the `total_physical` field instead, as it contains the same information for Evergreen//One arrays.
            replication (int): The sum of replication space consumed by all pods on this array.
        """
        if data_reduction is not None:
            self.data_reduction = data_reduction
        if shared is not None:
            self.shared = shared
        if snapshots is not None:
            self.snapshots = snapshots
        if system is not None:
            self.system = system
        if thin_provisioning is not None:
            self.thin_provisioning = thin_provisioning
        if total_physical is not None:
            self.total_physical = total_physical
        if total_provisioned is not None:
            self.total_provisioned = total_provisioned
        if total_reduction is not None:
            self.total_reduction = total_reduction
        if unique is not None:
            self.unique = unique
        if virtual is not None:
            self.virtual = virtual
        if used_provisioned is not None:
            self.used_provisioned = used_provisioned
        if total_used is not None:
            self.total_used = total_used
        if footprint is not None:
            self.footprint = footprint
        if shared_effective is not None:
            self.shared_effective = shared_effective
        if snapshots_effective is not None:
            self.snapshots_effective = snapshots_effective
        if unique_effective is not None:
            self.unique_effective = unique_effective
        if total_effective is not None:
            self.total_effective = total_effective
        if replication is not None:
            self.replication = replication

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Space`".format(key))
        if key == "shared" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `shared`, must be a value greater than or equal to `0`")
        if key == "snapshots" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `snapshots`, must be a value greater than or equal to `0`")
        if key == "system" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `system`, must be a value greater than or equal to `0`")
        if key == "thin_provisioning" and value is not None:
            if value > 1.0:
                raise ValueError("Invalid value for `thin_provisioning`, value must be less than or equal to `1.0`")
            if value < 0.0:
                raise ValueError("Invalid value for `thin_provisioning`, must be a value greater than or equal to `0.0`")
        if key == "total_physical" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `total_physical`, must be a value greater than or equal to `0`")
        if key == "total_provisioned" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `total_provisioned`, must be a value greater than or equal to `0`")
        if key == "unique" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `unique`, must be a value greater than or equal to `0`")
        if key == "virtual" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `virtual`, must be a value greater than or equal to `0`")
        if key == "used_provisioned" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `used_provisioned`, must be a value greater than or equal to `0`")
        if key == "total_used" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `total_used`, must be a value greater than or equal to `0`")
        if key == "footprint" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `footprint`, must be a value greater than or equal to `0`")
        if key == "shared_effective" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `shared_effective`, must be a value greater than or equal to `0`")
        if key == "snapshots_effective" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `snapshots_effective`, must be a value greater than or equal to `0`")
        if key == "unique_effective" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `unique_effective`, must be a value greater than or equal to `0`")
        if key == "total_effective" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `total_effective`, must be a value greater than or equal to `0`")
        if key == "replication" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `replication`, must be a value greater than or equal to `0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Space`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Space`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Space`".format(key))
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
        if issubclass(Space, dict):
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
        if not isinstance(other, Space):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
