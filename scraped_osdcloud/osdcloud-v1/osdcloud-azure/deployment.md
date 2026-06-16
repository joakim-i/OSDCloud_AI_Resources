> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deployment.md).

# Deployment

If your OSDCloud Azure Setup is complete, and you're run a quick test, here is how to make things work in WinPE.  You will need the **OSD PowerShell Module 22.6.1+**

## OSDCloud Boot Image

If you are using an OSDCloud boot image, then the OSD PowerShell Module should be updated automatically. In a PowerShell prompt, run **`Start-OSDCloudAzure`**.  You will be prompted for Azure Device Authentication

![](/files/nSsSZU9oJum6EYwyICnq)

### Device Authentication Flow

Follow the instructions and authenticate to Azure on a separate device running a full OS (not WinPE) or a Mobile Web Browser

![](/files/XkPelcEV8TcGucdI5cXl)

### Multiple Azure Subscriptions

You may have multiple Azure Subscriptions, you will be required to select one using the crude menu pictured below

![](/files/F7gmBnOlTm8pNL9W6CGp)

### OSDCloud Azure

Once you are connected to Azure, you'll be presented with OSDCloud Azure where you can select an appropriate Operating System

![](/files/Ml9QlgkOTf7VMk6QwLVC)

### Deployment Options

This will change from time to time as more features are added. They should look identical to OSDCloud "Classic"

![](/files/OyZ12f8HAikskcbwjkgB)

### Microsoft Update Catalog

In addition to Network Drivers, Disk and SCSIAdapter Drivers are also downloaded from Microsoft Update Catalog. This is to ensure that you are able to boot to Specialize for EXE Driver Extraction. You have the option to download System Firmware on supported devices as well

![](/files/b4YNnTM1G3FLECSTfrdl)

### Driver Pack

You are able to select a different Driver Pack, Microsoft Update Catalog, or None as needed&#x20;

![](/files/KfJnemF2IET1ZrSF4BDr)

### Start

Once you have sorted out your options, press Start

![](/files/V4xhVNlxaZEhuPveLqVU)

### OSDCloud Variables

Invoke-OSDCloud is the Task Sequence and it is Variable driven. You will see the Variables that you have set prior to starting Invoke-OSDCloud

![](/files/ckKBld3bs6tUrYuYGJ6N)

### Invoke-OSDCloud

The Windows Image or ISO that you selected will be download during this process

![](/files/ld955XaaRwi1OtFur8yP)

### ISO Deployment

If you selected an ISO instead of a WIM, and the Index was set to Auto, you will be prompted to select a Windows Image

![](/files/7Bfbl6vmmnTIKFSvpJPE)

### Complete

If everything worked out properly, within a few minutes you will have a completed OS ready to reboot

![](/files/LhiPRHH9TpH0AX10pnNz)

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deployment.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
