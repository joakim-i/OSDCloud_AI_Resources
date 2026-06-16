> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-containers/driverpack.md).

# DriverPack

**DriverPack** is an optional Storage Container in your **OSDCloud Storage Account (tagged)** that is used for mirroring vendor Driver Packs. Accounts must have the **Storage Blob Data Reader** role for this Storage Container to download the Driver Packs

It is recommended that you separate Device Manufacturers to help filter the content. This is not a requirement, but this may be added at a later date without warning.  You create these paths during the upload of a Driver Pack

![](/files/ja8Md7T5wjOeZiPP0k6L)

The contents of the dell folder contain Dell Driver Packs that are simply copied without any conversion. This purpose of mirroring the Dell Driver Packs is because downloading content from Dell's site may run slow on occasion, and this allows my deployments to run faster

![](/files/WROEb6ypYHdHfVBF722l)

For Lenovo, I opt to convert the EXE to a ZIP or CAB file and Upload the new file in the Azure Container. This is recommended to allow the Lenovo (HP and Surface) drivers to install in WinPE instead of the Specialize Phase

![](/files/Ztx5WxQitMPiHuoOPP7L)

## Obtaining Driver Packs

You can easily download the DriverPacks that OSDCloud uses to a USB Drive using the following&#x20;

```powershell
Update-OSDCloudUSB -DriverPack *
```

You can use this function to download the Driver Packs you need from any of the Device Manufacturers that are supported by OSDCloud

![](/files/sHvUJLPQIXweJt4wm2dR)

You can then Upload them to the DriverPack Storage Container, or convert the EXE files to CAB or ZIP before uploading

{% hint style="warning" %}
Remember to keep the same BaseName as the original DriverPack as this is what is matched in Azure Storage.  The Extension can be ZIP, CAB, MSI, or EXE
{% endhint %}

## Deployment

During OSDCloud Azure deployment, if a Driver Pack BaseName is matched in the DriverPack Storage Container, it will be downloaded from Azure instead of the Device Manufacturer's site

![](/files/4Atprak1whzXi9k8CALp)

## Sponsor

{% embed url="<https://www.recastsoftware.com/?utm_source=osdeploy&utm_medium=ad&utm_campaign=web>" %}
OSDeploy is sponsored by Recast Software
{% endembed %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-containers/driverpack.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
