> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-winpe/psmodule.md).

# PSModule

## PSModuleCopy

This parameter allows me to copy a PowerShell Module from my local computer to WinPE.  I use this frequently in testing an updated OSD Module that I'm working on before publishing it to PowerShell Gallery.  This parameter is also useful if you have your own custom PowerShell Modules that you do not publish in the PowerShell Gallery, but you need them in WinPE.  This is ideal for adding a custom OSDCloud GUI

<figure><img src="/files/zlNt2cK9sPQmDrbz6wtj" alt=""><figcaption></figcaption></figure>

## PSModuleInstall

If you want to add a PowerShell Module that is in the PowerShell Gallery, this parameter will download expand it into WinPE PowerShell Modules

<figure><img src="/files/YmxLsTTI8K0H5FS8vJOK" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-winpe/psmodule.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
