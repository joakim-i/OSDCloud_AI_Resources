> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/integration/osdcloud-ipu/windows-in-place-upgrades.md).

# Windows In-place Upgrades

```
Invoke-OSDCloudIPU -OSName 'Windows 11 23H2 x64'
```

Invoke-OSDCloudIPU will check your device, gather several items to know what the correct upgrade media is needed, then download and upgrade.  It will also download a driver pack if found and make available to the setup engine.

Available Parameters:

* \[String] OSName:  Windows Version & Arch
* \[Switch] Silent: Passes the[ /quiet parameter](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-command-line-options?view=windows-11#diagnosticprompt) to the setup engine
* \[Switch] SkipDriverPack: Will skip checking and downloading a driver pack to apply during upgrade
* \[Switch] NoReboot: Passes the[ ](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-command-line-options?view=windows-11#diagnosticprompt)[/noreboot](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-command-line-options?view=windows-11#noreboot) to the setup engine
* \[Switch] DownloadOnly: Will download the media for your device, but not actually trigger upgrade, think of this option like pre-caching
* \[Switch] DiagnosticPrompt: Passes the[ /DiagnosticPrompt](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-command-line-options?view=windows-11#diagnosticprompt) parameter to the setup engine

Items it checks on the local device:

* Current OS Edition (Pro / Home / Enterprise)
* Current OS Language (Get-WinSystemLocale)
* Current OS Activation (Retail / Volume)
* Current OS Architecture (x64 or ARM64)

Based on the OSName you provide, and the OS information gathered from the local machine, it will first download the approrate .esd file to c:\OSDCloud\OS\\($OSName), then it will build the upgrade media needed in c:\OSDCloud\IPU\Media.\
\
Note, during the process, it will check if you have a OSDCloud Flash drive inserted, and pull the esd file from there if available.

Then it will check for and download the driver pack to c:\Drivers

Once all of the content is downlaoded, it will then trigger the upgrade.

\[Place holder for Images]


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/integration/osdcloud-ipu/windows-in-place-upgrades.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
