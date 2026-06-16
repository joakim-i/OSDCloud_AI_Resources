> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-vm/get-osdcloudvmsettings.md).

# Get-OSDCloudVMSettings

While you can't change the OSDCloud VM Defaults as those are OSD Module based, you can add OSDCloud VM Settings that overlay over the OSDCloud VM Defaults.  Using the **`Get-OSDCloudVMSettings`** function, you are able to see the current effective settings that are a combination of the following.  In this design, the last entry wins

1. OSD Module Defaults
2. OSDCloud Template Settings
3. OSDCloud Workspace Settings

If you have not made any changes to the Template or Workspace Settings, the current settings should mirror the OSD Module Defaults

<figure><img src="/files/zpeK7XvicsGyciFIpwjZ" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-vm/get-osdcloudvmsettings.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
