> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/tips/quick-setup.md).

# Quick Setup

{% hint style="warning" %}
**Requires Admin Rights**
{% endhint %}

If you are looking to quickly get OSDCloud running, and you have all the Prerequisites met, then this script should do the job.  This process should take less than 10 minutes to complete

```powershell
#Requires -RunAsAdministrator
#How To: Quick Setup of OSDCloud
#Drivers: All
#Startup: OSDCloudGUI

Install-Module OSD -Force
Import-Module OSD -Force
New-OSDCloud.template
New-OSDCloud.workspace -WorkspacePath C:\OSDCloud
Edit-OSDCloud.winpe -CloudDriver * -StartOSDCloudGUI
New-OSDCloud.iso
```

Here's how things look when you boot to the ISO

![](/files/-Mgl3jZZh-KznlLgHjSZ)

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
GET https://www.osdcloud.com/osdcloud-v1/tips/quick-setup.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
