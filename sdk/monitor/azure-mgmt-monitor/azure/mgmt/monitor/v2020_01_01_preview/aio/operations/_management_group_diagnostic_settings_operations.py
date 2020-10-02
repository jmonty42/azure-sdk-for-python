# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ManagementGroupDiagnosticSettingsOperations:
    """ManagementGroupDiagnosticSettingsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~$(python-base-namespace).v2020_01_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        management_group_id: str,
        name: str,
        **kwargs
    ) -> "models.ManagementGroupDiagnosticSettingsResource":
        """Gets the active management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementGroupDiagnosticSettingsResource, or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ManagementGroupDiagnosticSettingsResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementGroupDiagnosticSettingsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}'}  # type: ignore

    async def create_or_update(
        self,
        management_group_id: str,
        name: str,
        parameters: "models.ManagementGroupDiagnosticSettingsResource",
        **kwargs
    ) -> "models.ManagementGroupDiagnosticSettingsResource":
        """Creates or updates management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :param parameters: Parameters supplied to the operation.
        :type parameters: ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagementGroupDiagnosticSettingsResource, or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ManagementGroupDiagnosticSettingsResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'ManagementGroupDiagnosticSettingsResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagementGroupDiagnosticSettingsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}'}  # type: ignore

    async def delete(
        self,
        management_group_id: str,
        name: str,
        **kwargs
    ) -> None:
        """Deletes existing management group diagnostic settings for the specified resource.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :param name: The name of the diagnostic setting.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings/{name}'}  # type: ignore

    def list(
        self,
        management_group_id: str,
        **kwargs
    ) -> AsyncIterable["models.ManagementGroupDiagnosticSettingsResourceCollection"]:
        """Gets the active management group diagnostic settings list for the specified management group.

        :param management_group_id: The management group id.
        :type management_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ManagementGroupDiagnosticSettingsResourceCollection or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~$(python-base-namespace).v2020_01_01_preview.models.ManagementGroupDiagnosticSettingsResourceCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ManagementGroupDiagnosticSettingsResourceCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ManagementGroupDiagnosticSettingsResourceCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/providers/microsoft.management/managementGroups/{managementGroupId}/providers/microsoft.insights/diagnosticSettings'}  # type: ignore
