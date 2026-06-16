> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/prerequisites.md).

# Prerequisites

### Admin Rights

You are going to be mounting wim files, so yes, this is an absolute with no way around it

For that a function is available, it will allow us to install the following tools :&#x20;

* Terraform for windows
* Bicep for windows
* Azure CLI
* Az.Accounts
* Az.Resources

```
PS > Install-azOSDIacTools
```

![](/files/WFPJpBJYauXJonIb3ew0)

If you launch again the same function we need to find all the version for all tools

![](/files/NtYFtXbDeTad8a6vH5ye)

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/infrastructure-as-code/prerequisites.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
