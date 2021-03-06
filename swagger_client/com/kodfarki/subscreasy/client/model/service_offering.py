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
from swagger_client.com.kodfarki.subscreasy.client.model.offer import Offer  # noqa: F401,E501
from swagger_client.com.kodfarki.subscreasy.client.model.service import Service  # noqa: F401,E501


class ServiceOffering(object):
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
        'description': 'str',
        'id': 'int',
        'offer': 'Offer',
        'over_usage_price': 'float',
        'over_usage_quota': 'float',
        'price': 'float',
        'quota_amount': 'float',
        'service': 'Service',
        'unit_name': 'str'
    }

    attribute_map = {
        'company': 'company',
        'description': 'description',
        'id': 'id',
        'offer': 'offer',
        'over_usage_price': 'overUsagePrice',
        'over_usage_quota': 'overUsageQuota',
        'price': 'price',
        'quota_amount': 'quotaAmount',
        'service': 'service',
        'unit_name': 'unitName'
    }

    def __init__(self, company=None, description=None, id=None, offer=None, over_usage_price=None, over_usage_quota=None, price=None, quota_amount=None, service=None, unit_name=None):  # noqa: E501
        """ServiceOffering - a model defined in Swagger"""  # noqa: E501

        self._company = None
        self._description = None
        self._id = None
        self._offer = None
        self._over_usage_price = None
        self._over_usage_quota = None
        self._price = None
        self._quota_amount = None
        self._service = None
        self._unit_name = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        self.offer = offer
        if over_usage_price is not None:
            self.over_usage_price = over_usage_price
        if over_usage_quota is not None:
            self.over_usage_quota = over_usage_quota
        if price is not None:
            self.price = price
        self.quota_amount = quota_amount
        if service is not None:
            self.service = service
        if unit_name is not None:
            self.unit_name = unit_name

    @property
    def company(self):
        """Gets the company of this ServiceOffering.  # noqa: E501


        :return: The company of this ServiceOffering.  # noqa: E501
        :rtype: Company
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ServiceOffering.


        :param company: The company of this ServiceOffering.  # noqa: E501
        :type: Company
        """

        self._company = company

    @property
    def description(self):
        """Gets the description of this ServiceOffering.  # noqa: E501


        :return: The description of this ServiceOffering.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceOffering.


        :param description: The description of this ServiceOffering.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ServiceOffering.  # noqa: E501


        :return: The id of this ServiceOffering.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceOffering.


        :param id: The id of this ServiceOffering.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def offer(self):
        """Gets the offer of this ServiceOffering.  # noqa: E501


        :return: The offer of this ServiceOffering.  # noqa: E501
        :rtype: Offer
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this ServiceOffering.


        :param offer: The offer of this ServiceOffering.  # noqa: E501
        :type: Offer
        """
        if offer is None:
            raise ValueError("Invalid value for `offer`, must not be `None`")  # noqa: E501

        self._offer = offer

    @property
    def over_usage_price(self):
        """Gets the over_usage_price of this ServiceOffering.  # noqa: E501


        :return: The over_usage_price of this ServiceOffering.  # noqa: E501
        :rtype: float
        """
        return self._over_usage_price

    @over_usage_price.setter
    def over_usage_price(self, over_usage_price):
        """Sets the over_usage_price of this ServiceOffering.


        :param over_usage_price: The over_usage_price of this ServiceOffering.  # noqa: E501
        :type: float
        """

        self._over_usage_price = over_usage_price

    @property
    def over_usage_quota(self):
        """Gets the over_usage_quota of this ServiceOffering.  # noqa: E501


        :return: The over_usage_quota of this ServiceOffering.  # noqa: E501
        :rtype: float
        """
        return self._over_usage_quota

    @over_usage_quota.setter
    def over_usage_quota(self, over_usage_quota):
        """Sets the over_usage_quota of this ServiceOffering.


        :param over_usage_quota: The over_usage_quota of this ServiceOffering.  # noqa: E501
        :type: float
        """

        self._over_usage_quota = over_usage_quota

    @property
    def price(self):
        """Gets the price of this ServiceOffering.  # noqa: E501


        :return: The price of this ServiceOffering.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ServiceOffering.


        :param price: The price of this ServiceOffering.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def quota_amount(self):
        """Gets the quota_amount of this ServiceOffering.  # noqa: E501


        :return: The quota_amount of this ServiceOffering.  # noqa: E501
        :rtype: float
        """
        return self._quota_amount

    @quota_amount.setter
    def quota_amount(self, quota_amount):
        """Sets the quota_amount of this ServiceOffering.


        :param quota_amount: The quota_amount of this ServiceOffering.  # noqa: E501
        :type: float
        """
        if quota_amount is None:
            raise ValueError("Invalid value for `quota_amount`, must not be `None`")  # noqa: E501

        self._quota_amount = quota_amount

    @property
    def service(self):
        """Gets the service of this ServiceOffering.  # noqa: E501


        :return: The service of this ServiceOffering.  # noqa: E501
        :rtype: Service
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ServiceOffering.


        :param service: The service of this ServiceOffering.  # noqa: E501
        :type: Service
        """

        self._service = service

    @property
    def unit_name(self):
        """Gets the unit_name of this ServiceOffering.  # noqa: E501


        :return: The unit_name of this ServiceOffering.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this ServiceOffering.


        :param unit_name: The unit_name of this ServiceOffering.  # noqa: E501
        :type: str
        """

        self._unit_name = unit_name

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
        if not isinstance(other, ServiceOffering):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
