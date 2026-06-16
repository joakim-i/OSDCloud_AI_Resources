> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/tips/using-osdcloud-with-a-windows-iso.md).

# Using OSDCloud with a Windows ISO

OSDCloud now supports installing an Operating System from an ISO, which means you can test drive Windows Insider Editions or even install Windows Server.  This example will show how to install Windows 11 Insider

## Download the Insider ISO

Hit the following link and download whatever ISO you want to flight

{% embed url="<https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewiso?rfs=1>" %}

![](/files/ZFXNBdGDSVEhGYr9nelu)

## OSDCloud USB

Save the Windows Insider ISO to your **OSDCloudUSB** volume in the OSDCloud\OS directory or any subdirectory

![](/files/9VjjRo1fFOJtMPRcxzhF)

## OSDCloud WinPE

Using your OSDCloud USB you can boot to WinPE.  If you **`Start-OSDCloudGUI`**, that will perform a search for ISO files and mount them before the GUI loads

![](/files/ZK1S7BIBpL8Vb1OujlXF)

This will allow you to select the WIM you want to install from the combo box.  You will even be able to select the Operating System Edition to whatever you want

![](/files/-Mi5HsLk_CVxhyJSCMX2)

![](/files/QRdx0tVd1Ogxxa69vRjw)

![](/files/-Mi5I90gG-BDyXtGesSH)

Now you are fully ready to install Windows 11 or Windows Server 2022 and let OSDCloud handle the Drivers

![](/files/-Mi5IUluwUoqDwDJtuKU)

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
GET https://www.osdcloud.com/osdcloud-v1/tips/using-osdcloud-with-a-windows-iso.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
