# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import DataFactoryManagementClientConfiguration
from .operations import Operations
from .operations import FactoriesOperations
from .operations import ExposureControlOperations
from .operations import IntegrationRuntimesOperations
from .operations import IntegrationRuntimeObjectMetadataOperations
from .operations import IntegrationRuntimeNodesOperations
from .operations import LinkedServicesOperations
from .operations import DatasetsOperations
from .operations import PipelinesOperations
from .operations import PipelineRunsOperations
from .operations import ActivityRunsOperations
from .operations import TriggersOperations
from .operations import TriggerRunsOperations
from .operations import DataFlowsOperations
from .operations import DataFlowDebugSessionOperations
from .operations import ManagedVirtualNetworksOperations
from .operations import ManagedPrivateEndpointsOperations
from . import models


class DataFactoryManagementClient(object):
    """The Azure Data Factory V2 management API provides a RESTful set of web services that interact with Azure Data Factory V2 services.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datafactory.operations.Operations
    :ivar factories: FactoriesOperations operations
    :vartype factories: azure.mgmt.datafactory.operations.FactoriesOperations
    :ivar exposure_control: ExposureControlOperations operations
    :vartype exposure_control: azure.mgmt.datafactory.operations.ExposureControlOperations
    :ivar integration_runtimes: IntegrationRuntimesOperations operations
    :vartype integration_runtimes: azure.mgmt.datafactory.operations.IntegrationRuntimesOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadataOperations operations
    :vartype integration_runtime_object_metadata: azure.mgmt.datafactory.operations.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_nodes: IntegrationRuntimeNodesOperations operations
    :vartype integration_runtime_nodes: azure.mgmt.datafactory.operations.IntegrationRuntimeNodesOperations
    :ivar linked_services: LinkedServicesOperations operations
    :vartype linked_services: azure.mgmt.datafactory.operations.LinkedServicesOperations
    :ivar datasets: DatasetsOperations operations
    :vartype datasets: azure.mgmt.datafactory.operations.DatasetsOperations
    :ivar pipelines: PipelinesOperations operations
    :vartype pipelines: azure.mgmt.datafactory.operations.PipelinesOperations
    :ivar pipeline_runs: PipelineRunsOperations operations
    :vartype pipeline_runs: azure.mgmt.datafactory.operations.PipelineRunsOperations
    :ivar activity_runs: ActivityRunsOperations operations
    :vartype activity_runs: azure.mgmt.datafactory.operations.ActivityRunsOperations
    :ivar triggers: TriggersOperations operations
    :vartype triggers: azure.mgmt.datafactory.operations.TriggersOperations
    :ivar trigger_runs: TriggerRunsOperations operations
    :vartype trigger_runs: azure.mgmt.datafactory.operations.TriggerRunsOperations
    :ivar data_flows: DataFlowsOperations operations
    :vartype data_flows: azure.mgmt.datafactory.operations.DataFlowsOperations
    :ivar data_flow_debug_session: DataFlowDebugSessionOperations operations
    :vartype data_flow_debug_session: azure.mgmt.datafactory.operations.DataFlowDebugSessionOperations
    :ivar managed_virtual_networks: ManagedVirtualNetworksOperations operations
    :vartype managed_virtual_networks: azure.mgmt.datafactory.operations.ManagedVirtualNetworksOperations
    :ivar managed_private_endpoints: ManagedPrivateEndpointsOperations operations
    :vartype managed_private_endpoints: azure.mgmt.datafactory.operations.ManagedPrivateEndpointsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataFactoryManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.factories = FactoriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.exposure_control = ExposureControlOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_nodes = IntegrationRuntimeNodesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_services = LinkedServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.datasets = DatasetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipelines = PipelinesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_runs = PipelineRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.activity_runs = ActivityRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.triggers = TriggersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger_runs = TriggerRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flows = DataFlowsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow_debug_session = DataFlowDebugSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.managed_virtual_networks = ManagedVirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.managed_private_endpoints = ManagedPrivateEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DataFactoryManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
