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


class Cancellation(object):
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
        'cancellation_type': 'str',
        'subscription_id': 'int'
    }

    attribute_map = {
        'cancellation_type': 'cancellationType',
        'subscription_id': 'subscriptionId'
    }

    def __init__(self, cancellation_type=None, subscription_id=None):  # noqa: E501
        """Cancellation - a model defined in Swagger"""  # noqa: E501

        self._cancellation_type = None
        self._subscription_id = None
        self.discriminator = None

        if cancellation_type is not None:
            self.cancellation_type = cancellation_type
        if subscription_id is not None:
            self.subscription_id = subscription_id

    @property
    def cancellation_type(self):
        """Gets the cancellation_type of this Cancellation.  # noqa: E501


        :return: The cancellation_type of this Cancellation.  # noqa: E501
        :rtype: str
        """
        return self._cancellation_type

    @cancellation_type.setter
    def cancellation_type(self, cancellation_type):
        """Sets the cancellation_type of this Cancellation.


        :param cancellation_type: The cancellation_type of this Cancellation.  # noqa: E501
        :type: str
        """
        allowed_values = ["IMMEDIATE", "ENDOFTHEPERIOD"]  # noqa: E501
        if cancellation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cancellation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cancellation_type, allowed_values)
            )

        self._cancellation_type = cancellation_type

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Cancellation.  # noqa: E501


        :return: The subscription_id of this Cancellation.  # noqa: E501
        :rtype: int
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Cancellation.


        :param subscription_id: The subscription_id of this Cancellation.  # noqa: E501
        :type: int
        """

        self._subscription_id = subscription_id

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
        if not isinstance(other, Cancellation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
