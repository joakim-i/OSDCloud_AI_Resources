> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-access-control-iam.md).

# Storage Access Control (IAM)

## Reader

{% embed url="<https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader>" %}

For OSDCloud to work with Azure Storage, the Technician will need Reader access to the Storage Account.  This allows for the reading of Tags which are used by OSDCloud, and the listing of the Containers

![](/files/5OHohLCrshCMVwyLL8Tf)

## Storage Blob Data Reader

{% embed url="<https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-reader>" %}

Additionally, the Storage Blob Data Reader must be added for the Containers in the Storage Account that contains the WIM files.  This can be added at the Storage Account level, or a specific Container

![](/files/Mkdsgg4lwNgsLYEhGm26)

## Azure Role Assignments

Verify the proper permissions in Azure Active Directory

![](/files/Rxyavngh3kYykmsUv1Ik)

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-access-control-iam.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
