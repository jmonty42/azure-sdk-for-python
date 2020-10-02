# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AccessLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    READ = "Read"
    WRITE = "Write"

class DiskCreateOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """This enumerates the possible sources of a disk's creation.
    """

    EMPTY = "Empty"  #: Create an empty data disk of a size given by diskSizeGB.
    ATTACH = "Attach"  #: Disk will be attached to a VM.
    FROM_IMAGE = "FromImage"  #: Create a new disk from a platform image specified by the given imageReference or galleryImageReference.
    IMPORT_ENUM = "Import"  #: Create a disk by importing from a blob specified by a sourceUri in a storage account specified by storageAccountId.
    COPY = "Copy"  #: Create a new disk or snapshot by copying from a disk or snapshot specified by the given sourceResourceId.
    RESTORE = "Restore"  #: Create a new disk by copying from a backup recovery point.
    UPLOAD = "Upload"  #: Create a new disk by obtaining a write token and using it to directly upload the contents of the disk.

class DiskEncryptionSetIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Managed Identity used by the DiskEncryptionSet. Only SystemAssigned is supported.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"

class DiskState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the disk.
    """

    UNATTACHED = "Unattached"  #: The disk is not being used and can be attached to a VM.
    ATTACHED = "Attached"  #: The disk is currently mounted to a running VM.
    RESERVED = "Reserved"  #: The disk is mounted to a stopped-deallocated VM.
    ACTIVE_SAS = "ActiveSAS"  #: The disk currently has an Active SAS Uri associated with it.
    READY_TO_UPLOAD = "ReadyToUpload"  #: A disk is ready to be created by upload by requesting a write token.
    ACTIVE_UPLOAD = "ActiveUpload"  #: A disk is created for upload and a write token has been issued for uploading to it.

class DiskStorageAccountTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The sku name.
    """

    STANDARD_LRS = "Standard_LRS"  #: Standard HDD locally redundant storage. Best for backup, non-critical, and infrequent access.
    PREMIUM_LRS = "Premium_LRS"  #: Premium SSD locally redundant storage. Best for production and performance sensitive workloads.
    STANDARD_SSD_LRS = "StandardSSD_LRS"  #: Standard SSD locally redundant storage. Best for web servers, lightly used enterprise applications and dev/test.
    ULTRA_SSD_LRS = "UltraSSD_LRS"  #: Ultra SSD locally redundant storage. Best for IO-intensive workloads such as SAP HANA, top tier databases (for example, SQL, Oracle), and other transaction-heavy workloads.

class EncryptionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of key used to encrypt the data of the disk.
    """

    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"  #: Disk is encrypted with XStore managed key at rest. It is the default encryption type.
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"  #: Disk is encrypted with Customer managed key at rest.

class HyperVGeneration(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    """

    V1 = "V1"
    V2 = "V2"

class OperatingSystemTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Operating System type.
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class SnapshotStorageAccountTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The sku name.
    """

    STANDARD_LRS = "Standard_LRS"  #: Standard HDD locally redundant storage.
    PREMIUM_LRS = "Premium_LRS"  #: Premium SSD locally redundant storage.
    STANDARD_ZRS = "Standard_ZRS"  #: Standard zone redundant storage.
