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

class LifecycleRulesApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api213_lifecycle_rules_delete_with_http_info(
        self,
        bucket_ids=None,  # type: List[str]
        bucket_names=None,  # type: List[str]
        ids=None,  # type: List[str]
        names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """DELETE lifecycle-rules

        Deletes individual lifecycle rules by name or id, or deletes all rules for a bucket. If `ids` is specified, `bucket_names` or `bucket_ids` is also required. If `bucket_names` or `bucket_ids` are specified without `ids`, delete all the rules for the bucket.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_lifecycle_rules_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param list[str] bucket_ids: A comma-separated list of bucket IDs. If after filtering, there is not at least one resource that matches each of the elements of `bucket_ids`, then an error is returned. This cannot be provided together with the `bucket_names` query parameter. This can be provided with the `ids` query parameter but not with `names`.
        :param list[str] bucket_names: A comma-separated list of bucket names. If there is not at least one resource that matches each of the elements of `bucket_names`, then an error is returned. This cannot be provided together with the `bucket_ids` query parameter. This can be provided with the `ids` query parameter but not with `names`.
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
        if bucket_ids is not None:
            if not isinstance(bucket_ids, list):
                bucket_ids = [bucket_ids]
        if bucket_names is not None:
            if not isinstance(bucket_names, list):
                bucket_names = [bucket_names]
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
        if 'bucket_ids' in params:
            query_params.append(('bucket_ids', params['bucket_ids']))
            collection_formats['bucket_ids'] = 'csv'
        if 'bucket_names' in params:
            query_params.append(('bucket_names', params['bucket_names']))
            collection_formats['bucket_names'] = 'csv'
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
            '/api/2.13/lifecycle-rules', 'DELETE',
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

    def api213_lifecycle_rules_get_with_http_info(
        self,
        bucket_ids=None,  # type: List[str]
        bucket_names=None,  # type: List[str]
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
        # type: (...) -> models.LifecycleRuleGetResponse
        """GET lifecycle-rules

        Returns a list of lifecycle rules. If `names` is specified, list the individual rules. If `ids` is specified, `bucket_names` or `bucket_ids` is also required. If `bucket_names` or `bucket_ids` are specified without `ids`, list all the rules for the bucket.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_lifecycle_rules_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param list[str] bucket_ids: A comma-separated list of bucket IDs. If after filtering, there is not at least one resource that matches each of the elements of `bucket_ids`, then an error is returned. This cannot be provided together with the `bucket_names` query parameter. This can be provided with the `ids` query parameter but not with `names`.
        :param list[str] bucket_names: A comma-separated list of bucket names. If there is not at least one resource that matches each of the elements of `bucket_names`, then an error is returned. This cannot be provided together with the `bucket_ids` query parameter. This can be provided with the `ids` query parameter but not with `names`.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :param str filter: Exclude resources that don't match the specified criteria.
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned. This cannot be provided together with the `name` or `names` query parameters.
        :param int limit: Limit the size of the response to the specified number of resources. A `limit` of `0` can be used to get the number of resources without getting all of the resources. It will be returned in the `total_item_count` field. If a client asks for a page size larger than the available number, the request is still valid. In that case the server just returns the available number of items, disregarding the client's page size request.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). NOTE: If you provide a sort you will not get a `continuation_token` in the response.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: LifecycleRuleGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if bucket_ids is not None:
            if not isinstance(bucket_ids, list):
                bucket_ids = [bucket_ids]
        if bucket_names is not None:
            if not isinstance(bucket_names, list):
                bucket_names = [bucket_names]
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

        if 'limit' in params and params['limit'] < 0:
            raise ValueError("Invalid value for parameter `limit` when calling `api213_lifecycle_rules_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api213_lifecycle_rules_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'bucket_ids' in params:
            query_params.append(('bucket_ids', params['bucket_ids']))
            collection_formats['bucket_ids'] = 'csv'
        if 'bucket_names' in params:
            query_params.append(('bucket_names', params['bucket_names']))
            collection_formats['bucket_names'] = 'csv'
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
            '/api/2.13/lifecycle-rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LifecycleRuleGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api213_lifecycle_rules_patch_with_http_info(
        self,
        lifecycle=None,  # type: models.LifecycleRulePatch
        bucket_ids=None,  # type: List[str]
        bucket_names=None,  # type: List[str]
        ids=None,  # type: List[str]
        names=None,  # type: List[str]
        confirm_date=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.LifecycleRuleResponse
        """PATCH lifecycle-rules

        Modify an existing lifecycle rule by name or id. If `ids` is specified, `bucket_names` or `bucket_ids` is also required.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_lifecycle_rules_patch_with_http_info(lifecycle, async_req=True)
        >>> result = thread.get()

        :param LifecycleRulePatch lifecycle: (required)
        :param list[str] bucket_ids: A comma-separated list of bucket IDs. If after filtering, there is not at least one resource that matches each of the elements of `bucket_ids`, then an error is returned. This cannot be provided together with the `bucket_names` query parameter. This can be provided with the `ids` query parameter but not with `names`.
        :param list[str] bucket_names: A comma-separated list of bucket names. If there is not at least one resource that matches each of the elements of `bucket_names`, then an error is returned. This cannot be provided together with the `bucket_ids` query parameter. This can be provided with the `ids` query parameter but not with `names`.
        :param list[str] ids: A comma-separated list of resource IDs. If after filtering, there is not at least one resource that matches each of the elements of `ids`, then an error is returned. This cannot be provided together with the `name` or `names` query parameters.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of `names`, then an error is returned.
        :param bool confirm_date: If set to `true`, then confirm the date of `keep_current_version_until` is correct.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: LifecycleRuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if bucket_ids is not None:
            if not isinstance(bucket_ids, list):
                bucket_ids = [bucket_ids]
        if bucket_names is not None:
            if not isinstance(bucket_names, list):
                bucket_names = [bucket_names]
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
        # verify the required parameter 'lifecycle' is set
        if lifecycle is None:
            raise TypeError("Missing the required parameter `lifecycle` when calling `api213_lifecycle_rules_patch`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'bucket_ids' in params:
            query_params.append(('bucket_ids', params['bucket_ids']))
            collection_formats['bucket_ids'] = 'csv'
        if 'bucket_names' in params:
            query_params.append(('bucket_names', params['bucket_names']))
            collection_formats['bucket_names'] = 'csv'
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'confirm_date' in params:
            query_params.append(('confirm_date', params['confirm_date']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'lifecycle' in params:
            body_params = params['lifecycle']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.13/lifecycle-rules', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LifecycleRuleResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api213_lifecycle_rules_post_with_http_info(
        self,
        rule=None,  # type: models.LifecycleRulePost
        confirm_date=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.LifecycleRuleResponse
        """POST lifecycle-rules

        Creates a lifecycle rule. `bucket` and `keep_previous_version_for` are required. If `rule_id` is not specified, it will be automatically generated in the format \"fbRuleIdX\".
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api213_lifecycle_rules_post_with_http_info(rule, async_req=True)
        >>> result = thread.get()

        :param LifecycleRulePost rule: (required)
        :param bool confirm_date: If set to `true`, then confirm the date of `keep_current_version_until` is correct.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: LifecycleRuleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'rule' is set
        if rule is None:
            raise TypeError("Missing the required parameter `rule` when calling `api213_lifecycle_rules_post`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'confirm_date' in params:
            query_params.append(('confirm_date', params['confirm_date']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule' in params:
            body_params = params['rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/2.13/lifecycle-rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LifecycleRuleResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
