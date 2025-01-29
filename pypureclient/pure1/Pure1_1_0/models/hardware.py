# coding: utf-8

"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](https://www.purestorage.com)  The Pure1 REST API 2.0 offers one single form of authentication: OAuth 2.0 via the [Token Exchange protocol](https://datatracker.ietf.org/doc/draft-ietf-oauth-token-exchange).  OAuth 2.0 is an open protocol to allow secure authorization in a simple and standard method from web, mobile, desktop and background applications.  Note that the [Authentication](#section/Authentication) section below mentions 'API Key' as the security scheme type. This is solely for the purpose of allowing testing this API with [Swagger UI](https://static.pure1.purestorage.com/api-swagger/index.html).  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_0 import models

class Hardware(object):
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
        'arrays': 'list[FixedReference]',
        'details': 'str',
        'identify_enabled': 'bool',
        'model': 'str',
        'serial': 'str',
        'slot': 'int',
        'speed': 'int',
        'status': 'str',
        'temperature': 'int',
        'type': 'str',
        'voltage': 'int'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'arrays': 'arrays',
        'details': 'details',
        'identify_enabled': 'identify_enabled',
        'model': 'model',
        'serial': 'serial',
        'slot': 'slot',
        'speed': 'speed',
        'status': 'status',
        'temperature': 'temperature',
        'type': 'type',
        'voltage': 'voltage'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        name=None,  # type: str
        arrays=None,  # type: List[models.FixedReference]
        details=None,  # type: str
        identify_enabled=None,  # type: bool
        model=None,  # type: str
        serial=None,  # type: str
        slot=None,  # type: int
        speed=None,  # type: int
        status=None,  # type: str
        temperature=None,  # type: int
        type=None,  # type: str
        voltage=None,  # type: int
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A non-modifiable, locally unique name chosen by the system.
            arrays (list[FixedReference]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays.
            details (str): Details about the component if `status` is not `healthy`.
            identify_enabled (bool): If true, the ID light is lit to visually identify the component.
            model (str): Model number of the hardware component.
            serial (str): Serial number of the hardware component.
            slot (int): Slot number occupied by the PCI Express card that hosts the component.
            speed (int): Speed (in bytes per second) at which the component is operating.
            status (str): Component status. Values include `critical`, `healthy`, `identifying`, `unhealthy`, `unclaimed`, `unknown`, `unrecognized`, and `unused`.
            temperature (int): Temperature (in degrees Celsius) reported by the component.
            type (str): Type of the hardware component. Values include `am`, `chassis`, `controller`, `cooling`, `drive_bay`, `eth_port`, `fan`, `fc_port`, `flash_blade`, `ib_port`, `mgmt_port`, `nvram_bay`, `power_supply`, `sas_module`, `sas_port`, `storage_shelf`, and `temp_sensor`.
            voltage (int): Voltage (in Volts) reported by the component.
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if arrays is not None:
            self.arrays = arrays
        if details is not None:
            self.details = details
        if identify_enabled is not None:
            self.identify_enabled = identify_enabled
        if model is not None:
            self.model = model
        if serial is not None:
            self.serial = serial
        if slot is not None:
            self.slot = slot
        if speed is not None:
            self.speed = speed
        if status is not None:
            self.status = status
        if temperature is not None:
            self.temperature = temperature
        if type is not None:
            self.type = type
        if voltage is not None:
            self.voltage = voltage

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Hardware`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Hardware`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Hardware`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Hardware`".format(key))
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
        if issubclass(Hardware, dict):
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
        if not isinstance(other, Hardware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
