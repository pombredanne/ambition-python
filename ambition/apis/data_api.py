#!/usr/bin/env python
# coding: utf-8

"""
DataApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
from __future__ import absolute_import

# python 2 and python 3 compatibility library
from six import iteritems

from . import AbstractBaseApi


class DataApi(AbstractBaseApi):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client

    def public_api_data_type_list(
        self,
        content_type=None,
        **kwargs
    ):
        """
        Returns a list of supported data types
        The Data API  <br/>Returns a list of supported data types
        :return: DepotDetailSerializer
        """
        all_params = [
        ]

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                error_message = "Got an unexpected keyword argument '%s' " \
                                "to method public_api_data_type_list" % key
                raise TypeError(error_message)
            params[key] = val
        del params['kwargs']

        resource_path = '/api/v1/data'.replace('{format}', 'json')
        method = 'GET'

        # path parameters
        allowed_params = [
        ]
        path_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        path_params = dict(path_param_items)
        # query parameters
        allowed_params = [
        ]
        query_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        query_params = dict(query_param_items)
        # headers
        allowed_params = [
        ]
        header_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        header_params = dict(header_param_items)
        # form parameters
        allowed_params = [
        ]
        form_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        form_params = dict(form_param_items)
        # files
        allowed_params = [
        ]
        file_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        files = dict(file_param_items)
        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        content_types = []
        if content_type is None or content_type not in content_types:
            content_type = self.api_client.select_header_content_type(content_types)
        header_params['Content-Type'] = content_type

        response = self.api_client.call_api(
            resource_path, method, path_params, query_params, header_params,
            body=body_params, post_params=form_params, files=files,
            response='DepotDetailSerializer')
        return response

    def public_api_data_type_retrieve(
        self,
        data_type,
        content_type=None,
        **kwargs
    ):
        """
        Returns a description of a data type and its schema
        The Data API  <br/>Returns a description of a data type and its schema
        :param str data_type: The id of the data type. Refer to the data types API for available types(required)
        :return: PublicApiDataTypeRetrieveResponse
        """
        all_params = [
            'data_type',
        ]

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                error_message = "Got an unexpected keyword argument '%s' " \
                                "to method public_api_data_type_retrieve" % key
                raise TypeError(error_message)
            params[key] = val
        del params['kwargs']

        resource_path = '/api/v1/data/{data_type}'.replace('{format}', 'json')
        method = 'GET'

        # path parameters
        allowed_params = [
            'data_type',
        ]
        path_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        path_params = dict(path_param_items)
        # query parameters
        allowed_params = [
        ]
        query_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        query_params = dict(query_param_items)
        # headers
        allowed_params = [
        ]
        header_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        header_params = dict(header_param_items)
        # form parameters
        allowed_params = [
        ]
        form_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        form_params = dict(form_param_items)
        # files
        allowed_params = [
        ]
        file_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        files = dict(file_param_items)
        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        content_types = []
        if content_type is None or content_type not in content_types:
            content_type = self.api_client.select_header_content_type(content_types)
        header_params['Content-Type'] = content_type

        response = self.api_client.call_api(
            resource_path, method, path_params, query_params, header_params,
            body=body_params, post_params=form_params, files=files,
            response='PublicApiDataTypeRetrieveResponse')
        return response

    def public_api_data_type_partial_update(
        self,
        data_type,
        content_type=None,
        **kwargs
    ):
        """
        Allows partial update of a data type configuration
        The Data API  <br/>Allows partial update of a data type configuration
        :param str data_type:(required)
        :param str integration_id:
        :param str display_name:
        :param str name:
        :return: DepotDetailSerializer
        """
        all_params = [
            'data_type',
            'integration_id',
            'display_name',
            'name',
        ]

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                error_message = "Got an unexpected keyword argument '%s' " \
                                "to method public_api_data_type_partial_update" % key
                raise TypeError(error_message)
            params[key] = val
        del params['kwargs']

        resource_path = '/api/v1/data/{data_type}'.replace('{format}', 'json')
        method = 'PATCH'

        # path parameters
        allowed_params = [
            'data_type',
        ]
        path_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        path_params = dict(path_param_items)
        # query parameters
        allowed_params = [
        ]
        query_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        query_params = dict(query_param_items)
        # headers
        allowed_params = [
        ]
        header_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        header_params = dict(header_param_items)
        # form parameters
        allowed_params = [
            'integration_id',
            'display_name',
            'name',
        ]
        form_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        form_params = dict(form_param_items)
        # files
        allowed_params = [
        ]
        file_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        files = dict(file_param_items)
        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        content_types = []
        if content_type is None or content_type not in content_types:
            content_type = self.api_client.select_header_content_type(content_types)
        header_params['Content-Type'] = content_type

        response = self.api_client.call_api(
            resource_path, method, path_params, query_params, header_params,
            body=body_params, post_params=form_params, files=files,
            response='DepotDetailSerializer')
        return response

    def public_api_data_create(
        self,
        data_type,
        body,
        content_type=None,
        **kwargs
    ):
        """
        Uploads a list of data objects
        The Data API  <br/>Uploads a list of data objects
        :param str data_type:(required)
        :param Serializer body: A list of data records.(required)
        :return: PublicApiDataCreateResponse
        """
        all_params = [
            'data_type',
            'body',
        ]

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                error_message = "Got an unexpected keyword argument '%s' " \
                                "to method public_api_data_create" % key
                raise TypeError(error_message)
            params[key] = val
        del params['kwargs']

        resource_path = '/api/v1/data/{data_type}/'.replace('{format}', 'json')
        method = 'POST'

        # path parameters
        allowed_params = [
            'data_type',
        ]
        path_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        path_params = dict(path_param_items)
        # query parameters
        allowed_params = [
        ]
        query_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        query_params = dict(query_param_items)
        # headers
        allowed_params = [
        ]
        header_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        header_params = dict(header_param_items)
        # form parameters
        allowed_params = [
        ]
        form_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        form_params = dict(form_param_items)
        # files
        allowed_params = [
        ]
        file_param_items = [
            item
            for item in params.items() if item[0] in allowed_params
        ]
        files = dict(file_param_items)
        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        content_types = ['application/json', 'text/csv', 'application/vnd.ms-excel']
        if content_type is None or content_type not in content_types:
            content_type = self.api_client.select_header_content_type(content_types)
        header_params['Content-Type'] = content_type

        response = self.api_client.call_api(
            resource_path, method, path_params, query_params, header_params,
            body=body_params, post_params=form_params, files=files,
            response='PublicApiDataCreateResponse')
        return response
