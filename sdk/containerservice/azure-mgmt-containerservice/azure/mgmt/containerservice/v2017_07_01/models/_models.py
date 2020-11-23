# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class Resource(msrest.serialization.Model):
    """The Resource model definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs['location']
        self.tags = kwargs.get('tags', None)


class ContainerService(Resource):
    """Container service.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :ivar provisioning_state: The current deployment or provisioning state, which only appears in
     the response.
    :vartype provisioning_state: str
    :param orchestrator_profile: Profile for the container service orchestrator.
    :type orchestrator_profile:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceOrchestratorProfile
    :param custom_profile: Properties to configure a custom container service cluster.
    :type custom_profile:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceCustomProfile
    :param service_principal_profile: Information about a service principal identity for the
     cluster to use for manipulating Azure APIs. Exact one of secret or keyVaultSecretRef need to be
     specified.
    :type service_principal_profile:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServicePrincipalProfile
    :param master_profile: Profile for the container service master.
    :type master_profile:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceMasterProfile
    :param agent_pool_profiles: Properties of the agent pool.
    :type agent_pool_profiles:
     list[~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceAgentPoolProfile]
    :param windows_profile: Profile for Windows VMs in the container service cluster.
    :type windows_profile:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceWindowsProfile
    :param linux_profile: Profile for Linux VMs in the container service cluster.
    :type linux_profile:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceLinuxProfile
    :param diagnostics_profile: Profile for diagnostics in the container service cluster.
    :type diagnostics_profile:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceDiagnosticsProfile
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'orchestrator_profile': {'key': 'properties.orchestratorProfile', 'type': 'ContainerServiceOrchestratorProfile'},
        'custom_profile': {'key': 'properties.customProfile', 'type': 'ContainerServiceCustomProfile'},
        'service_principal_profile': {'key': 'properties.servicePrincipalProfile', 'type': 'ContainerServicePrincipalProfile'},
        'master_profile': {'key': 'properties.masterProfile', 'type': 'ContainerServiceMasterProfile'},
        'agent_pool_profiles': {'key': 'properties.agentPoolProfiles', 'type': '[ContainerServiceAgentPoolProfile]'},
        'windows_profile': {'key': 'properties.windowsProfile', 'type': 'ContainerServiceWindowsProfile'},
        'linux_profile': {'key': 'properties.linuxProfile', 'type': 'ContainerServiceLinuxProfile'},
        'diagnostics_profile': {'key': 'properties.diagnosticsProfile', 'type': 'ContainerServiceDiagnosticsProfile'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerService, self).__init__(**kwargs)
        self.provisioning_state = None
        self.orchestrator_profile = kwargs.get('orchestrator_profile', None)
        self.custom_profile = kwargs.get('custom_profile', None)
        self.service_principal_profile = kwargs.get('service_principal_profile', None)
        self.master_profile = kwargs.get('master_profile', None)
        self.agent_pool_profiles = kwargs.get('agent_pool_profiles', None)
        self.windows_profile = kwargs.get('windows_profile', None)
        self.linux_profile = kwargs.get('linux_profile', None)
        self.diagnostics_profile = kwargs.get('diagnostics_profile', None)


