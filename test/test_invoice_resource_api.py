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
from com.kodfarki.subscreasy.client.invoice_resource_api import InvoiceResourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestInvoiceResourceApi(unittest.TestCase):
    """InvoiceResourceApi unit test stubs"""

    def setUp(self):
        self.api = com.kodfarki.subscreasy.client.invoice_resource_api.InvoiceResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_invoice_using_post(self):
        """Test case for create_invoice_using_post

        createInvoice  # noqa: E501
        """
        pass

    def test_delete_invoice_using_delete(self):
        """Test case for delete_invoice_using_delete

        deleteInvoice  # noqa: E501
        """
        pass

    def test_get_all_invoices_using_get(self):
        """Test case for get_all_invoices_using_get

        getAllInvoices  # noqa: E501
        """
        pass

    def test_get_invoice_by_subscriber_using_get(self):
        """Test case for get_invoice_by_subscriber_using_get

        getInvoiceBySubscriber  # noqa: E501
        """
        pass

    def test_get_invoice_using_get(self):
        """Test case for get_invoice_using_get

        getInvoice  # noqa: E501
        """
        pass

    def test_update_invoice_using_put(self):
        """Test case for update_invoice_using_put

        updateInvoice  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
