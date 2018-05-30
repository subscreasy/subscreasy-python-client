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

from swagger_client.com.kodfarki.subscreasy.client.model.company import Company  # noqa: F401,E501


class Service(object):
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
        'company': 'Company',
        'id': 'int',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'company': 'company',
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, company=None, id=None, name=None, type=None):  # noqa: E501
        """Service - a model defined in Swagger"""  # noqa: E501

        self._company = None
        self._id = None
        self._name = None
        self._type = None
        self.discriminator = None

        self.company = company
        if id is not None:
            self.id = id
        self.name = name
        self.type = type

    @property
    def company(self):
        """Gets the company of this Service.  # noqa: E501


        :return: The company of this Service.  # noqa: E501
        :rtype: Company
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Service.


        :param company: The company of this Service.  # noqa: E501
        :type: Company
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def id(self):
        """Gets the id of this Service.  # noqa: E501


        :return: The id of this Service.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Service.


        :param id: The id of this Service.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Service.  # noqa: E501


        :return: The name of this Service.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Service.


        :param name: The name of this Service.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Service.  # noqa: E501


        :return: The type of this Service.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Service.


        :param type: The type of this Service.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ONOFF", "SEAT_BASED", "USAGE_BASED"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other