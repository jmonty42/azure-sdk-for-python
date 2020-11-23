# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import OperationsManagementClientConfiguration
from .operations import SolutionsOperations
from .operations import ManagementAssociationsOperations
from .operations import ManagementConfigurationsOperations
from .operations import Operations
from .. import models


class OperationsManagementClient(object):
    """Operations Management Client.

    :ivar solutions: SolutionsOperations operations
    :vartype solutions: operations_management_client.aio.operations.SolutionsOperations
    :ivar management_associations: ManagementAssociationsOperations operations
    :vartype management_associations: operations_management_client.aio.operations.ManagementAssociationsOperations
    :ivar management_configurations: ManagementConfigurationsOperations operations
    :vartype management_configurations: operations_management_client.aio.operations.ManagementConfigurationsOperations
    :ivar operations: Operations operations
    :vartype operations: operations_management_client.aio.operations.Operations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param provider_name: Provider name for the parent resource.
    :type provider_name: str
    :param resource_type: Resource type for the parent resource.
    :type resource_type: str
    :param resource_name: Parent resource name.
    :type resource_name: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        provider_name: str,
        resource_type: str,
        resource_name: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = OperationsManagementClientConfiguration(credential, subscription_id, provider_name, resource_type, resource_name, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.solutions = SolutionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_associations = ManagementAssociationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_configurations = ManagementConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "OperationsManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
