> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deep-dive/azure-tags.md).

# Azure Tags

{% hint style="danger" %}
This page is incomplete
{% endhint %}

You're probably wondering why Tags are used by OSDCloud, and why it won't work without them.  The way OSDCloud works in Azure is that it needs to locate the WIM files that are in a Container that are within a Storage Account

## Get-AzStorageAccount (Az.Storage)

This PowerShell cmdlet is used to get all the Storage Accounts that you can see in your Azure Subscription with the (Storage Account) Reader role.  In my case, I have 13 Storage Accounts

```powershell
PS C:\> Get-AzStorageAccount | Select StorageAccountName

StorageAccountName 
------------------ 
azosd              
azosdcloud         
azosdweb           
cdsosd             
cs710032001c802b70f
getosdcloudcom     
goosdcloudcom      
mmsmoa             
mmsmoafunction     
osdcloudazure      
osdclouddemo       
ou812              
winpe     
```

Ideally, you should assign Rights to limit what I can read from, but as an Azure Global Admin, I get to see everything.  Additionally, not all of these Storage Accounts are used for OSD.  Some are used by Functions, or Reporting, etc.

## Get-AzTag (Az.Resources)

You can see all the Tags (Key) in your Azure Subscription using this cmdlet.  In the example below, I have two Azure Resources that have an OSDCloud Tag

```powershell
PS C:\> Get-AzTag

Name              Count
----              -----
ms-resource-usage 1    
OSDCloud          2 
```

## Tags Property

PowerShell makes it easy to see which Storage Accounts are used by OSDCloud

```powershell
PS C:\> Get-AzStorageAccount | Select-Object StorageAccountName, Tags
StorageAccountName  Tags                                    
------------------  ----                                    
azosd               {}                                      
azosdcloud          {[OSDCloud, Production]}                
azosdweb            {}                                      
cdsosd              {}                                      
cs710032001c802b70f {[ms-resource-usage, azure-cloud-shell]}
getosdcloudcom      {}                                      
goosdcloudcom       {}                                      
mmsmoa              {}                                      
mmsmoafunction      {}                                      
osdcloudazure       {}                                      
osdclouddemo        {[OSDCloud, Development]}               
ou812               {}                                      
winpe               {}  

PS C:\> Get-AzStorageAccount | Where-Object {$_.Tags.ContainsKey('OSDCloud')} | Select-Object ResourceGroupName,StorageAccountName,PrimaryLocation,SkuName,Tags
ResourceGroupName  : AzOSDCloud
StorageAccountName : azosdcloud
PrimaryLocation    : southcentralus
SkuName            : 
Tags               : {[OSDCloud, Production]}

ResourceGroupName  : OSDCloudDemo
StorageAccountName : osdclouddemo
PrimaryLocation    : southcentralus
SkuName            : 
Tags               : {[OSDCloud, Development]}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deep-dive/azure-tags.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
