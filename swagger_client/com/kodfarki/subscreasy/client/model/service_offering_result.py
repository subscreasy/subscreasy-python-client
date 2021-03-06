# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ServiceOfferingResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'capacity': 'str',
        'id': 'int',
        'name': 'str',
        'price': 'float',
        'type': 'str',
        'unit_name': 'str',
        'units_per_price': 'float'
    }

    attribute_map = {
        'capacity': 'capacity',
        'id': 'id',
        'name': 'name',
        'price': 'price',
        'type': 'type',
        'unit_name': 'unitName',
        'units_per_price': 'unitsPerPrice'
    }

    def __init__(self, capacity=None, id=None, name=None, price=None, type=None, unit_name=None, units_per_price=None):  # noqa: E501
        """ServiceOfferingResult - a model defined in Swagger"""  # noqa: E501

        self._capacity = None
        self._id = None
        self._name = None
        self._price = None
        self._type = None
        self._unit_name = None
        self._units_per_price = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if type is not None:
            self.type = type
        if unit_name is not None:
            self.unit_name = unit_name
        if units_per_price is not None:
            self.units_per_price = units_per_price

    @property
    def capacity(self):
        """Gets the capacity of this ServiceOfferingResult.  # noqa: E501


        :return: The capacity of this ServiceOfferingResult.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ServiceOfferingResult.


        :param capacity: The capacity of this ServiceOfferingResult.  # noqa: E501
        :type: str
        """

        self._capacity = capacity

    @property
    def id(self):
        """Gets the id of this ServiceOfferingResult.  # noqa: E501


        :return: The id of this ServiceOfferingResult.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceOfferingResult.


        :param id: The id of this ServiceOfferingResult.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ServiceOfferingResult.  # noqa: E501


        :return: The name of this ServiceOfferingResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceOfferingResult.


        :param name: The name of this ServiceOfferingResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """Gets the price of this ServiceOfferingResult.  # noqa: E501


        :return: The price of this ServiceOfferingResult.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ServiceOfferingResult.


        :param price: The price of this ServiceOfferingResult.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def type(self):
        """Gets the type of this ServiceOfferingResult.  # noqa: E501


        :return: The type of this ServiceOfferingResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServiceOfferingResult.


        :param type: The type of this ServiceOfferingResult.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def unit_name(self):
        """Gets the unit_name of this ServiceOfferingResult.  # noqa: E501


        :return: The unit_name of this ServiceOfferingResult.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this ServiceOfferingResult.


        :param unit_name: The unit_name of this ServiceOfferingResult.  # noqa: E501
        :type: str
        """

        self._unit_name = unit_name

    @property
    def units_per_price(self):
        """Gets the units_per_price of this ServiceOfferingResult.  # noqa: E501


        :return: The units_per_price of this ServiceOfferingResult.  # noqa: E501
        :rtype: float
        """
        return self._units_per_price

    @units_per_price.setter
    def units_per_price(self, units_per_price):
        """Sets the units_per_price of this ServiceOfferingResult.


        :param units_per_price: The units_per_price of this ServiceOfferingResult.  # noqa: E501
        :type: float
        """

        self._units_per_price = units_per_price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServiceOfferingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
