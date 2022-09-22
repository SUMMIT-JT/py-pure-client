# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.6, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
from typing import List, Optional

from .. import models

class PoliciesAllApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api26_policies_all_get_with_http_info(
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
        # type: (...) -> models.PolicyBaseGetResponse
        """GET policies-all

        List all policies of all types.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api26_policies_all_get_with_http_info(async_req=True)
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
        :return: PolicyBaseGetResponse
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

        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `api26_policies_all_get`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api26_policies_all_get`, must be a value greater than or equal to `0`")
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
            '/api/2.6/policies-all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyBaseGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api26_policies_all_members_get_with_http_info(
        self,
        continuation_token=None,  # type: str
        filter=None,  # type: str
        limit=None,  # type: int
        local_file_system_ids=None,  # type: List[str]
        local_file_system_names=None,  # type: List[str]
        member_ids=None,  # type: List[str]
        member_names=None,  # type: List[str]
        member_types=None,  # type: List[models.ModelsFB26ResourceTypeYaml]
        offset=None,  # type: int
        policy_ids=None,  # type: List[str]
        policy_names=None,  # type: List[str]
        remote_ids=None,  # type: List[str]
        remote_file_system_ids=None,  # type: List[str]
        remote_file_system_names=None,  # type: List[str]
        remote_names=None,  # type: List[str]
        sort=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.PolicyMemberWithRemoteGetResponse
        """GET policies-all/members

        List policies (of all types) mapped to other entities (file systems, snapshots, file system replica links, and object store users).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api26_policies_all_members_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :param str filter: Exclude resources that don't match the specified criteria.
        :param int limit: Limit the size of the response to the specified number of resources. A `limit` of `0` can be used to get the number of resources without getting all of the resources. It will be returned in the `total_item_count` field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request.
        :param list[str] local_file_system_ids: A comma-separated list of local file system IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `local_file_system_names` query parameter.
        :param list[str] local_file_system_names: A comma-separated list of local file system names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `local_file_system_ids` query parameter.
        :param list[str] member_ids: A comma-separated list of member IDs. If after filtering, there is not at least one resource that matches each of the elements of `member_ids`, then an error is returned. This cannot be provided together with the `member_names` query parameter.
        :param list[str] member_names: A comma-separated list of member names.
        :param list[ModelsFB26ResourceTypeYaml] member_types: A comma-separated list of member types. Valid values are `file-systems`, `file-system-snapshots`, `file-system-replica-links`, and `object-store-users`. Different endpoints may accept different subsets of these values.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] policy_ids: A comma-separated list of policy IDs. If after filtering, there is not at least one resource that matches each of the elements of `policy_ids`, then an error is returned. This cannot be provided together with the `policy_names` query parameter.
        :param list[str] policy_names: A comma-separated list of policy names.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. If after filtering, there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_file_system_ids: A comma-separated list of remote file system IDs. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `remote_file_system_names` query parameter.
        :param list[str] remote_file_system_names: A comma-separated list of remote file system names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with the `remote_file_system_ids` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. If there is not at least one resource that matches each of the elements, then an error is returned. This cannot be provided together with `remote_ids` query parameter.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: PolicyMemberWithRemoteGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if local_file_system_ids is not None:
            if not isinstance(local_file_system_ids, list):
                local_file_system_ids = [local_file_system_ids]
        if local_file_system_names is not None:
            if not isinstance(local_file_system_names, list):
                local_file_system_names = [local_file_system_names]
        if member_ids is not None:
            if not isinstance(member_ids, list):
                member_ids = [member_ids]
        if member_names is not None:
            if not isinstance(member_names, list):
                member_names = [member_names]
        if member_types is not None:
            if not isinstance(member_types, list):
                member_types = [member_types]
        if policy_ids is not None:
            if not isinstance(policy_ids, list):
                policy_ids = [policy_ids]
        if policy_names is not None:
            if not isinstance(policy_names, list):
                policy_names = [policy_names]
        if remote_ids is not None:
            if not isinstance(remote_ids, list):
                remote_ids = [remote_ids]
        if remote_file_system_ids is not None:
            if not isinstance(remote_file_system_ids, list):
                remote_file_system_ids = [remote_file_system_ids]
        if remote_file_system_names is not None:
            if not isinstance(remote_file_system_names, list):
                remote_file_system_names = [remote_file_system_names]
        if remote_names is not None:
            if not isinstance(remote_names, list):
                remote_names = [remote_names]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]

        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `api26_policies_all_members_get`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api26_policies_all_members_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'local_file_system_ids' in params:
            query_params.append(('local_file_system_ids', params['local_file_system_ids']))
            collection_formats['local_file_system_ids'] = 'csv'
        if 'local_file_system_names' in params:
            query_params.append(('local_file_system_names', params['local_file_system_names']))
            collection_formats['local_file_system_names'] = 'csv'
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))
            collection_formats['member_ids'] = 'csv'
        if 'member_names' in params:
            query_params.append(('member_names', params['member_names']))
            collection_formats['member_names'] = 'csv'
        if 'member_types' in params:
            query_params.append(('member_types', params['member_types']))
            collection_formats['member_types'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'
        if 'remote_ids' in params:
            query_params.append(('remote_ids', params['remote_ids']))
            collection_formats['remote_ids'] = 'csv'
        if 'remote_file_system_ids' in params:
            query_params.append(('remote_file_system_ids', params['remote_file_system_ids']))
            collection_formats['remote_file_system_ids'] = 'csv'
        if 'remote_file_system_names' in params:
            query_params.append(('remote_file_system_names', params['remote_file_system_names']))
            collection_formats['remote_file_system_names'] = 'csv'
        if 'remote_names' in params:
            query_params.append(('remote_names', params['remote_names']))
            collection_formats['remote_names'] = 'csv'
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
            '/api/2.6/policies-all/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PolicyMemberWithRemoteGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
