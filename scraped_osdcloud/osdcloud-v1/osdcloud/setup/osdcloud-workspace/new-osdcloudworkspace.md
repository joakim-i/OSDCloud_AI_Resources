> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-workspace/new-osdcloudworkspace.md).

# New-OSDCloudWorkspace

{% hint style="info" %}
**This function requires elevated Admin Rights**
{% endhint %}

{% embed url="<https://github.com/OSDeploy/OSD/blob/master/Docs/New-OSDCloudWorkspace.md>" %}
Online Help
{% endembed %}

This is the function that will create an OSDCloud Workspace from your active OSDCloud Template.  If you have multiple OSDCloud Templates, it's a good idea to check the one you are currently using and to change it if necessary.  In this example below I'm changing to a patched WinRE as my OSDCloud Template

```powershell
PS C:\> Get-OSDCloudTemplate
C:\ProgramData\OSDCloud\Templates\WinPE KB5026372

PS C:\> Get-OSDCloudTemplateNames
default
Public WinPE
Public WinPE KB5026372
Public WinRE
Public WinRE KB5026372
WinPE
WinPE KB5026372
WinPE Language en Dvorak
WinPE Language en es fr
WinPE Language fr en es
WinRE
WinRE KB5026372

PS C:\> Set-OSDCloudTemplate -Name 'WinRE KB5026372'
C:\ProgramData\OSDCloud\Templates\WinRE KB5026372
```

Now that I've checked my OSDCloud Template, I'll create a new OSDCloud Workspace.  By default, the OSDCloud Workspace is created at C:\OSDCloud but I can change the default by specifying a **`WorkspacePath`**

<figure><img src="/files/EdQLM4XE2qE9NzoDs0Dt" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-workspace/new-osdcloudworkspace.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
