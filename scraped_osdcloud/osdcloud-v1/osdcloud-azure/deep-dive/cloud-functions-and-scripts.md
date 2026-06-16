> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deep-dive/cloud-functions-and-scripts.md).

# Cloud Functions and Scripts

OSDCloud Functions are used to simplify the OSD Process in WinPE and OOBE.  Storing these functions online allows for easy updates without requiring downloading PowerShell Modules or constantly updating WinPE

To import OSDCloud Functions, use the following command

```powershell
iex (irm functions.osdcloud.com)
```

If the OSDCloud functions loaded successfully, you should see version information and the PowerShell Prompt will change to show `[OSDCloud]:`  These functions exist in the current PowerShell session and are unloaded by closing the current PowerShell session

![](/files/dcEZmGxLpHA8YjUob97e)

## Available Functions

Most OSDCloud Functions start with an osdcloud prefix.  You can view these in the current PowerShell session by running the following command

```powershell
Get-Command osdcloud*
```

![](/files/jjJr9KYCv9YLe2zZflLU)

## Why use OSDCloud Functions?

The best example that I can give is that it makes OSDCloud universal.  This allows you to use OSDCloud on any WinPE Boot Image that has PowerShell.  If you have an OSDCloud Boot Image that was created last December, well before OSDCloud Azure, there isn't a need to update the Boot Image since it will self update as part of the OSDCloud Azure deployment

![](/files/a01u6StZkjWx8Ws0CGh7)

Additionally, OSDCloud Functions allows for faster development, and it ensures you are always running the latest version.  To access Azure, you need to be online, so updating OSDCloud components works perfectly in this situation

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deep-dive/cloud-functions-and-scripts.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
