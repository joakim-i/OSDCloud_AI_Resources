> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-workspace/get-osdcloudworkspace.md).

# Get-OSDCloudWorkspace

{% embed url="<https://github.com/OSDeploy/OSD/blob/master/Docs/Get-OSDCloudWorkspace.md>" %}
Online Help
{% endembed %}

It's a good idea to remember how to know what your current OSDCloud Workspace is.  You can find out with this function.  On a system that has never created an OSDCloud Workspace, you will receive the following Warning and nothing will be returned

```powershell
PS C:\> Get-OSDCloudWorkspace
WARNING: 2022-02-22-223047 Unable to locate C:\ProgramData\OSDCloud\workspace.json
```

Here is an example of how to test if you have an OSDCloud Workspace

```powershell
PS C:\> if (Get-OSDCloudWorkspace) {$true} else {$false}
WARNING: 2022-02-22-223256 Unable to locate C:\ProgramData\OSDCloud\workspace.json
False
```

Ideally, you should get a path returned if you have an OSDCloud Workspace

```powershell
PS C:\> Get-OSDCloudWorkspace
C:\OSDCloud
```

{% hint style="info" %}
The current OSDCloud Workspace is stored in the OSDCloud Template at `C:\ProgramData\OSDCloud\workspace.json`
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-workspace/get-osdcloudworkspace.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
