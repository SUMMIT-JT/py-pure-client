# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.14, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class UsageApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api214_usage_groups_get_with_http_info(
        self,
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        file_system_ids=None,  # type: List[str]
        file_system_names=None,  # type: List[str]
        filter=None,  # type: str
        gids=None,  # type: List[int]
        group_names=None,  # type: List[str]
        limit=None,  # type: int
        offset=None,  # type: int
        sort=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.GroupQuotaGetResponse
        """GET usage/groups

        List groups with hard limit quotas and their file system usage.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api214_usage_groups_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :param list[str] file_system_ids: A comma-separated list of file system IDs. If after filtering, there is not at least one resource that matches each of the elements of `file_system_ids`, then an error is returned. This cannot be provided together with the `file_system_names` query parameter.
        :param list[str] file_system_names: A comma-separated list of file system names. If there is not at least one resource that matches each of the elements of `file_system_names`, then an error is returned.
        :param str filter: Exclude resources that don't match the specified criteria.
        :param list[int] gids: A comma-separated list of group IDs. If there is not at least one resource that matches each of the elements of `gids`, then an error is returned. This cannot be provided together with `group_names` query parameter.
        :param list[str] group_names: A comma-separated list of group names. If there is not at least one resource that matches each of the elements of `group_names`, then an error is returned. This cannot be provided together with `gids` query parameter.
        :param int limit: Limit the size of the response to the specified number of resources. A `limit` of `0` can be used to get the number of resources without getting all of the resources. It will be returned in the `total_item_count` field. If a client asks for a page size larger than the available number, the request is still valid. In that case the server just returns the available number of items, disregarding the client's page size request.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: GroupQuotaGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if file_system_ids is not None:
            if not isinstance(file_system_ids, list):
                file_system_ids = [file_system_ids]
        if file_system_names is not None:
            if not isinstance(file_system_names, list):
                file_system_names = [file_system_names]
        if gids is not None:
            if not isinstance(gids, list):
                gids = [gids]
        if group_names is not None:
            if not isinstance(group_names, list):
                group_names = [group_names]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'limit' in params and params['limit'] < 0:
            raise ValueError("Invalid value for parameter `limit` when calling `api214_usage_groups_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api214_usage_groups_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'file_system_ids' in params:
            query_params.append(('file_system_ids', params['file_system_ids']))
            collection_formats['file_system_ids'] = 'csv'
        if 'file_system_names' in params:
            query_params.append(('file_system_names', params['file_system_names']))
            collection_formats['file_system_names'] = 'csv'
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'gids' in params:
            query_params.append(('gids', params['gids']))
            collection_formats['gids'] = 'csv'
        if 'group_names' in params:
            query_params.append(('group_names', params['group_names']))
            collection_formats['group_names'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.14/usage/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupQuotaGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api214_usage_users_get_with_http_info(
        self,
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        file_system_ids=None,  # type: List[str]
        file_system_names=None,  # type: List[str]
        filter=None,  # type: str
        limit=None,  # type: int
        offset=None,  # type: int
        sort=None,  # type: List[str]
        uids=None,  # type: List[int]
        user_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.UserQuotaGetResponse
        """GET usage/users

        List users with hard limit quotas and their file system usage.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api214_usage_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :param list[str] file_system_ids: A comma-separated list of file system IDs. If after filtering, there is not at least one resource that matches each of the elements of `file_system_ids`, then an error is returned. This cannot be provided together with the `file_system_names` query parameter.
        :param list[str] file_system_names: A comma-separated list of file system names. If there is not at least one resource that matches each of the elements of `file_system_names`, then an error is returned.
        :param str filter: Exclude resources that don't match the specified criteria.
        :param int limit: Limit the size of the response to the specified number of resources. A `limit` of `0` can be used to get the number of resources without getting all of the resources. It will be returned in the `total_item_count` field. If a client asks for a page size larger than the available number, the request is still valid. In that case the server just returns the available number of items, disregarding the client's page size request.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response.
        :param list[int] uids: A comma-separated list of user IDs. If there is not at least one resource that matches each of the elements of `uids`, then an error is returned. This cannot be provided together with `user_names` query parameter.
        :param list[str] user_names: A comma-separated list of user names. If there is not at least one resource that matches each of the elements of `user_names`, then an error is returned. This cannot be provided together with `uids` query parameter.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: UserQuotaGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if file_system_ids is not None:
            if not isinstance(file_system_ids, list):
                file_system_ids = [file_system_ids]
        if file_system_names is not None:
            if not isinstance(file_system_names, list):
                file_system_names = [file_system_names]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        if uids is not None:
            if not isinstance(uids, list):
                uids = [uids]
        if user_names is not None:
            if not isinstance(user_names, list):
                user_names = [user_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'limit' in params and params['limit'] < 0:
            raise ValueError("Invalid value for parameter `limit` when calling `api214_usage_users_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api214_usage_users_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'file_system_ids' in params:
            query_params.append(('file_system_ids', params['file_system_ids']))
            collection_formats['file_system_ids'] = 'csv'
        if 'file_system_names' in params:
            query_params.append(('file_system_names', params['file_system_names']))
            collection_formats['file_system_names'] = 'csv'
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'uids' in params:
            query_params.append(('uids', params['uids']))
            collection_formats['uids'] = 'csv'
        if 'user_names' in params:
            query_params.append(('user_names', params['user_names']))
            collection_formats['user_names'] = 'csv'

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.14/usage/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserQuotaGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
