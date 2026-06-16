> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal.md).

# Azure Portal

This section is going to detail how to run OSD from Azure Storage.  If you know nothing about Azure Storage, then you may find this helpful

{% content-ref url="/pages/WGVfnthP0rSyBTDVD51v" %}
[Storage Accounts](/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-accounts.md)
{% endcontent-ref %}

The first thing you will need to create is a Storage Account.  Think of this as your Deployment Server.  Your Azure environment may consist of one or hundreds of Storage Accounts which are used for all kinds of things, such as Azure Functions, or Web Services.  For OSDCloud to find the correct Storage Account to use, the Storage Account contains a Tag, which is a Key Value pair.  OSDCloud ignores all Storage Accounts that do not have a Tag Key of OSDCloud (the Value doesn't matter yet, just the Key).  For the Tag to be read, the Deployment User needs to have Reader role on the Storage Account.  This design makes it able to find the proper Storage Accounts to use for OSDCloud in generally less than a second.

{% content-ref url="/pages/XZXZh8kVYp4GJrJQhR8w" %}
[Storage Containers (Public)](/osdcloud-v1/recycle-bin/storage-containers-public.md)
{% endcontent-ref %}

{% content-ref url="/pages/9s3DjjWqEfDIxNki00UO" %}
[Storage Containers](/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-containers.md)
{% endcontent-ref %}

Storage Containers exist within a Storage Account.  Think as these as Deployment Shares, which can either be Public or Private.  It may be quite helpful to put a WinPE Boot ISO that contains no sensitive information in your Public Storage Container, or don't may one at all.  Public Storage Containers are optional, OSDCloud doesn't need them

What OSDCloud does need are Storage Containers with WIM files (ISO support is coming soon).  These should be kept in a Private (Secure) Storage Container.

Files that exist in the Storage Containers are called Blobs.  In the scope of OSDCloud, these Blobs would be WIM files.  The only role that is needed to access the Blob is Storage Blob Data Reader

When you are ready to set the required access to your Storage Account and Storage Containers, review the following page

{% content-ref url="/pages/XVioZRw2WDNpcfIvWHqi" %}
[Storage Access Control (IAM)](/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-access-control-iam.md)
{% endcontent-ref %}

Once you have these steps complete, simply upload your WIM files into your Storage Containers and they will be ready for OSDCloud to use.  For now, only Image Index 1 is used, but more functionalities will be added soon, including a GUI

Feedback is critical at this point as this is being designed from scratch.  If you have some ideas for improvement, please reach out

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
