> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deployment/osdcloudre-azure.md).

# OSDCloudRE Azure

This tool is designed to run in Windows and create a new Recovery Partition.  The Recovery Partition will be prepared with the Boot Image ISO that is downloaded from Azure Storage

{% hint style="warning" %}
The goal of this tool is to allow booting to OSDCloud in a Recovery Partition so you can immediately image the device without a USB. It is not intended to create a permanent OSDCloud Recovery Partition

There are no plans to create functions to remove or resize the OSDCloudRE Partition
{% endhint %}

## BootImage Container

Create a BootImage Storage Container and upload an OSDCloud ISO.  Read the following link for more information

{% content-ref url="/pages/opvRZXabwXXqzgXggNZJ" %}
[BootImage](/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-containers/bootimage.md)
{% endcontent-ref %}

## Start-OSDCloudREAzure

Open PowerShell as Admin and run this function. You will be prompted to authenticate to Azure

![](/files/MjN3LaqdgAK1LtwfZ105)

Once authenticated, OSDCloud Storage Accounts with BootImage Containers will be enumerated. If an OSDCloud ISO or Boot Image ISO is found, the OSDCloudRE Azure GUI will be displayed. You are able to select from multiple files if you have any

![](/files/U64faK7KCpCENxq92e7c)

It's important to note that when the process is completed, the computer will reboot automatically. Deselect the Restart-Computer option in the Build Options file menu

![](/files/AmMKIJmbNxGep1VHcGNW)

Press the Start button when you are ready to continue

## Process

The ISO will be downloaded from Azure Storage. This step should take less than a minute to complete

![](/files/9B29eJdpcLXaFHeyhLU7)

Once the ISO has been downloaded, it will be mounted and the contents will be copied to the new OSDCloudRE Partition.  On next boot, Windows Boot Manager (bootmgr) will be set to boot to the OSDCloudRE Partition

![](/files/LLvxWLPHhPOFbAXRZtvz)

If you view Disk Manager, you will see the secondary Recovery Partition which is created immediately after the Windows Partition

![](/files/JgulcKQx6YwNLDOlg7Cv)

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deployment/osdcloudre-azure.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
