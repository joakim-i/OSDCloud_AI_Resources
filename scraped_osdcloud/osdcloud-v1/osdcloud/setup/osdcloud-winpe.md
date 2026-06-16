> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-winpe.md).

# OSDCloud WinPE

## Edit-OSDCloudWinPE

{% hint style="info" %}
**This function requires elevated Admin Rights**
{% endhint %}

{% embed url="<https://github.com/OSDeploy/OSD/blob/master/Docs/Edit-OSDCloudWinPE.md>" %}
Online Help
{% endembed %}

This is the function that is used to edit the WinPE in your OSDCloud Workspace.  The basic design of this function is to edit the Startnet.cmd in WinPE to perform a startup to run OSDCloud

In the example below, the default configuration starts WinPE with 3 windows

1. Startnet.cmd.  Closing this window will cause WinPE to restart
2. Normal PowerShell window.  This is where you should run you OSDCloud commands
3. Minimized PowerShell window.  This is a backup so you can run some commands while OSDCloud is running in the normal PowerShell window

<figure><img src="/files/U5MgEwMTS3DGLbHTrL0R" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-winpe.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
