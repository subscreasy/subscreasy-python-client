# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from com.kodfarki.subscreasy.client.subscriber_resource_api import SubscriberResourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSubscriberResourceApi(unittest.TestCase):
    """SubscriberResourceApi unit test stubs"""

    def setUp(self):
        self.api = com.kodfarki.subscreasy.client.subscriber_resource_api.SubscriberResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_subscriber_using_post(self):
        """Test case for create_subscriber_using_post

        createSubscriber  # noqa: E501
        """
        pass

    def test_delete_subscriber_using_delete(self):
        """Test case for delete_subscriber_using_delete

        deleteSubscriber  # noqa: E501
        """
        pass

    def test_get_all_subscribers_using_get(self):
        """Test case for get_all_subscribers_using_get

        getAllSubscribers  # noqa: E501
        """
        pass

    def test_get_subscriber_by_email_using_get(self):
        """Test case for get_subscriber_by_email_using_get

        getSubscriberByEmail  # noqa: E501
        """
        pass

    def test_get_subscriber_by_name_using_get(self):
        """Test case for get_subscriber_by_name_using_get

        getSubscriberByName  # noqa: E501
        """
        pass

    def test_get_subscriber_using_get(self):
        """Test case for get_subscriber_using_get

        getSubscriber  # noqa: E501
        """
        pass

    def test_update_subscriber_using_put(self):
        """Test case for update_subscriber_using_put

        updateSubscriber  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()