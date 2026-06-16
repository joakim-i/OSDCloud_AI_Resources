> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-workspace/set-osdcloudworkspace.md).

# Set-OSDCloudWorkspace

{% hint style="info" %}
**This function requires elevated Admin Rights**
{% endhint %}

{% embed url="<https://github.com/OSDeploy/OSD/blob/master/Docs/Set-OSDCloudWorkspace.md>" %}
Online Help
{% endembed %}

The OSDCloud Workspace can also be set.  This is typically handled automatically when you create a new OSDCloud Workspace, but you can also set this with the **`Set-OSDCloudWorkspace`** function.  Here are some examples

```powershell
[ADMIN]: PS C:\> Get-OSDCloudWorkspace
C:\OSDCloud

[ADMIN]: PS C:\> Set-OSDCloudWorkspace C:\OSDCloudDev
C:\OSDCloudDev

[ADMIN]: PS C:\> Get-OSDCloudWorkspace
C:\OSDCloudDev

[ADMIN]: PS C:\> Set-OSDCloudWorkspace -WorkspacePath C:\OSDCloudProd
C:\OSDCloudProd

[ADMIN]: PS C:\> Get-OSDCloudWorkspace
C:\OSDCloudProd
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-workspace/set-osdcloudworkspace.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
