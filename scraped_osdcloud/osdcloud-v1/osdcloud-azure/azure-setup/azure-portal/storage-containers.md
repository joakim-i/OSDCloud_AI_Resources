> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-containers.md).

# Storage Containers

{% embed url="<https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction>" %}

Storage Containers exist within the Azure Storage Account.  These can be set to be Public, but for the scope of OSDCloud Azure, these should be kept Private and Secure.

## Container Naming

Containers can be named whatever you want them to be to help you organize your Windows Images.  In the example below, I've created Storage Containers to separate the different Windows Image types

![](/files/CuHnpIAdoUWQaQLH8UdW)

Containers can also be named to separate your Teams, there isn't a wrong way to design this

* [ ] Client Image Development Team
* [ ] Client Image Deployment Team
* [ ] Server Image Development Team
* [ ] Server Image Deployment Team

One thing to remember is that each Container can have different Roles for Access

## Create an Images Storage Container

In this example, I will create a simple Storage Container called Images that will contain my Windows Images

![](/files/EZ3Knn3PAZSJT5p9vBvW)

## Upload WIM

Now you can upload a WIM to your images Container. Select Upload and then browse to your WIM.  You will need to select Overwrite since we have not added any Access Control yet, and use the Account key option for the upload

![](/files/5IfFFmWFjTl4t6ZK5c13)

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-containers.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
