# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Attributes(msrest.serialization.Model):
    """The object attributes managed by the KeyVault service.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param enabled: Determines whether the object is enabled.
    :type enabled: bool
    :param not_before: Not before date in UTC.
    :type not_before: ~datetime.datetime
    :param expires: Expiry date in UTC.
    :type expires: ~datetime.datetime
    :ivar created: Creation time in UTC.
    :vartype created: ~datetime.datetime
    :ivar updated: Last updated time in UTC.
    :vartype updated: ~datetime.datetime
    """

    _validation = {
        'created': {'readonly': True},
        'updated': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'not_before': {'key': 'nbf', 'type': 'unix-time'},
        'expires': {'key': 'exp', 'type': 'unix-time'},
        'created': {'key': 'created', 'type': 'unix-time'},
        'updated': {'key': 'updated', 'type': 'unix-time'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Attributes, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.not_before = kwargs.get('not_before', None)
        self.expires = kwargs.get('expires', None)
        self.created = None
        self.updated = None


class Error(msrest.serialization.Model):
    """The key vault server error.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar inner_error: The key vault server error.
    :vartype inner_error: ~azure.keyvault.v7_2.models.Error
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'inner_error': {'key': 'innererror', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.inner_error = None


class FullBackupOperation(msrest.serialization.Model):
    """Full backup operation.

    :param status: Status of the backup operation.
    :type status: str
    :param status_details: The status details of backup operation.
    :type status_details: str
    :param error: Error encountered, if any, during the full backup operation.
    :type error: ~azure.keyvault.v7_2.models.Error
    :param start_time: The start time of the backup operation in UTC.
    :type start_time: ~datetime.datetime
    :param end_time: The end time of the backup operation in UTC.
    :type end_time: ~datetime.datetime
    :param job_id: Identifier for the full backup operation.
    :type job_id: str
    :param azure_storage_blob_container_uri: The Azure blob storage container Uri which contains
     the full backup.
    :type azure_storage_blob_container_uri: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'status_details': {'key': 'statusDetails', 'type': 'str'},
        'error': {'key': 'error', 'type': 'Error'},
        'start_time': {'key': 'startTime', 'type': 'unix-time'},
        'end_time': {'key': 'endTime', 'type': 'unix-time'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'azure_storage_blob_container_uri': {'key': 'azureStorageBlobContainerUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FullBackupOperation, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.status_details = kwargs.get('status_details', None)
        self.error = kwargs.get('error', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.job_id = kwargs.get('job_id', None)
        self.azure_storage_blob_container_uri = kwargs.get('azure_storage_blob_container_uri', None)


class KeyVaultError(msrest.serialization.Model):
    """The key vault error exception.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar error: The key vault server error.
    :vartype error: ~azure.keyvault.v7_2.models.Error
    """

    _validation = {
        'error': {'readonly': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyVaultError, self).__init__(**kwargs)
        self.error = None


class Permission(msrest.serialization.Model):
    """Role definition permissions.

    :param actions: Allowed actions.
    :type actions: list[str]
    :param not_actions: Denied actions.
    :type not_actions: list[str]
    :param data_actions: Allowed Data actions.
    :type data_actions: list[str]
    :param not_data_actions: Denied Data actions.
    :type not_data_actions: list[str]
    """

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[str]'},
        'not_actions': {'key': 'notActions', 'type': '[str]'},
        'data_actions': {'key': 'dataActions', 'type': '[str]'},
        'not_data_actions': {'key': 'notDataActions', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Permission, self).__init__(**kwargs)
        self.actions = kwargs.get('actions', None)
        self.not_actions = kwargs.get('not_actions', None)
        self.data_actions = kwargs.get('data_actions', None)
        self.not_data_actions = kwargs.get('not_data_actions', None)


class RestoreOperation(msrest.serialization.Model):
    """Restore operation.

    :param status: Status of the restore operation.
    :type status: str
    :param status_details: The status details of restore operation.
    :type status_details: str
    :param error: Error encountered, if any, during the restore operation.
    :type error: ~azure.keyvault.v7_2.models.Error
    :param job_id: Identifier for the restore operation.
    :type job_id: str
    :param start_time: The start time of the restore operation.
    :type start_time: ~datetime.datetime
    :param end_time: The end time of the restore operation.
    :type end_time: ~datetime.datetime
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'status_details': {'key': 'statusDetails', 'type': 'str'},
        'error': {'key': 'error', 'type': 'Error'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'unix-time'},
        'end_time': {'key': 'endTime', 'type': 'unix-time'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RestoreOperation, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.status_details = kwargs.get('status_details', None)
        self.error = kwargs.get('error', None)
        self.job_id = kwargs.get('job_id', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)


class RestoreOperationParameters(msrest.serialization.Model):
    """RestoreOperationParameters.

    All required parameters must be populated in order to send to Azure.

    :param sas_token_parameters: Required.
    :type sas_token_parameters: ~azure.keyvault.v7_2.models.SASTokenParameter
    :param folder_to_restore: Required. The Folder name of the blob where the previous successful
     full backup was stored.
    :type folder_to_restore: str
    """

    _validation = {
        'sas_token_parameters': {'required': True},
        'folder_to_restore': {'required': True},
    }

    _attribute_map = {
        'sas_token_parameters': {'key': 'sasTokenParameters', 'type': 'SASTokenParameter'},
        'folder_to_restore': {'key': 'folderToRestore', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RestoreOperationParameters, self).__init__(**kwargs)
        self.sas_token_parameters = kwargs['sas_token_parameters']
        self.folder_to_restore = kwargs['folder_to_restore']


class RoleAssignment(msrest.serialization.Model):
    """Role Assignments.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The role assignment ID.
    :vartype id: str
    :ivar name: The role assignment name.
    :vartype name: str
    :ivar type: The role assignment type.
    :vartype type: str
    :param properties: Role assignment properties.
    :type properties: ~azure.keyvault.v7_2.models.RoleAssignmentPropertiesWithScope
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'RoleAssignmentPropertiesWithScope'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignment, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = kwargs.get('properties', None)


class RoleAssignmentCreateParameters(msrest.serialization.Model):
    """Role assignment create parameters.

    All required parameters must be populated in order to send to Azure.

    :param properties: Required. Role assignment properties.
    :type properties: ~azure.keyvault.v7_2.models.RoleAssignmentProperties
    """

    _validation = {
        'properties': {'required': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'RoleAssignmentProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentCreateParameters, self).__init__(**kwargs)
        self.properties = kwargs['properties']


class RoleAssignmentFilter(msrest.serialization.Model):
    """Role Assignments filter.

    :param principal_id: Returns role assignment of the specific principal.
    :type principal_id: str
    """

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentFilter, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)


class RoleAssignmentListResult(msrest.serialization.Model):
    """Role assignment list operation result.

    :param value: Role assignment list.
    :type value: list[~azure.keyvault.v7_2.models.RoleAssignment]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[RoleAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class RoleAssignmentProperties(msrest.serialization.Model):
    """Role assignment properties.

    All required parameters must be populated in order to send to Azure.

    :param role_definition_id: Required. The role definition ID used in the role assignment.
    :type role_definition_id: str
    :param principal_id: Required. The principal ID assigned to the role. This maps to the ID
     inside the Active Directory. It can point to a user, service principal, or security group.
    :type principal_id: str
    """

    _validation = {
        'role_definition_id': {'required': True},
        'principal_id': {'required': True},
    }

    _attribute_map = {
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentProperties, self).__init__(**kwargs)
        self.role_definition_id = kwargs['role_definition_id']
        self.principal_id = kwargs['principal_id']


class RoleAssignmentPropertiesWithScope(msrest.serialization.Model):
    """Role assignment properties with scope.

    :param scope: The role assignment scope.
    :type scope: str
    :param role_definition_id: The role definition ID.
    :type role_definition_id: str
    :param principal_id: The principal ID.
    :type principal_id: str
    """

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleAssignmentPropertiesWithScope, self).__init__(**kwargs)
        self.scope = kwargs.get('scope', None)
        self.role_definition_id = kwargs.get('role_definition_id', None)
        self.principal_id = kwargs.get('principal_id', None)


class RoleDefinition(msrest.serialization.Model):
    """Role definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The role definition ID.
    :vartype id: str
    :ivar name: The role definition name.
    :vartype name: str
    :ivar type: The role definition type.
    :vartype type: str
    :param role_name: The role name.
    :type role_name: str
    :param description: The role definition description.
    :type description: str
    :param role_type: The role type.
    :type role_type: str
    :param permissions: Role definition permissions.
    :type permissions: list[~azure.keyvault.v7_2.models.Permission]
    :param assignable_scopes: Role definition assignable scopes.
    :type assignable_scopes: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'role_name': {'key': 'properties.roleName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'role_type': {'key': 'properties.type', 'type': 'str'},
        'permissions': {'key': 'properties.permissions', 'type': '[Permission]'},
        'assignable_scopes': {'key': 'properties.assignableScopes', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.role_name = kwargs.get('role_name', None)
        self.description = kwargs.get('description', None)
        self.role_type = kwargs.get('role_type', None)
        self.permissions = kwargs.get('permissions', None)
        self.assignable_scopes = kwargs.get('assignable_scopes', None)


class RoleDefinitionFilter(msrest.serialization.Model):
    """Role Definitions filter.

    :param role_name: Returns role definition with the specific name.
    :type role_name: str
    """

    _attribute_map = {
        'role_name': {'key': 'roleName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleDefinitionFilter, self).__init__(**kwargs)
        self.role_name = kwargs.get('role_name', None)


class RoleDefinitionListResult(msrest.serialization.Model):
    """Role definition list operation result.

    :param value: Role definition list.
    :type value: list[~azure.keyvault.v7_2.models.RoleDefinition]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[RoleDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RoleDefinitionListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class SASTokenParameter(msrest.serialization.Model):
    """SASTokenParameter.

    All required parameters must be populated in order to send to Azure.

    :param storage_resource_uri: Required. Azure Blob storage container Uri.
    :type storage_resource_uri: str
    :param token: Required. The SAS token pointing to an Azure Blob storage container.
    :type token: str
    """

    _validation = {
        'storage_resource_uri': {'required': True},
        'token': {'required': True},
    }

    _attribute_map = {
        'storage_resource_uri': {'key': 'storageResourceUri', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SASTokenParameter, self).__init__(**kwargs)
        self.storage_resource_uri = kwargs['storage_resource_uri']
        self.token = kwargs['token']


class SelectiveKeyRestoreOperation(msrest.serialization.Model):
    """Selective Key Restore operation.

    :param status: Status of the restore operation.
    :type status: str
    :param status_details: The status details of restore operation.
    :type status_details: str
    :param error: Error encountered, if any, during the selective key restore operation.
    :type error: ~azure.keyvault.v7_2.models.Error
    :param job_id: Identifier for the selective key restore operation.
    :type job_id: str
    :param start_time: The start time of the restore operation.
    :type start_time: ~datetime.datetime
    :param end_time: The end time of the restore operation.
    :type end_time: ~datetime.datetime
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'status_details': {'key': 'statusDetails', 'type': 'str'},
        'error': {'key': 'error', 'type': 'Error'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'unix-time'},
        'end_time': {'key': 'endTime', 'type': 'unix-time'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SelectiveKeyRestoreOperation, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.status_details = kwargs.get('status_details', None)
        self.error = kwargs.get('error', None)
        self.job_id = kwargs.get('job_id', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)


class SelectiveKeyRestoreOperationParameters(msrest.serialization.Model):
    """SelectiveKeyRestoreOperationParameters.

    All required parameters must be populated in order to send to Azure.

    :param sas_token_parameters: Required.
    :type sas_token_parameters: ~azure.keyvault.v7_2.models.SASTokenParameter
    :param folder: Required. The Folder name of the blob where the previous successful full backup
     was stored.
    :type folder: str
    """

    _validation = {
        'sas_token_parameters': {'required': True},
        'folder': {'required': True},
    }

    _attribute_map = {
        'sas_token_parameters': {'key': 'sasTokenParameters', 'type': 'SASTokenParameter'},
        'folder': {'key': 'folder', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SelectiveKeyRestoreOperationParameters, self).__init__(**kwargs)
        self.sas_token_parameters = kwargs['sas_token_parameters']
        self.folder = kwargs['folder']
