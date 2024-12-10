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

class FileSystemSnapshotTransfer(object):
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
        'completed': 'int',
        'data_transferred': 'int',
        'direction': 'Direction',
        'progress': 'float',
        'remote': 'FixedReferenceNoResourceType',
        'remote_snapshot': 'FixedReferenceNoResourceType',
        'started': 'int',
        'status': 'str',
        'local_snapshot': 'FixedReferenceNoResourceType'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'completed': 'completed',
        'data_transferred': 'data_transferred',
        'direction': 'direction',
        'progress': 'progress',
        'remote': 'remote',
        'remote_snapshot': 'remote_snapshot',
        'started': 'started',
        'status': 'status',
        'local_snapshot': 'local_snapshot'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        completed=None,  # type: int
        data_transferred=None,  # type: int
        direction=None,  # type: models.Direction
        progress=None,  # type: float
        remote=None,  # type: models.FixedReferenceNoResourceType
        remote_snapshot=None,  # type: models.FixedReferenceNoResourceType
        started=None,  # type: int
        status=None,  # type: str
        local_snapshot=None,  # type: models.FixedReferenceNoResourceType
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            completed (int): A timestamp at which the replication of the snapshot completed.
            data_transferred (int): The amount of data transferred to the target, in bytes.
            direction (Direction)
            progress (float): A percentage that indicates how much progress has been made on the transfer.
            remote (FixedReferenceNoResourceType): The array where the remote file system snapshot is located.
            remote_snapshot (FixedReferenceNoResourceType): A reference to the associated remote file system snapshot.
            started (int): A timestamp at which the replication of the snapshot started.
            status (str): The status of current replication. Valid values are `completed`, `in-progress`, and `queued`.
            local_snapshot (FixedReferenceNoResourceType): A reference to the associated local file system snapshot.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if completed is not None:
            self.completed = completed
        if data_transferred is not None:
            self.data_transferred = data_transferred
        if direction is not None:
            self.direction = direction
        if progress is not None:
            self.progress = progress
        if remote is not None:
            self.remote = remote
        if remote_snapshot is not None:
            self.remote_snapshot = remote_snapshot
        if started is not None:
            self.started = started
        if status is not None:
            self.status = status
        if local_snapshot is not None:
            self.local_snapshot = local_snapshot

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FileSystemSnapshotTransfer`".format(key))
        if key == "progress" and value is not None:
            if value > 1:
                raise ValueError("Invalid value for `progress`, value must be less than or equal to `1`")
            if value < 0:
                raise ValueError("Invalid value for `progress`, must be a value greater than or equal to `0`")
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
        if issubclass(FileSystemSnapshotTransfer, dict):
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
        if not isinstance(other, FileSystemSnapshotTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
