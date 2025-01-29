# coding: utf-8

"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](https://www.purestorage.com)  The Pure1 REST API 2.0 offers one single form of authentication: OAuth 2.0 via the [Token Exchange protocol](https://datatracker.ietf.org/doc/draft-ietf-oauth-token-exchange).  OAuth 2.0 is an open protocol to allow secure authorization in a simple and standard method from web, mobile, desktop and background applications.  Note that the [Authentication](#section/Authentication) section below mentions 'API Key' as the security scheme type. This is solely for the purpose of allowing testing this API with [Swagger UI](https://static.pure1.purestorage.com/api-swagger/index.html).  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class ArraysApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api11_arrays_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        fqdns=None,  # type: List[str]
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
        # type: (...) -> models.ArrayGetResponse
        """Get arrays

        Retrieves information about FlashArray and FlashBlade storage appliances. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api11_arrays_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] fqdns: A comma-separated list of resource FQDNs. If there is not at least one resource that matches each `fqdn` element, an error is returned. Single quotes are required around all strings.
        :param list[str] ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each `id` element, an error is returned. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each `name` element, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: ArrayGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        continuation_token = models.quoteString(continuation_token)
        if fqdns is not None:
            if not isinstance(fqdns, list):
                fqdns = [fqdns]
        fqdns = models.quoteStrings(fqdns)
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        ids = models.quoteStrings(ids)
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        names = models.quoteStrings(names)
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

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api11_arrays_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'fqdns' in params:
            query_params.append(('fqdns', params['fqdns']))
            collection_formats['fqdns'] = 'csv'
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
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
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
            '/api/1.1/arrays', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArrayGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api11_arrays_support_contracts_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        limit=None,  # type: int
        offset=None,  # type: int
        resource_ids=None,  # type: List[str]
        resource_fqdns=None,  # type: List[str]
        resource_names=None,  # type: List[str]
        sort=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.SupportContractGetResponse
        """Get array support contracts

        Retrieves the support contracts associated with arrays. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api11_arrays_support_contracts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] resource_ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each `resource_id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] resource_fqdns: A comma-separated list of resource FQDNs. If there is not at least one resource that matches each `resource_fqdn` element, an error is returned. Single quotes are required around all strings.
        :param list[str] resource_names: A comma-separated list of resource names. If there is not at least one resource that matches each `resource_name` element, an error is returned. Single quotes are required around all strings.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: SupportContractGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        continuation_token = models.quoteString(continuation_token)
        if resource_ids is not None:
            if not isinstance(resource_ids, list):
                resource_ids = [resource_ids]
        resource_ids = models.quoteStrings(resource_ids)
        if resource_fqdns is not None:
            if not isinstance(resource_fqdns, list):
                resource_fqdns = [resource_fqdns]
        resource_fqdns = models.quoteStrings(resource_fqdns)
        if resource_names is not None:
            if not isinstance(resource_names, list):
                resource_names = [resource_names]
        resource_names = models.quoteStrings(resource_names)
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

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api11_arrays_support_contracts_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'resource_ids' in params:
            query_params.append(('resource_ids', params['resource_ids']))
            collection_formats['resource_ids'] = 'csv'
        if 'resource_fqdns' in params:
            query_params.append(('resource_fqdns', params['resource_fqdns']))
            collection_formats['resource_fqdns'] = 'csv'
        if 'resource_names' in params:
            query_params.append(('resource_names', params['resource_names']))
            collection_formats['resource_names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
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
            '/api/1.1/arrays/support-contracts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SupportContractGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api11_arrays_tags_batch_put_with_http_info(
        self,
        tag=None,  # type: List[models.TagPut]
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        namespaces=None,  # type: List[str]
        resource_ids=None,  # type: List[str]
        resource_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.TagResponse
        """Create or update array tags 

        Creates or updates array tags contextual to Pure1 only. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api11_arrays_tags_batch_put_with_http_info(tag, async_req=True)
        >>> result = thread.get()

        :param list[TagPut] tag: A list of tags to be upserted. (required)
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param list[str] namespaces: A comma-separated list of namespaces. Single quotes are required around all strings.
        :param list[str] resource_ids: REQUIRED: either `resource_ids` or `resource_names`. A comma-separated list of resource IDs. If there is not at least one resource that matches each `resource_id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] resource_names: REQUIRED: either `resource_ids` or `resource_names`. A comma-separated list of resource names. If there is not at least one resource that matches each `resource_name` element, an error is returned. Single quotes are required around all strings.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: TagResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if tag is not None:
            if not isinstance(tag, list):
                tag = [tag]
        if namespaces is not None:
            if not isinstance(namespaces, list):
                namespaces = [namespaces]
        namespaces = models.quoteStrings(namespaces)
        if resource_ids is not None:
            if not isinstance(resource_ids, list):
                resource_ids = [resource_ids]
        resource_ids = models.quoteStrings(resource_ids)
        if resource_names is not None:
            if not isinstance(resource_names, list):
                resource_names = [resource_names]
        resource_names = models.quoteStrings(resource_names)
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'tag' is set
        if tag is None:
            raise TypeError("Missing the required parameter `tag` when calling `api11_arrays_tags_batch_put`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'namespaces' in params:
            query_params.append(('namespaces', params['namespaces']))
            collection_formats['namespaces'] = 'csv'
        if 'resource_ids' in params:
            query_params.append(('resource_ids', params['resource_ids']))
            collection_formats['resource_ids'] = 'csv'
        if 'resource_names' in params:
            query_params.append(('resource_names', params['resource_names']))
            collection_formats['resource_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag' in params:
            body_params = params['tag']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.1/arrays/tags/batch', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api11_arrays_tags_delete_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        keys=None,  # type: List[str]
        namespaces=None,  # type: List[str]
        resource_ids=None,  # type: List[str]
        resource_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """Delete array tags

        Deletes array tags from Pure1. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api11_arrays_tags_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param list[str] keys: A comma-separated list of tag keys. Single quotes are required around all strings.
        :param list[str] namespaces: A comma-separated list of namespaces. Single quotes are required around all strings.
        :param list[str] resource_ids: REQUIRED: either `resource_ids` or `resource_names`. A comma-separated list of resource IDs. If there is not at least one resource that matches each `resource_id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] resource_names: REQUIRED: either `resource_ids` or `resource_names`. A comma-separated list of resource names. If there is not at least one resource that matches each `resource_name` element, an error is returned. Single quotes are required around all strings.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if keys is not None:
            if not isinstance(keys, list):
                keys = [keys]
        keys = models.quoteStrings(keys)
        if namespaces is not None:
            if not isinstance(namespaces, list):
                namespaces = [namespaces]
        namespaces = models.quoteStrings(namespaces)
        if resource_ids is not None:
            if not isinstance(resource_ids, list):
                resource_ids = [resource_ids]
        resource_ids = models.quoteStrings(resource_ids)
        if resource_names is not None:
            if not isinstance(resource_names, list):
                resource_names = [resource_names]
        resource_names = models.quoteStrings(resource_names)
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
        if 'keys' in params:
            query_params.append(('keys', params['keys']))
            collection_formats['keys'] = 'csv'
        if 'namespaces' in params:
            query_params.append(('namespaces', params['namespaces']))
            collection_formats['namespaces'] = 'csv'
        if 'resource_ids' in params:
            query_params.append(('resource_ids', params['resource_ids']))
            collection_formats['resource_ids'] = 'csv'
        if 'resource_names' in params:
            query_params.append(('resource_names', params['resource_names']))
            collection_formats['resource_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
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
            '/api/1.1/arrays/tags', 'DELETE',
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

    def api11_arrays_tags_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        keys=None,  # type: List[str]
        limit=None,  # type: int
        namespaces=None,  # type: List[str]
        offset=None,  # type: int
        resource_ids=None,  # type: List[str]
        resource_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.TagGetResponse
        """Get array tags

        Retrieves the tags associated with specified arrays. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api11_arrays_tags_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] keys: A comma-separated list of tag keys. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] namespaces: A comma-separated list of namespaces. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] resource_ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each `resource_id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] resource_names: A comma-separated list of resource names. If there is not at least one resource that matches each `resource_name` element, an error is returned. Single quotes are required around all strings.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: TagGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        continuation_token = models.quoteString(continuation_token)
        if keys is not None:
            if not isinstance(keys, list):
                keys = [keys]
        keys = models.quoteStrings(keys)
        if namespaces is not None:
            if not isinstance(namespaces, list):
                namespaces = [namespaces]
        namespaces = models.quoteStrings(namespaces)
        if resource_ids is not None:
            if not isinstance(resource_ids, list):
                resource_ids = [resource_ids]
        resource_ids = models.quoteStrings(resource_ids)
        if resource_names is not None:
            if not isinstance(resource_names, list):
                resource_names = [resource_names]
        resource_names = models.quoteStrings(resource_names)
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api11_arrays_tags_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'keys' in params:
            query_params.append(('keys', params['keys']))
            collection_formats['keys'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'namespaces' in params:
            query_params.append(('namespaces', params['namespaces']))
            collection_formats['namespaces'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'resource_ids' in params:
            query_params.append(('resource_ids', params['resource_ids']))
            collection_formats['resource_ids'] = 'csv'
        if 'resource_names' in params:
            query_params.append(('resource_names', params['resource_names']))
            collection_formats['resource_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
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
            '/api/1.1/arrays/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
