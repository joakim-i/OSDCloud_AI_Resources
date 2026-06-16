> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/technicien.md).

# Technicien

With OSDCloud we need a technician account to access the storage account in azure as well as the containers. For this we need to reset his ID. This ID will be used in the declarative files of **Bicep** and **Terraform**.

```
PS > get-azOSDTechId -AzureAdUserName OSD -UseDeviceAuthentication
```

![](/files/gmt73GISuIqirpbxk1iu)

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/technicien.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
