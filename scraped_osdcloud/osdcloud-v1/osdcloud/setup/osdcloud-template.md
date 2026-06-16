> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template.md).

# OSDCloud Template

Now that you have your Machine Configuration complete, the next thing to do is to create an OSDCloud Template.  This is called a Template as it will be used to create multiple OSDCloud Workspaces (multiple variations).  You'll understand why this is needed over the next few pages

## New-OSDCloudTemplate

{% hint style="info" %}
**This function requires elevated Admin Rights**
{% endhint %}

{% embed url="<https://github.com/OSDeploy/OSD/blob/master/Docs/New-OSDCloudTemplate.md>" %}
Online Help
{% endembed %}

The default OSDCloud Template exists at C:\ProgramData\OSDCloud.  You can create one here using the following command

```powershell
New-OSDCloudTemplate
```

Once you run this command, an OSDCloud Template will be created from the Windows ADK, there's really nothing to it.  If you want to learn more, go through the next few pages


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
