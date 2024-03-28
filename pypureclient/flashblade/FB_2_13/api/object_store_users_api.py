# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.13, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class ObjectStoreUsersApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api213_object_store_users_delete_with_http_info(
        self,
        ids=None,  # type: List[str]
        names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """DELETE object-store-users

        Delete an object store user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_object_store_users_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned. This cannot be provided together with the `name` or `names` query parameters.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}

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
            '/api/2.13/object-store-users', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api213_object_store_users_get_with_http_info(
        self,
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        names=None,  # type: List[str]
        offset=None,  # type: int
        sort=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.ObjectStoreUserGetResponse
        """GET object-store-users

        List object store users and their attributes.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_object_store_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :param str filter: Exclude resources that don't match the specified criteria.
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned. This cannot be provided together with the `name` or `names` query parameters.
        :param int limit: Limit the size of the response to the specified number of resources. A `limit` of `0` can be used to get the number of resources without getting all of the resources. It will be returned in the `total_item_count` field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: ObjectStoreUserGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if names is not None:
            if not isinstance(names, list):
                names = [names]
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

        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `api213_object_store_users_get`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api213_object_store_users_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}

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
            '/api/2.13/object-store-users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectStoreUserGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api213_object_store_users_object_store_access_policies_delete_with_http_info(
        self,
        member_ids=None,  # type: List[str]
        member_names=None,  # type: List[str]
        policy_ids=None,  # type: List[str]
        policy_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """DELETE object-store-users/object-store-access-policies

        Revoke an object store user’s access policy.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_object_store_users_object_store_access_policies_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param list[str] member_ids: A comma-separated list of member IDs. If after filtering, there is not at least one resource that matches each of the elements of `member_ids`, then an error is returned. This cannot be provided together with the `member_names` query parameter.
        :param list[str] member_names: A comma-separated list of member names.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If after filtering, there is not at least one resource that matches each of the elements of `policy_ids`, then an error is returned. This cannot be provided together with the `policy_names` query parameter.
        :param list[str] policy_names: A comma-separated list of policy names.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if member_ids is not None:
            if not isinstance(member_ids, list):
                member_ids = [member_ids]
        if member_names is not None:
            if not isinstance(member_names, list):
                member_names = [member_names]
        if policy_ids is not None:
            if not isinstance(policy_ids, list):
                policy_ids = [policy_ids]
        if policy_names is not None:
            if not isinstance(policy_names, list):
                policy_names = [policy_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))
            collection_formats['member_ids'] = 'csv'
        if 'member_names' in params:
            query_params.append(('member_names', params['member_names']))
            collection_formats['member_names'] = 'csv'
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'

        header_params = {}

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
            '/api/2.13/object-store-users/object-store-access-policies', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api213_object_store_users_object_store_access_policies_get_with_http_info(
        self,
        continuation_token=None,  # type: str
        filter=None,  # type: str
        limit=None,  # type: int
        member_ids=None,  # type: List[str]
        member_names=None,  # type: List[str]
        offset=None,  # type: int
        policy_ids=None,  # type: List[str]
        policy_names=None,  # type: List[str]
        sort=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.PolicyMemberGetResponse
        """GET object-store-users/object-store-access-policies

        List object store users and their access policies.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_object_store_users_object_store_access_policies_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :param str filter: Exclude resources that don't match the specified criteria.
        :param int limit: Limit the size of the response to the specified number of resources. A `limit` of `0` can be used to get the number of resources without getting all of the resources. It will be returned in the `total_item_count` field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request.
        :param list[str] member_ids: A comma-separated list of member IDs. If after filtering, there is not at least one resource that matches each of the elements of `member_ids`, then an error is returned. This cannot be provided together with the `member_names` query parameter.
        :param list[str] member_names: A comma-separated list of member names.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If after filtering, there is not at least one resource that matches each of the elements of `policy_ids`, then an error is returned. This cannot be provided together with the `policy_names` query parameter.
        :param list[str] policy_names: A comma-separated list of policy names.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: PolicyMemberGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if member_ids is not None:
            if not isinstance(member_ids, list):
                member_ids = [member_ids]
        if member_names is not None:
            if not isinstance(member_names, list):
                member_names = [member_names]
        if policy_ids is not None:
            if not isinstance(policy_ids, list):
                policy_ids = [policy_ids]
        if policy_names is not None:
            if not isinstance(policy_names, list):
                policy_names = [policy_names]
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

        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `api213_object_store_users_object_store_access_policies_get`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api213_object_store_users_object_store_access_policies_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))
            collection_formats['member_ids'] = 'csv'
        if 'member_names' in params:
            query_params.append(('member_names', params['member_names']))
            collection_formats['member_names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}

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
            '/api/2.13/object-store-users/object-store-access-policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyMemberGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api213_object_store_users_object_store_access_policies_post_with_http_info(
        self,
        member_ids=None,  # type: List[str]
        member_names=None,  # type: List[str]
        policy_ids=None,  # type: List[str]
        policy_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.PolicyMemberResponse
        """POST object-store-users/object-store-access-policies

        Grant access policies to an object store user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_object_store_users_object_store_access_policies_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param list[str] member_ids: A comma-separated list of member IDs. If after filtering, there is not at least one resource that matches each of the elements of `member_ids`, then an error is returned. This cannot be provided together with the `member_names` query parameter.
        :param list[str] member_names: A comma-separated list of member names.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If after filtering, there is not at least one resource that matches each of the elements of `policy_ids`, then an error is returned. This cannot be provided together with the `policy_names` query parameter.
        :param list[str] policy_names: A comma-separated list of policy names.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: PolicyMemberResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if member_ids is not None:
            if not isinstance(member_ids, list):
                member_ids = [member_ids]
        if member_names is not None:
            if not isinstance(member_names, list):
                member_names = [member_names]
        if policy_ids is not None:
            if not isinstance(policy_ids, list):
                policy_ids = [policy_ids]
        if policy_names is not None:
            if not isinstance(policy_names, list):
                policy_names = [policy_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))
            collection_formats['member_ids'] = 'csv'
        if 'member_names' in params:
            query_params.append(('member_names', params['member_names']))
            collection_formats['member_names'] = 'csv'
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'

        header_params = {}

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
            '/api/2.13/object-store-users/object-store-access-policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyMemberResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api213_object_store_users_post_with_http_info(
        self,
        names=None,  # type: List[str]
        full_access=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.ObjectStoreUserResponse
        """POST object-store-users

        Create object store users to administer object storage for an object store account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_object_store_users_post_with_http_info(names, async_req=True)
        >>> result = thread.get()

        :param list[str] names: A comma-separated list of resource names. (required)
        :param bool full_access: If set to `true`, creates an object store user with full permissions. If set to `false`, creates an object store user with no permission. If not specified, defaults to `false`.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: ObjectStoreUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'names' is set
        if names is None:
            raise TypeError("Missing the required parameter `names` when calling `api213_object_store_users_post`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'full_access' in params:
            query_params.append(('full_access', params['full_access']))

        header_params = {}

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
            '/api/2.13/object-store-users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectStoreUserResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