class ContainerServiceAgentPoolProfile(msrest.serialization.Model):
    """Profile for the container service agent pool.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Unique name of the agent pool profile in the context of the subscription
     and resource group.
    :type name: str
    :param count: Number of agents (VMs) to host docker containers. Allowed values must be in the
     range of 1 to 100 (inclusive). The default value is 1.
    :type count: int
    :param vm_size: Required. Size of agent VMs. Possible values include: "Standard_A1",
     "Standard_A10", "Standard_A11", "Standard_A1_v2", "Standard_A2", "Standard_A2_v2",
     "Standard_A2m_v2", "Standard_A3", "Standard_A4", "Standard_A4_v2", "Standard_A4m_v2",
     "Standard_A5", "Standard_A6", "Standard_A7", "Standard_A8", "Standard_A8_v2",
     "Standard_A8m_v2", "Standard_A9", "Standard_B2ms", "Standard_B2s", "Standard_B4ms",
     "Standard_B8ms", "Standard_D1", "Standard_D11", "Standard_D11_v2", "Standard_D11_v2_Promo",
     "Standard_D12", "Standard_D12_v2", "Standard_D12_v2_Promo", "Standard_D13", "Standard_D13_v2",
     "Standard_D13_v2_Promo", "Standard_D14", "Standard_D14_v2", "Standard_D14_v2_Promo",
     "Standard_D15_v2", "Standard_D16_v3", "Standard_D16s_v3", "Standard_D1_v2", "Standard_D2",
     "Standard_D2_v2", "Standard_D2_v2_Promo", "Standard_D2_v3", "Standard_D2s_v3", "Standard_D3",
     "Standard_D32_v3", "Standard_D32s_v3", "Standard_D3_v2", "Standard_D3_v2_Promo", "Standard_D4",
     "Standard_D4_v2", "Standard_D4_v2_Promo", "Standard_D4_v3", "Standard_D4s_v3",
     "Standard_D5_v2", "Standard_D5_v2_Promo", "Standard_D64_v3", "Standard_D64s_v3",
     "Standard_D8_v3", "Standard_D8s_v3", "Standard_DS1", "Standard_DS11", "Standard_DS11_v2",
     "Standard_DS11_v2_Promo", "Standard_DS12", "Standard_DS12_v2", "Standard_DS12_v2_Promo",
     "Standard_DS13", "Standard_DS13-2_v2", "Standard_DS13-4_v2", "Standard_DS13_v2",
     "Standard_DS13_v2_Promo", "Standard_DS14", "Standard_DS14-4_v2", "Standard_DS14-8_v2",
     "Standard_DS14_v2", "Standard_DS14_v2_Promo", "Standard_DS15_v2", "Standard_DS1_v2",
     "Standard_DS2", "Standard_DS2_v2", "Standard_DS2_v2_Promo", "Standard_DS3", "Standard_DS3_v2",
     "Standard_DS3_v2_Promo", "Standard_DS4", "Standard_DS4_v2", "Standard_DS4_v2_Promo",
     "Standard_DS5_v2", "Standard_DS5_v2_Promo", "Standard_E16_v3", "Standard_E16s_v3",
     "Standard_E2_v3", "Standard_E2s_v3", "Standard_E32-16s_v3", "Standard_E32-8s_v3",
     "Standard_E32_v3", "Standard_E32s_v3", "Standard_E4_v3", "Standard_E4s_v3",
     "Standard_E64-16s_v3", "Standard_E64-32s_v3", "Standard_E64_v3", "Standard_E64s_v3",
     "Standard_E8_v3", "Standard_E8s_v3", "Standard_F1", "Standard_F16", "Standard_F16s",
     "Standard_F16s_v2", "Standard_F1s", "Standard_F2", "Standard_F2s", "Standard_F2s_v2",
     "Standard_F32s_v2", "Standard_F4", "Standard_F4s", "Standard_F4s_v2", "Standard_F64s_v2",
     "Standard_F72s_v2", "Standard_F8", "Standard_F8s", "Standard_F8s_v2", "Standard_G1",
     "Standard_G2", "Standard_G3", "Standard_G4", "Standard_G5", "Standard_GS1", "Standard_GS2",
     "Standard_GS3", "Standard_GS4", "Standard_GS4-4", "Standard_GS4-8", "Standard_GS5",
     "Standard_GS5-16", "Standard_GS5-8", "Standard_H16", "Standard_H16m", "Standard_H16mr",
     "Standard_H16r", "Standard_H8", "Standard_H8m", "Standard_L16s", "Standard_L32s",
     "Standard_L4s", "Standard_L8s", "Standard_M128-32ms", "Standard_M128-64ms", "Standard_M128ms",
     "Standard_M128s", "Standard_M64-16ms", "Standard_M64-32ms", "Standard_M64ms", "Standard_M64s",
     "Standard_NC12", "Standard_NC12s_v2", "Standard_NC12s_v3", "Standard_NC24", "Standard_NC24r",
     "Standard_NC24rs_v2", "Standard_NC24rs_v3", "Standard_NC24s_v2", "Standard_NC24s_v3",
     "Standard_NC6", "Standard_NC6s_v2", "Standard_NC6s_v3", "Standard_ND12s", "Standard_ND24rs",
     "Standard_ND24s", "Standard_ND6s", "Standard_NV12", "Standard_NV24", "Standard_NV6".
    :type vm_size: str or
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceVMSizeTypes
    :param os_disk_size_gb: OS Disk Size in GB to be used to specify the disk size for every
     machine in this master/agent pool. If you specify 0, it will apply the default osDisk size
     according to the vmSize specified.
    :type os_disk_size_gb: int
    :param dns_prefix: DNS prefix to be used to create the FQDN for the agent pool.
    :type dns_prefix: str
    :ivar fqdn: FQDN for the agent pool.
    :vartype fqdn: str
    :param ports: Ports number array used to expose on this agent pool. The default opened ports
     are different based on your choice of orchestrator.
    :type ports: list[int]
    :param storage_profile: Storage profile specifies what kind of storage used. Choose from
     StorageAccount and ManagedDisks. Leave it empty, we will choose for you based on the
     orchestrator choice. Possible values include: "StorageAccount", "ManagedDisks".
    :type storage_profile: str or
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceStorageProfileTypes
    :param vnet_subnet_id: VNet SubnetID specifies the VNet's subnet identifier.
    :type vnet_subnet_id: str
    :param os_type: OsType to be used to specify os type. Choose from Linux and Windows. Default to
     Linux. Possible values include: "Linux", "Windows". Default value: "Linux".
    :type os_type: str or ~azure.mgmt.containerservice.v2017_07_01.models.OSType
    """

    _validation = {
        'name': {'required': True},
        'count': {'maximum': 100, 'minimum': 1},
        'vm_size': {'required': True},
        'os_disk_size_gb': {'maximum': 1023, 'minimum': 0},
        'fqdn': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'os_disk_size_gb': {'key': 'osDiskSizeGB', 'type': 'int'},
        'dns_prefix': {'key': 'dnsPrefix', 'type': 'str'},
        'fqdn': {'key': 'fqdn', 'type': 'str'},
        'ports': {'key': 'ports', 'type': '[int]'},
        'storage_profile': {'key': 'storageProfile', 'type': 'str'},
        'vnet_subnet_id': {'key': 'vnetSubnetID', 'type': 'str'},
        'os_type': {'key': 'osType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceAgentPoolProfile, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.count = kwargs.get('count', 1)
        self.vm_size = kwargs['vm_size']
        self.os_disk_size_gb = kwargs.get('os_disk_size_gb', None)
        self.dns_prefix = kwargs.get('dns_prefix', None)
        self.fqdn = None
        self.ports = kwargs.get('ports', None)
        self.storage_profile = kwargs.get('storage_profile', None)
        self.vnet_subnet_id = kwargs.get('vnet_subnet_id', None)
        self.os_type = kwargs.get('os_type', "Linux")


class ContainerServiceCustomProfile(msrest.serialization.Model):
    """Properties to configure a custom container service cluster.

    All required parameters must be populated in order to send to Azure.

    :param orchestrator: Required. The name of the custom orchestrator to use.
    :type orchestrator: str
    """

    _validation = {
        'orchestrator': {'required': True},
    }

    _attribute_map = {
        'orchestrator': {'key': 'orchestrator', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceCustomProfile, self).__init__(**kwargs)
        self.orchestrator = kwargs['orchestrator']


class ContainerServiceDiagnosticsProfile(msrest.serialization.Model):
    """Profile for diagnostics on the container service cluster.

    All required parameters must be populated in order to send to Azure.

    :param vm_diagnostics: Required. Profile for diagnostics on the container service VMs.
    :type vm_diagnostics:
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceVMDiagnostics
    """

    _validation = {
        'vm_diagnostics': {'required': True},
    }

    _attribute_map = {
        'vm_diagnostics': {'key': 'vmDiagnostics', 'type': 'ContainerServiceVMDiagnostics'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceDiagnosticsProfile, self).__init__(**kwargs)
        self.vm_diagnostics = kwargs['vm_diagnostics']


class ContainerServiceLinuxProfile(msrest.serialization.Model):
    """Profile for Linux VMs in the container service cluster.

    All required parameters must be populated in order to send to Azure.

    :param admin_username: Required. The administrator username to use for Linux VMs.
    :type admin_username: str
    :param ssh: Required. SSH configuration for Linux-based VMs running on Azure.
    :type ssh: ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceSshConfiguration
    """

    _validation = {
        'admin_username': {'required': True, 'pattern': r'^[A-Za-z][-A-Za-z0-9_]*$'},
        'ssh': {'required': True},
    }

    _attribute_map = {
        'admin_username': {'key': 'adminUsername', 'type': 'str'},
        'ssh': {'key': 'ssh', 'type': 'ContainerServiceSshConfiguration'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceLinuxProfile, self).__init__(**kwargs)
        self.admin_username = kwargs['admin_username']
        self.ssh = kwargs['ssh']


class ContainerServiceListResult(msrest.serialization.Model):
    """The response from the List Container Services operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: The list of container services.
    :type value: list[~azure.mgmt.containerservice.v2017_07_01.models.ContainerService]
    :ivar next_link: The URL to get the next set of container service results.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ContainerService]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = None


class ContainerServiceMasterProfile(msrest.serialization.Model):
    """Profile for the container service master.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param count: Number of masters (VMs) in the container service cluster. Allowed values are 1,
     3, and 5. The default value is 1. Possible values include: 1, 3, 5. Default value: "1".
    :type count: str or ~azure.mgmt.containerservice.v2017_07_01.models.Count
    :param dns_prefix: Required. DNS prefix to be used to create the FQDN for the master pool.
    :type dns_prefix: str
    :param vm_size: Required. Size of agent VMs. Possible values include: "Standard_A1",
     "Standard_A10", "Standard_A11", "Standard_A1_v2", "Standard_A2", "Standard_A2_v2",
     "Standard_A2m_v2", "Standard_A3", "Standard_A4", "Standard_A4_v2", "Standard_A4m_v2",
     "Standard_A5", "Standard_A6", "Standard_A7", "Standard_A8", "Standard_A8_v2",
     "Standard_A8m_v2", "Standard_A9", "Standard_B2ms", "Standard_B2s", "Standard_B4ms",
     "Standard_B8ms", "Standard_D1", "Standard_D11", "Standard_D11_v2", "Standard_D11_v2_Promo",
     "Standard_D12", "Standard_D12_v2", "Standard_D12_v2_Promo", "Standard_D13", "Standard_D13_v2",
     "Standard_D13_v2_Promo", "Standard_D14", "Standard_D14_v2", "Standard_D14_v2_Promo",
     "Standard_D15_v2", "Standard_D16_v3", "Standard_D16s_v3", "Standard_D1_v2", "Standard_D2",
     "Standard_D2_v2", "Standard_D2_v2_Promo", "Standard_D2_v3", "Standard_D2s_v3", "Standard_D3",
     "Standard_D32_v3", "Standard_D32s_v3", "Standard_D3_v2", "Standard_D3_v2_Promo", "Standard_D4",
     "Standard_D4_v2", "Standard_D4_v2_Promo", "Standard_D4_v3", "Standard_D4s_v3",
     "Standard_D5_v2", "Standard_D5_v2_Promo", "Standard_D64_v3", "Standard_D64s_v3",
     "Standard_D8_v3", "Standard_D8s_v3", "Standard_DS1", "Standard_DS11", "Standard_DS11_v2",
     "Standard_DS11_v2_Promo", "Standard_DS12", "Standard_DS12_v2", "Standard_DS12_v2_Promo",
     "Standard_DS13", "Standard_DS13-2_v2", "Standard_DS13-4_v2", "Standard_DS13_v2",
     "Standard_DS13_v2_Promo", "Standard_DS14", "Standard_DS14-4_v2", "Standard_DS14-8_v2",
     "Standard_DS14_v2", "Standard_DS14_v2_Promo", "Standard_DS15_v2", "Standard_DS1_v2",
     "Standard_DS2", "Standard_DS2_v2", "Standard_DS2_v2_Promo", "Standard_DS3", "Standard_DS3_v2",
     "Standard_DS3_v2_Promo", "Standard_DS4", "Standard_DS4_v2", "Standard_DS4_v2_Promo",
     "Standard_DS5_v2", "Standard_DS5_v2_Promo", "Standard_E16_v3", "Standard_E16s_v3",
     "Standard_E2_v3", "Standard_E2s_v3", "Standard_E32-16s_v3", "Standard_E32-8s_v3",
     "Standard_E32_v3", "Standard_E32s_v3", "Standard_E4_v3", "Standard_E4s_v3",
     "Standard_E64-16s_v3", "Standard_E64-32s_v3", "Standard_E64_v3", "Standard_E64s_v3",
     "Standard_E8_v3", "Standard_E8s_v3", "Standard_F1", "Standard_F16", "Standard_F16s",
     "Standard_F16s_v2", "Standard_F1s", "Standard_F2", "Standard_F2s", "Standard_F2s_v2",
     "Standard_F32s_v2", "Standard_F4", "Standard_F4s", "Standard_F4s_v2", "Standard_F64s_v2",
     "Standard_F72s_v2", "Standard_F8", "Standard_F8s", "Standard_F8s_v2", "Standard_G1",
     "Standard_G2", "Standard_G3", "Standard_G4", "Standard_G5", "Standard_GS1", "Standard_GS2",
     "Standard_GS3", "Standard_GS4", "Standard_GS4-4", "Standard_GS4-8", "Standard_GS5",
     "Standard_GS5-16", "Standard_GS5-8", "Standard_H16", "Standard_H16m", "Standard_H16mr",
     "Standard_H16r", "Standard_H8", "Standard_H8m", "Standard_L16s", "Standard_L32s",
     "Standard_L4s", "Standard_L8s", "Standard_M128-32ms", "Standard_M128-64ms", "Standard_M128ms",
     "Standard_M128s", "Standard_M64-16ms", "Standard_M64-32ms", "Standard_M64ms", "Standard_M64s",
     "Standard_NC12", "Standard_NC12s_v2", "Standard_NC12s_v3", "Standard_NC24", "Standard_NC24r",
     "Standard_NC24rs_v2", "Standard_NC24rs_v3", "Standard_NC24s_v2", "Standard_NC24s_v3",
     "Standard_NC6", "Standard_NC6s_v2", "Standard_NC6s_v3", "Standard_ND12s", "Standard_ND24rs",
     "Standard_ND24s", "Standard_ND6s", "Standard_NV12", "Standard_NV24", "Standard_NV6".
    :type vm_size: str or
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceVMSizeTypes
    :param os_disk_size_gb: OS Disk Size in GB to be used to specify the disk size for every
     machine in this master/agent pool. If you specify 0, it will apply the default osDisk size
     according to the vmSize specified.
    :type os_disk_size_gb: int
    :param vnet_subnet_id: VNet SubnetID specifies the VNet's subnet identifier.
    :type vnet_subnet_id: str
    :param first_consecutive_static_ip: FirstConsecutiveStaticIP used to specify the first static
     ip of masters.
    :type first_consecutive_static_ip: str
    :param storage_profile: Storage profile specifies what kind of storage used. Choose from
     StorageAccount and ManagedDisks. Leave it empty, we will choose for you based on the
     orchestrator choice. Possible values include: "StorageAccount", "ManagedDisks".
    :type storage_profile: str or
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceStorageProfileTypes
    :ivar fqdn: FQDN for the master pool.
    :vartype fqdn: str
    """

    _validation = {
        'dns_prefix': {'required': True},
        'vm_size': {'required': True},
        'os_disk_size_gb': {'maximum': 1023, 'minimum': 0},
        'fqdn': {'readonly': True},
    }

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'dns_prefix': {'key': 'dnsPrefix', 'type': 'str'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'os_disk_size_gb': {'key': 'osDiskSizeGB', 'type': 'int'},
        'vnet_subnet_id': {'key': 'vnetSubnetID', 'type': 'str'},
        'first_consecutive_static_ip': {'key': 'firstConsecutiveStaticIP', 'type': 'str'},
        'storage_profile': {'key': 'storageProfile', 'type': 'str'},
        'fqdn': {'key': 'fqdn', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceMasterProfile, self).__init__(**kwargs)
        self.count = kwargs.get('count', "1")
        self.dns_prefix = kwargs['dns_prefix']
        self.vm_size = kwargs['vm_size']
        self.os_disk_size_gb = kwargs.get('os_disk_size_gb', None)
        self.vnet_subnet_id = kwargs.get('vnet_subnet_id', None)
        self.first_consecutive_static_ip = kwargs.get('first_consecutive_static_ip', "10.240.255.5")
        self.storage_profile = kwargs.get('storage_profile', None)
        self.fqdn = None


class ContainerServiceOrchestratorProfile(msrest.serialization.Model):
    """Profile for the container service orchestrator.

    All required parameters must be populated in order to send to Azure.

    :param orchestrator_type: Required. The orchestrator to use to manage container service cluster
     resources. Valid values are Kubernetes, Swarm, DCOS, DockerCE and Custom. Possible values
     include: "Kubernetes", "Swarm", "DCOS", "DockerCE", "Custom".
    :type orchestrator_type: str or
     ~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceOrchestratorTypes
    :param orchestrator_version: The version of the orchestrator to use. You can specify the
     major.minor.patch part of the actual version.For example, you can specify version as "1.6.11".
    :type orchestrator_version: str
    """

    _validation = {
        'orchestrator_type': {'required': True},
    }

    _attribute_map = {
        'orchestrator_type': {'key': 'orchestratorType', 'type': 'str'},
        'orchestrator_version': {'key': 'orchestratorVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceOrchestratorProfile, self).__init__(**kwargs)
        self.orchestrator_type = kwargs['orchestrator_type']
        self.orchestrator_version = kwargs.get('orchestrator_version', None)


class ContainerServicePrincipalProfile(msrest.serialization.Model):
    """Information about a service principal identity for the cluster to use for manipulating Azure APIs. Either secret or keyVaultSecretRef must be specified.

    All required parameters must be populated in order to send to Azure.

    :param client_id: Required. The ID for the service principal.
    :type client_id: str
    :param secret: The secret password associated with the service principal in plain text.
    :type secret: str
    :param key_vault_secret_ref: Reference to a secret stored in Azure Key Vault.
    :type key_vault_secret_ref: ~azure.mgmt.containerservice.v2017_07_01.models.KeyVaultSecretRef
    """

    _validation = {
        'client_id': {'required': True},
    }

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'str'},
        'key_vault_secret_ref': {'key': 'keyVaultSecretRef', 'type': 'KeyVaultSecretRef'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServicePrincipalProfile, self).__init__(**kwargs)
        self.client_id = kwargs['client_id']
        self.secret = kwargs.get('secret', None)
        self.key_vault_secret_ref = kwargs.get('key_vault_secret_ref', None)


class ContainerServiceSshConfiguration(msrest.serialization.Model):
    """SSH configuration for Linux-based VMs running on Azure.

    All required parameters must be populated in order to send to Azure.

    :param public_keys: Required. The list of SSH public keys used to authenticate with Linux-based
     VMs. Only expect one key specified.
    :type public_keys:
     list[~azure.mgmt.containerservice.v2017_07_01.models.ContainerServiceSshPublicKey]
    """

    _validation = {
        'public_keys': {'required': True},
    }

    _attribute_map = {
        'public_keys': {'key': 'publicKeys', 'type': '[ContainerServiceSshPublicKey]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceSshConfiguration, self).__init__(**kwargs)
        self.public_keys = kwargs['public_keys']


class ContainerServiceSshPublicKey(msrest.serialization.Model):
    """Contains information about SSH certificate public key data.

    All required parameters must be populated in order to send to Azure.

    :param key_data: Required. Certificate public key used to authenticate with VMs through SSH.
     The certificate must be in PEM format with or without headers.
    :type key_data: str
    """

    _validation = {
        'key_data': {'required': True},
    }

    _attribute_map = {
        'key_data': {'key': 'keyData', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceSshPublicKey, self).__init__(**kwargs)
        self.key_data = kwargs['key_data']


class ContainerServiceVMDiagnostics(msrest.serialization.Model):
    """Profile for diagnostics on the container service VMs.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Whether the VM diagnostic agent is provisioned on the VM.
    :type enabled: bool
    :ivar storage_uri: The URI of the storage account where diagnostics are stored.
    :vartype storage_uri: str
    """

    _validation = {
        'enabled': {'required': True},
        'storage_uri': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'storage_uri': {'key': 'storageUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceVMDiagnostics, self).__init__(**kwargs)
        self.enabled = kwargs['enabled']
        self.storage_uri = None


class ContainerServiceWindowsProfile(msrest.serialization.Model):
    """Profile for Windows VMs in the container service cluster.

    All required parameters must be populated in order to send to Azure.

    :param admin_username: Required. The administrator username to use for Windows VMs.
    :type admin_username: str
    :param admin_password: Required. The administrator password to use for Windows VMs.
    :type admin_password: str
    """

    _validation = {
        'admin_username': {'required': True, 'pattern': r'^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)*$'},
        'admin_password': {'required': True, 'pattern': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%\^&\*\(\)])[a-zA-Z\d!@#$%\^&\*\(\)]{12,123}$'},
    }

    _attribute_map = {
        'admin_username': {'key': 'adminUsername', 'type': 'str'},
        'admin_password': {'key': 'adminPassword', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContainerServiceWindowsProfile, self).__init__(**kwargs)
        self.admin_username = kwargs['admin_username']
        self.admin_password = kwargs['admin_password']


class KeyVaultSecretRef(msrest.serialization.Model):
    """Reference to a secret stored in Azure Key Vault.

    All required parameters must be populated in order to send to Azure.

    :param vault_id: Required. Key vault identifier.
    :type vault_id: str
    :param secret_name: Required. The secret name.
    :type secret_name: str
    :param version: The secret version.
    :type version: str
    """

    _validation = {
        'vault_id': {'required': True},
        'secret_name': {'required': True},
    }

    _attribute_map = {
        'vault_id': {'key': 'vaultID', 'type': 'str'},
        'secret_name': {'key': 'secretName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyVaultSecretRef, self).__init__(**kwargs)
        self.vault_id = kwargs['vault_id']
        self.secret_name = kwargs['secret_name']
        self.version = kwargs.get('version', None)


class OrchestratorProfile(msrest.serialization.Model):
    """Contains information about orchestrator.

    All required parameters must be populated in order to send to Azure.

    :param orchestrator_type: Orchestrator type.
    :type orchestrator_type: str
    :param orchestrator_version: Required. Orchestrator version (major, minor, patch).
    :type orchestrator_version: str
    :param is_preview: Whether Kubernetes version is currently in preview.
    :type is_preview: bool
    """

    _validation = {
        'orchestrator_version': {'required': True},
    }

    _attribute_map = {
        'orchestrator_type': {'key': 'orchestratorType', 'type': 'str'},
        'orchestrator_version': {'key': 'orchestratorVersion', 'type': 'str'},
        'is_preview': {'key': 'isPreview', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrchestratorProfile, self).__init__(**kwargs)
        self.orchestrator_type = kwargs.get('orchestrator_type', None)
        self.orchestrator_version = kwargs['orchestrator_version']
        self.is_preview = kwargs.get('is_preview', None)


class OrchestratorVersionProfile(msrest.serialization.Model):
    """The profile of an orchestrator and its available versions.

    All required parameters must be populated in order to send to Azure.

    :param orchestrator_type: Required. Orchestrator type.
    :type orchestrator_type: str
    :param orchestrator_version: Required. Orchestrator version (major, minor, patch).
    :type orchestrator_version: str
    :param default: Installed by default if version is not specified.
    :type default: bool
    :param is_preview: Whether Kubernetes version is currently in preview.
    :type is_preview: bool
    :param upgrades: The list of available upgrade versions.
    :type upgrades: list[~azure.mgmt.containerservice.v2017_07_01.models.OrchestratorProfile]
    """

    _validation = {
        'orchestrator_type': {'required': True},
        'orchestrator_version': {'required': True},
    }

    _attribute_map = {
        'orchestrator_type': {'key': 'orchestratorType', 'type': 'str'},
        'orchestrator_version': {'key': 'orchestratorVersion', 'type': 'str'},
        'default': {'key': 'default', 'type': 'bool'},
        'is_preview': {'key': 'isPreview', 'type': 'bool'},
        'upgrades': {'key': 'upgrades', 'type': '[OrchestratorProfile]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrchestratorVersionProfile, self).__init__(**kwargs)
        self.orchestrator_type = kwargs['orchestrator_type']
        self.orchestrator_version = kwargs['orchestrator_version']
        self.default = kwargs.get('default', None)
        self.is_preview = kwargs.get('is_preview', None)
        self.upgrades = kwargs.get('upgrades', None)


class OrchestratorVersionProfileListResult(msrest.serialization.Model):
    """The list of versions for supported orchestrators.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Id of the orchestrator version profile list result.
    :vartype id: str
    :ivar name: Name of the orchestrator version profile list result.
    :vartype name: str
    :ivar type: Type of the orchestrator version profile list result.
    :vartype type: str
    :param orchestrators: Required. List of orchestrator version profiles.
    :type orchestrators:
     list[~azure.mgmt.containerservice.v2017_07_01.models.OrchestratorVersionProfile]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'orchestrators': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'orchestrators': {'key': 'properties.orchestrators', 'type': '[OrchestratorVersionProfile]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrchestratorVersionProfileListResult, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.orchestrators = kwargs['orchestrators']
