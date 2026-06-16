> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/bicep.md).

# Bicep

With Bicep we need only one file which is located in the directory <mark style="color:purple;">**c:\osdcloud\bicep**</mark>.

![](/files/ffoJExfaSl0Jia9Rflie)

Here is the content of the bicep file, we are only interested in line **62-63** we must come here and insert the [Technicien](/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/technicien.md) I&#x64;**.**

```bicep
@description('Specifies the name of the Azure Storage account.')
param storageAccountName string ='azosdcloud'

@description('Specifies the name of the Azure Storage account.')
param StorageAccuntList string ='azosdscripts'

@description('Specifies the name of the blob for logs container.')
param containerName string = 'logs'

@description('Specifies the location in which the Azure Storage resources should be deployed.')
param location string = resourceGroup().location

@description('Specifies container object list for wim images.')
param containers object = {
  c1:{
    name: 'server'
    type: 'Container'
  }
  c2:{
    name: 'retail'
    type: 'Container'
  }
  c3:{
    name: 'insiders'
    type: 'Container'
  }
  c4:{
    name: 'driverpack'
    type: 'Container'
  }
  c5:{
    name: 'bootimage'
    type: 'Container'
  }

}
@description('Specifies container object list for powershell scripts, packages, unattend.')
param scripts object = {
  c1:{
    name: 'scripts'
    type: 'Container'
  }
  c2:{
    name: 'packages'
    type: 'Container'
  }
  c3:{
    name: 'unattend'
    type: 'Container'
  }
  c4:{
    name: 'others'
    type: 'Container'
  }
}

@description('This is the built-in Storage Blob Data Reader.')
resource StorageBlobDataReaderDefinition 'Microsoft.Authorization/roleDefinitions@2018-01-01-preview' existing = {
  scope: subscription()
  name: 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
}
@description('This is the ID for the AzureADAccount who can access.')
param principalId string = ''

resource AzStorage 'Microsoft.Storage/storageAccounts@2021-06-01' = {
  name: storageAccountName
  location: location
  tags : {
    OSDCloud :'production' 
  }
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    allowBlobPublicAccess: true
    allowSharedKeyAccess:true
    minimumTlsVersion: 'TLS1_2'
    defaultToOAuthAuthentication: true
    
  }
}
resource AzScripts 'Microsoft.Storage/storageAccounts@2021-06-01' = {
  name: StorageAccuntList
  location: location
  tags : {
    OSDScripts :'powershell' 
  }
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    allowBlobPublicAccess: true
    allowSharedKeyAccess:true
    allowCrossTenantReplication: true
    minimumTlsVersion: 'TLS1_2'
    defaultToOAuthAuthentication: true
  }
}

resource log 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-06-01' = {
  name: '${AzStorage.name}/default/${containerName}'

}

resource containerlist 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-06-01' =[for cont in items(containers):{
  name:'${AzStorage.name}/default/${cont.value.name}'
  properties: {
    publicAccess: cont.value.type
}
}]

resource containerscriptlist 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-06-01' =[for cont in items(scripts):{
  name:'${AzScripts.name}/default/${cont.value.name}'
  properties: {
    publicAccess: cont.value.type
}
}]

resource ActivateFeedStorage 'Microsoft.Storage/storageAccounts/blobServices@2021-09-01' = {
  name: 'default'
  parent: AzStorage
  properties: {
    changeFeed: {
      enabled: true
    }
  }
}
resource ActivateFeedScript 'Microsoft.Storage/storageAccounts/blobServices@2021-09-01' = {
  name: 'default'
  parent: AzScripts
  properties: {
    changeFeed: {
      enabled: true
    }
  }
}

resource roleAssignmentAzStorage 'Microsoft.Authorization/roleAssignments@2020-10-01-preview' = {
  scope: AzStorage
  name: guid(AzStorage.id, principalId, StorageBlobDataReaderDefinition.id)
  properties: {
    roleDefinitionId: StorageBlobDataReaderDefinition.id
    principalId: principalId
    principalType: 'User'
  }
}
resource roleAssignmentAzSScripts 'Microsoft.Authorization/roleAssignments@2020-10-01-preview' = {
  scope: AzScripts
  name: guid(AzScripts.id, principalId, StorageBlobDataReaderDefinition.id)
  properties: {
    roleDefinitionId: StorageBlobDataReaderDefinition.id
    principalId: principalId
    principalType: 'User'
  }
}

```

Once this Bicep file is executed your **Azure** environment will be configured with two **storage accounts**, one for wim image storage and a second one still expiring for powershell scripts, packages, unattend and others.

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/bicep.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
