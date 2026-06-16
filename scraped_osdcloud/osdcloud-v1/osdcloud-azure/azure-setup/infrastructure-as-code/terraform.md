> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/terraform.md).

# Terraform

Unlike Bicep Terraform allows us to separate the variables of the definition files from the state of our infrastructure, the working folder is c:\osdcloud\terraform

![](/files/6pwO5dNysda9MHez1XbZ)

### File main.tf

This is the main file of terraform and contains the complete description of the future infrastructure.

```bicep
resource "azurerm_resource_group" "RessourceGroup" {
    location    = var.osdcloud_Location
    name      = var.osdcloud_resourcegroup
}

resource "azurerm_storage_account" "OSDCloud" {
  account_replication_type = "LRS"
  account_tier             = "Standard"
  location                 = var.osdcloud_Location
  name                     = var.osdcloud_StorageAccountOSDCloud
  resource_group_name      = var.osdcloud_resourcegroup
  access_tier              = "Hot"
  min_tls_version          = "TLS1_2"
  account_kind             = "StorageV2"
  shared_access_key_enabled = true
  allow_nested_items_to_be_public = true
    blob_properties {
      change_feed_enabled = true
    }
  
  tags = {
    OSDCloud = "production"
  }
  depends_on = [
    azurerm_resource_group.RessourceGroup,
  ]
}
resource "azurerm_storage_account" "OSDScripts" {
    depends_on = [
    azurerm_resource_group.RessourceGroup,
  ]

  account_replication_type = "LRS"
  account_tier             = "Standard"
  location                 = var.osdcloud_Location
  name                     = var.osdcloud_StorageAccountOSDScripts
  resource_group_name      = var.osdcloud_resourcegroup
  min_tls_version          = "TLS1_2"
  access_tier              = "Hot"
  account_kind             = "StorageV2"
  shared_access_key_enabled = true
  allow_nested_items_to_be_public = true
    blob_properties {
      change_feed_enabled = true
    }
  tags = {
    OSDScripts = "powershell"
  }
}

resource "azurerm_storage_container" "ContainerOSDCloud" {
   depends_on = [
    azurerm_resource_group.RessourceGroup,
    azurerm_storage_account.OSDCloud,
  ]

  count = length(var.osdcloud_containers)
  name                  = var.osdcloud_containers[count.index]
  storage_account_name  = azurerm_storage_account.OSDCloud.name
  container_access_type = "container"
}

resource "azurerm_storage_container" "ContainerOSDScripts" {
  count = length(var.osdscript_containers)
  name                  = var.osdscript_containers[count.index]
  storage_account_name  = azurerm_storage_account.OSDScripts.name
  container_access_type = "container"
}

resource "azurerm_role_assignment" "RBAC_OSDCloud" {
  scope                = azurerm_storage_account.OSDCloud.id
  role_definition_name = "Storage Blob Data Reader"
  principal_id         = var.technicien_id
}
resource "azurerm_role_assignment" "RBAC_OSDScripts" {
  scope                = azurerm_storage_account.OSDScripts.id
  role_definition_name = "Storage Blob Data Reader"
  principal_id         = var.technicien_id
}

```

### File provider.tf

The providers file contains the information to connect to Azure.

```bicep
terraform {
  backend "local" {}
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.9.0"
    }
  }
}

provider "azurerm" {
  subscription_id = var.subscription_id
  tenant_id =  var.tenant_id
  features {}
}

```

### File variables.tf

This file allows you to understand the role of each variable as well as the type that accepts variables, objects, lists, integer etc...

```bicep
variable "osdcloud_containers" {
    description = "List of containers to create for OSDCloud"
    type = list
}
variable "osdscript_containers" {
    description = "List of containers to create for OSDScripts"
    type = list
}
variable "osdcloud_resourcegroup" {
    description = " Name for the resource group"
    type = string
}
variable "osdcloud_StorageAccountOSDCloud" {
    description = "The name of the storage account for OSDCloud"
    type = string
}
 variable "osdcloud_StorageAccountOSDScripts" {
    description = "The name of the storage account for OSDScripts"
    type = string   
 }   
variable "osdcloud_Location" {
    description = "Select your Azure region"
    type = string

 validation {
    condition = contains(
      ["eastasia", "southeastasia", "centralus","eastus","eastus2","westus","northcentralus","southcentralus","northeurope","westeurope","japanwest","japaneast","brazilsouth","australiaeast","australiasoutheast","southindia","centralindia","westindia","canadacentral","canadaeast","uksouth","ukwest","westcentralus","germanywestcentral","norwaywest","norwayeast","brazilsoutheast","westus3","swedencentral"],
      var.osdcloud_Location
    )
    error_message = "Err: This location is not valid for Azure."
  }
}
variable "subscription_id" {
    description = " your Azure subscription id"
    type = string
}

variable "technicien_id" {
    description = " your AzureAD User Id, it can only connect to storage account download and list objects"
    type = string
}
variable "tenant_id" {
    description = " your Azure tenant id"
    type = string
}
```

### file terraform.tfvars

It is in this file that we must fill in all the necessary information.

* [x] The Azure regrion
* [x] The subscription Id
* [x] The [Technicien](/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/technicien.md) Id
* [x] The tenant Id

```
osdcloud_containers = ["server", "retail", "insiders", "driverpack", "bootimage"]
osdscript_containers = ["scripts", "packages", "unattend", "others"]
osdcloud_resourcegroup = "AzOSDCloud"
osdcloud_StorageAccountOSDScripts = "osdscripts"
osdcloud_StorageAccountOSDCloud = "osdcloud"
osdcloud_Location = ""
subscription_id = ""
technicien_id = ""
tenant_id = ""
```

## Sponsor

{% embed url="<https://www.recastsoftware.com/>" %}
OSDeploy is sponsored by Recast Software
{% endembed %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/terraform.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
