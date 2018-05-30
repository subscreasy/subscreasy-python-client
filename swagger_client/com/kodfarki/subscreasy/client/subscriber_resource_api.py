# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SubscriberResourceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_subscriber_using_post(self, subscriber, **kwargs):  # noqa: E501
        """createSubscriber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_subscriber_using_post(subscriber, async=True)
        >>> result = thread.get()

        :param async bool
        :param Subscriber subscriber: subscriber (required)
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_subscriber_using_post_with_http_info(subscriber, **kwargs)  # noqa: E501
        else:
            (data) = self.create_subscriber_using_post_with_http_info(subscriber, **kwargs)  # noqa: E501
            return data

    def create_subscriber_using_post_with_http_info(self, subscriber, **kwargs):  # noqa: E501
        """createSubscriber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_subscriber_using_post_with_http_info(subscriber, async=True)
        >>> result = thread.get()

        :param async bool
        :param Subscriber subscriber: subscriber (required)
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscriber']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subscriber_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscriber' is set
        if ('subscriber' not in params or
                params['subscriber'] is None):
            raise ValueError("Missing the required parameter `subscriber` when calling `create_subscriber_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscriber' in params:
            body_params = params['subscriber']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/subscribers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscriber',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_subscriber_using_delete(self, id, **kwargs):  # noqa: E501
        """deleteSubscriber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_subscriber_using_delete(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_subscriber_using_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_subscriber_using_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_subscriber_using_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """deleteSubscriber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_subscriber_using_delete_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_subscriber_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_subscriber_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/subscribers/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_subscribers_using_get(self, **kwargs):  # noqa: E501
        """getAllSubscribers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_subscribers_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_subscribers_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_subscribers_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_subscribers_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getAllSubscribers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_subscribers_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_subscribers_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/subscribers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Subscriber]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subscriber_by_email_using_get(self, email, **kwargs):  # noqa: E501
        """getSubscriberByEmail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subscriber_by_email_using_get(email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str email: email (required)
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_subscriber_by_email_using_get_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.get_subscriber_by_email_using_get_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def get_subscriber_by_email_using_get_with_http_info(self, email, **kwargs):  # noqa: E501
        """getSubscriberByEmail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subscriber_by_email_using_get_with_http_info(email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str email: email (required)
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscriber_by_email_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `get_subscriber_by_email_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/subscribers/email/{email}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Subscriber]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subscriber_by_name_using_get(self, name, **kwargs):  # noqa: E501
        """getSubscriberByName  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subscriber_by_name_using_get(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_subscriber_by_name_using_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_subscriber_by_name_using_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_subscriber_by_name_using_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """getSubscriberByName  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subscriber_by_name_using_get_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscriber_by_name_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_subscriber_by_name_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/subscribers/name/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Subscriber]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subscriber_using_get(self, id, **kwargs):  # noqa: E501
        """getSubscriber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subscriber_using_get(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: id (required)
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_subscriber_using_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_subscriber_using_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_subscriber_using_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """getSubscriber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subscriber_using_get_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: id (required)
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscriber_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_subscriber_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/subscribers/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscriber',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_subscriber_using_put(self, subscriber, **kwargs):  # noqa: E501
        """updateSubscriber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_subscriber_using_put(subscriber, async=True)
        >>> result = thread.get()

        :param async bool
        :param Subscriber subscriber: subscriber (required)
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_subscriber_using_put_with_http_info(subscriber, **kwargs)  # noqa: E501
        else:
            (data) = self.update_subscriber_using_put_with_http_info(subscriber, **kwargs)  # noqa: E501
            return data

    def update_subscriber_using_put_with_http_info(self, subscriber, **kwargs):  # noqa: E501
        """updateSubscriber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_subscriber_using_put_with_http_info(subscriber, async=True)
        >>> result = thread.get()

        :param async bool
        :param Subscriber subscriber: subscriber (required)
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscriber']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_subscriber_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscriber' is set
        if ('subscriber' not in params or
                params['subscriber'] is None):
            raise ValueError("Missing the required parameter `subscriber` when calling `update_subscriber_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscriber' in params:
            body_params = params['subscriber']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/subscribers', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscriber',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)