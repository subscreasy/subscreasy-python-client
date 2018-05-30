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


class Subscriber(object):
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
        'address': 'str',
        'city': 'str',
        'country': 'str',
        'email': 'str',
        'gsm_number': 'str',
        'identity_number': 'str',
        'ip': 'str',
        'last_login_date': 'str',
        'name': 'str',
        'registration_date': 'str',
        'secure_id': 'str',
        'shipping_address': 'str',
        'shipping_city': 'str',
        'shipping_country': 'str',
        'shipping_name': 'str',
        'shipping_zip_code': 'str',
        'surname': 'str',
        'use_billing_address_for_shipping': 'bool',
        'zip_code': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'country': 'country',
        'email': 'email',
        'gsm_number': 'gsmNumber',
        'identity_number': 'identityNumber',
        'ip': 'ip',
        'last_login_date': 'lastLoginDate',
        'name': 'name',
        'registration_date': 'registrationDate',
        'secure_id': 'secureId',
        'shipping_address': 'shippingAddress',
        'shipping_city': 'shippingCity',
        'shipping_country': 'shippingCountry',
        'shipping_name': 'shippingName',
        'shipping_zip_code': 'shippingZipCode',
        'surname': 'surname',
        'use_billing_address_for_shipping': 'useBillingAddressForShipping',
        'zip_code': 'zipCode'
    }

    def __init__(self, address=None, city=None, country=None, email=None, gsm_number=None, identity_number=None, ip=None, last_login_date=None, name=None, registration_date=None, secure_id=None, shipping_address=None, shipping_city=None, shipping_country=None, shipping_name=None, shipping_zip_code=None, surname=None, use_billing_address_for_shipping=None, zip_code=None):  # noqa: E501
        """Subscriber - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._city = None
        self._country = None
        self._email = None
        self._gsm_number = None
        self._identity_number = None
        self._ip = None
        self._last_login_date = None
        self._name = None
        self._registration_date = None
        self._secure_id = None
        self._shipping_address = None
        self._shipping_city = None
        self._shipping_country = None
        self._shipping_name = None
        self._shipping_zip_code = None
        self._surname = None
        self._use_billing_address_for_shipping = None
        self._zip_code = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if gsm_number is not None:
            self.gsm_number = gsm_number
        if identity_number is not None:
            self.identity_number = identity_number
        if ip is not None:
            self.ip = ip
        if last_login_date is not None:
            self.last_login_date = last_login_date
        if name is not None:
            self.name = name
        if registration_date is not None:
            self.registration_date = registration_date
        if secure_id is not None:
            self.secure_id = secure_id
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if shipping_city is not None:
            self.shipping_city = shipping_city
        if shipping_country is not None:
            self.shipping_country = shipping_country
        if shipping_name is not None:
            self.shipping_name = shipping_name
        if shipping_zip_code is not None:
            self.shipping_zip_code = shipping_zip_code
        if surname is not None:
            self.surname = surname
        if use_billing_address_for_shipping is not None:
            self.use_billing_address_for_shipping = use_billing_address_for_shipping
        if zip_code is not None:
            self.zip_code = zip_code

    @property
    def address(self):
        """Gets the address of this Subscriber.  # noqa: E501


        :return: The address of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Subscriber.


        :param address: The address of this Subscriber.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this Subscriber.  # noqa: E501


        :return: The city of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Subscriber.


        :param city: The city of this Subscriber.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Subscriber.  # noqa: E501


        :return: The country of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Subscriber.


        :param country: The country of this Subscriber.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """Gets the email of this Subscriber.  # noqa: E501


        :return: The email of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Subscriber.


        :param email: The email of this Subscriber.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def gsm_number(self):
        """Gets the gsm_number of this Subscriber.  # noqa: E501


        :return: The gsm_number of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._gsm_number

    @gsm_number.setter
    def gsm_number(self, gsm_number):
        """Sets the gsm_number of this Subscriber.


        :param gsm_number: The gsm_number of this Subscriber.  # noqa: E501
        :type: str
        """

        self._gsm_number = gsm_number

    @property
    def identity_number(self):
        """Gets the identity_number of this Subscriber.  # noqa: E501


        :return: The identity_number of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._identity_number

    @identity_number.setter
    def identity_number(self, identity_number):
        """Sets the identity_number of this Subscriber.


        :param identity_number: The identity_number of this Subscriber.  # noqa: E501
        :type: str
        """

        self._identity_number = identity_number

    @property
    def ip(self):
        """Gets the ip of this Subscriber.  # noqa: E501


        :return: The ip of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Subscriber.


        :param ip: The ip of this Subscriber.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def last_login_date(self):
        """Gets the last_login_date of this Subscriber.  # noqa: E501


        :return: The last_login_date of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._last_login_date

    @last_login_date.setter
    def last_login_date(self, last_login_date):
        """Sets the last_login_date of this Subscriber.


        :param last_login_date: The last_login_date of this Subscriber.  # noqa: E501
        :type: str
        """

        self._last_login_date = last_login_date

    @property
    def name(self):
        """Gets the name of this Subscriber.  # noqa: E501


        :return: The name of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Subscriber.


        :param name: The name of this Subscriber.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def registration_date(self):
        """Gets the registration_date of this Subscriber.  # noqa: E501


        :return: The registration_date of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this Subscriber.


        :param registration_date: The registration_date of this Subscriber.  # noqa: E501
        :type: str
        """

        self._registration_date = registration_date

    @property
    def secure_id(self):
        """Gets the secure_id of this Subscriber.  # noqa: E501


        :return: The secure_id of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._secure_id

    @secure_id.setter
    def secure_id(self, secure_id):
        """Sets the secure_id of this Subscriber.


        :param secure_id: The secure_id of this Subscriber.  # noqa: E501
        :type: str
        """

        self._secure_id = secure_id

    @property
    def shipping_address(self):
        """Gets the shipping_address of this Subscriber.  # noqa: E501


        :return: The shipping_address of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Subscriber.


        :param shipping_address: The shipping_address of this Subscriber.  # noqa: E501
        :type: str
        """

        self._shipping_address = shipping_address

    @property
    def shipping_city(self):
        """Gets the shipping_city of this Subscriber.  # noqa: E501


        :return: The shipping_city of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._shipping_city

    @shipping_city.setter
    def shipping_city(self, shipping_city):
        """Sets the shipping_city of this Subscriber.


        :param shipping_city: The shipping_city of this Subscriber.  # noqa: E501
        :type: str
        """

        self._shipping_city = shipping_city

    @property
    def shipping_country(self):
        """Gets the shipping_country of this Subscriber.  # noqa: E501


        :return: The shipping_country of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._shipping_country

    @shipping_country.setter
    def shipping_country(self, shipping_country):
        """Sets the shipping_country of this Subscriber.


        :param shipping_country: The shipping_country of this Subscriber.  # noqa: E501
        :type: str
        """

        self._shipping_country = shipping_country

    @property
    def shipping_name(self):
        """Gets the shipping_name of this Subscriber.  # noqa: E501


        :return: The shipping_name of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._shipping_name

    @shipping_name.setter
    def shipping_name(self, shipping_name):
        """Sets the shipping_name of this Subscriber.


        :param shipping_name: The shipping_name of this Subscriber.  # noqa: E501
        :type: str
        """

        self._shipping_name = shipping_name

    @property
    def shipping_zip_code(self):
        """Gets the shipping_zip_code of this Subscriber.  # noqa: E501


        :return: The shipping_zip_code of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._shipping_zip_code

    @shipping_zip_code.setter
    def shipping_zip_code(self, shipping_zip_code):
        """Sets the shipping_zip_code of this Subscriber.


        :param shipping_zip_code: The shipping_zip_code of this Subscriber.  # noqa: E501
        :type: str
        """

        self._shipping_zip_code = shipping_zip_code

    @property
    def surname(self):
        """Gets the surname of this Subscriber.  # noqa: E501


        :return: The surname of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this Subscriber.


        :param surname: The surname of this Subscriber.  # noqa: E501
        :type: str
        """

        self._surname = surname

    @property
    def use_billing_address_for_shipping(self):
        """Gets the use_billing_address_for_shipping of this Subscriber.  # noqa: E501


        :return: The use_billing_address_for_shipping of this Subscriber.  # noqa: E501
        :rtype: bool
        """
        return self._use_billing_address_for_shipping

    @use_billing_address_for_shipping.setter
    def use_billing_address_for_shipping(self, use_billing_address_for_shipping):
        """Sets the use_billing_address_for_shipping of this Subscriber.


        :param use_billing_address_for_shipping: The use_billing_address_for_shipping of this Subscriber.  # noqa: E501
        :type: bool
        """

        self._use_billing_address_for_shipping = use_billing_address_for_shipping

    @property
    def zip_code(self):
        """Gets the zip_code of this Subscriber.  # noqa: E501


        :return: The zip_code of this Subscriber.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Subscriber.


        :param zip_code: The zip_code of this Subscriber.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

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
        if not isinstance(other, Subscriber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other