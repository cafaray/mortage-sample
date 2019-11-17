# coding: utf-8

"""
    Employees API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@apigee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def employee_uuid_delete(self, employee_uuid, **kwargs):  # noqa: E501
        """Delete an Employee with given UUID  # noqa: E501

        This endpoint will delete an existing Employee.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_uuid_delete(employee_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_uuid: UUID of a Employee (required)
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employee_uuid_delete_with_http_info(employee_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.employee_uuid_delete_with_http_info(employee_uuid, **kwargs)  # noqa: E501
            return data

    def employee_uuid_delete_with_http_info(self, employee_uuid, **kwargs):  # noqa: E501
        """Delete an Employee with given UUID  # noqa: E501

        This endpoint will delete an existing Employee.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_uuid_delete_with_http_info(employee_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_uuid: UUID of a Employee (required)
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['employee_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employee_uuid_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'employee_uuid' is set
        if ('employee_uuid' not in params or
                params['employee_uuid'] is None):
            raise ValueError("Missing the required parameter `employee_uuid` when calling `employee_uuid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'employee_uuid' in params:
            path_params['employee-uuid'] = params['employee_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{employee-uuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Employee',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def employee_uuid_get(self, employee_uuid, **kwargs):  # noqa: E501
        """Get an Employee with given UUID.  # noqa: E501

        This endpoint returns a Employee from a given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_uuid_get(employee_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_uuid: UUID of a Employee (required)
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employee_uuid_get_with_http_info(employee_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.employee_uuid_get_with_http_info(employee_uuid, **kwargs)  # noqa: E501
            return data

    def employee_uuid_get_with_http_info(self, employee_uuid, **kwargs):  # noqa: E501
        """Get an Employee with given UUID.  # noqa: E501

        This endpoint returns a Employee from a given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_uuid_get_with_http_info(employee_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_uuid: UUID of a Employee (required)
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['employee_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employee_uuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'employee_uuid' is set
        if ('employee_uuid' not in params or
                params['employee_uuid'] is None):
            raise ValueError("Missing the required parameter `employee_uuid` when calling `employee_uuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'employee_uuid' in params:
            path_params['employee-uuid'] = params['employee_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{employee-uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Employee',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def employee_uuid_put(self, employee_uuid, body, **kwargs):  # noqa: E501
        """Update an Employee with given UUID  # noqa: E501

        This endpoint will update an existing Employee.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_uuid_put(employee_uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_uuid: UUID of a Employee (required)
        :param Employee body: an Employee oject (required)
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employee_uuid_put_with_http_info(employee_uuid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.employee_uuid_put_with_http_info(employee_uuid, body, **kwargs)  # noqa: E501
            return data

    def employee_uuid_put_with_http_info(self, employee_uuid, body, **kwargs):  # noqa: E501
        """Update an Employee with given UUID  # noqa: E501

        This endpoint will update an existing Employee.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_uuid_put_with_http_info(employee_uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_uuid: UUID of a Employee (required)
        :param Employee body: an Employee oject (required)
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['employee_uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employee_uuid_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'employee_uuid' is set
        if ('employee_uuid' not in params or
                params['employee_uuid'] is None):
            raise ValueError("Missing the required parameter `employee_uuid` when calling `employee_uuid_put`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `employee_uuid_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'employee_uuid' in params:
            path_params['employee-uuid'] = params['employee_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{employee-uuid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Employee',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def root_get(self, **kwargs):  # noqa: E501
        """Get all Employees  # noqa: E501

        This endpoint returns a list of all Employees as an array.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: EmployeesArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.root_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.root_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def root_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all Employees  # noqa: E501

        This endpoint returns a list of all Employees as an array.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: EmployeesArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method root_get" % key
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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmployeesArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def root_post(self, body, **kwargs):  # noqa: E501
        """Create a new Employee  # noqa: E501

        This endpoint will create a new Employee.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Employee body: an Employee oject (required)
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.root_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.root_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def root_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new Employee  # noqa: E501

        This endpoint will create a new Employee.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Employee body: an Employee oject (required)
        :return: Employee
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method root_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `root_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Employee',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
