# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.37
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_37 import models

class HostPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'chap': 'Chap',
        'iqns': 'list[str]',
        'nqns': 'list[str]',
        'personality': 'str',
        'preferred_arrays': 'list[Reference]',
        'wwns': 'list[str]',
        'vlan': 'str'
    }

    attribute_map = {
        'chap': 'chap',
        'iqns': 'iqns',
        'nqns': 'nqns',
        'personality': 'personality',
        'preferred_arrays': 'preferred_arrays',
        'wwns': 'wwns',
        'vlan': 'vlan'
    }

    required_args = {
    }

    def __init__(
        self,
        chap=None,  # type: models.Chap
        iqns=None,  # type: List[str]
        nqns=None,  # type: List[str]
        personality=None,  # type: str
        preferred_arrays=None,  # type: List[models.Reference]
        wwns=None,  # type: List[str]
        vlan=None,  # type: str
    ):
        """
        Keyword args:
            chap (Chap)
            iqns (list[str]): The iSCSI qualified name (IQN) associated with the host.
            nqns (list[str]): The NVMe Qualified Name (NQN) associated with the host.
            personality (str): Determines how the system tunes the array to ensure that it works optimally with the host. Set `personality` to the name of the host operating system or virtual memory system. Valid values are `aix`, `esxi`, `hitachi-vsp`, `hpux`, `oracle-vm-server`, `solaris`, and `vms`. If your system is not listed as one of the valid host personalities, do not set the option. By default, the personality is not set.
            preferred_arrays (list[Reference]): For synchronous replication configurations, sets a host's preferred array to specify which array exposes active/optimized paths to that host. Enter multiple preferred arrays in comma-separated format. If a preferred array is set for a host, then the other arrays in the same pod will expose active/non-optimized paths to that host. If the host is in a host group, `preferred_arrays` cannot be set because host groups have their own preferred arrays. On a preferred array of a certain host, all the paths on all the ports (for both the primary and secondary controllers) are set up as A/O (active/optimized) paths, while on a non-preferred array, all the paths are A/N (Active/Non-optimized) paths.
            wwns (list[str]): The Fibre Channel World Wide Name (WWN) associated with the host.
            vlan (str): The VLAN ID that the host is associated with. If not set or set to `any`, the host can access any VLAN. If set to `untagged`, the host can only access untagged VLANs. If set to a number between `1` and `4094`, the host can only access the specified VLAN with that number.
        """
        if chap is not None:
            self.chap = chap
        if iqns is not None:
            self.iqns = iqns
        if nqns is not None:
            self.nqns = nqns
        if personality is not None:
            self.personality = personality
        if preferred_arrays is not None:
            self.preferred_arrays = preferred_arrays
        if wwns is not None:
            self.wwns = wwns
        if vlan is not None:
            self.vlan = vlan

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `HostPost`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `HostPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `HostPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `HostPost`".format(key))
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
        if issubclass(HostPost, dict):
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
        if not isinstance(other, HostPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
