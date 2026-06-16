> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/configure-azure.md).

# Configure Azure

## Admin Right

You are going to be mounting wim files, so yes, this is an absolute with no way around it

## Function

For this we have a single function **invoke-AzOSDAzureConfig** that admits several *parameters*. It has two **parameterSetName** one for Bicep and one for Terraform

* <mark style="color:blue;">**ParameterSetName Bicep**</mark>
* Location : corresponding Azure region
* ResourceGroupName : corresponding the resource group create in Azure

```
invoke-AzOSDAzureConfig -Location westeurope -ResourceGroupName osdclouddemo
```

* <mark style="color:blue;">**ParameterSetName Terraform**</mark>
* UseTerraform : Is boolean parameter

```
PS C:\Users\JM2K69> invoke-AzOSDAzureConfig -UseTerraform $true
```

The function uses the command *Connect-AzAccount -UseDeviceAuthentication* for the authentication part with <mark style="color:purple;">**Bicep**</mark> and for the <mark style="color:purple;">**Terraform**</mark> part we will use ***Azure Cli*** with *az login --use-device-code*

## Terraform execution

### Terraform.tfvars&#x20;

```
osdcloud_containers = ["server", "retail", "insiders", "driverpack", "bootimage"]
osdscript_containers = ["scripts", "packages", "unattend", "others"]
osdcloud_resourcegroup = "AzOSDClouddemo"
osdcloud_StorageAccountOSDScripts = "osdscriptsdemo"
osdcloud_StorageAccountOSDCloud = "osdclouddemo2"
osdcloud_Location = "westeurope"
subscription_id = "9b288c1f-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
technicien_id = "1618bbc9-bdce-45af-a3bd-a86c224d8094"
tenant_id = "d1c6xxxx-d6xx-4xx-xxxx-313xxxxxxx86be"

```

### Execution

![](/files/zcrGPZTgIc9xbuj0AH31)

![](/files/Os29lrqaw0vetpzlwwfF)

### Verify in Azure

#### Resource groups

![Resource Group in Azure portal](/files/1OlPsiG0M4nqsj910eC6)

#### Storage account properties

![Tag, all properties are set.](/files/OgpnnvgSI7UME4Kysg6d)

#### Acces Control (IAM)

![](/files/YLE3cvk1QgBruTtbZ7LH)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/configure-azure.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
