> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/about-osdcloud.md).

# About OSDCloud

**OSDCloud** is a Community Tool for deploying Windows 11 (amd64 and arm64) over the internet without using local infrastructure. OSDCloud runs in WinPE using the [**OSDCloud**](https://www.powershellgallery.com/packages/OSDCloud/) or the [**OSD**](https://www.powershellgallery.com/packages/OSD/) PowerShell Modules.

OSDCloud fills a gap for organizations using Intune that still require a solution for bare metal OSD.

<figure><img src="/files/B66AqiZAXqhuUIsqf1up" alt=""><figcaption></figcaption></figure>

## Operating System

Supported versions of Windows 11 (23H2-25H2) for amd64 and arm64 are downloaded directly from Microsoft.

<figure><img src="/files/nClxJh5EfdjQcno65WbF" alt=""><figcaption></figcaption></figure>

## Firmware Updates

Firmware updates are downloaded directly from Microsoft Update Catalog and applied after rebooting from WinPE.

<figure><img src="/files/IJflqqPyOYQb2YF2Lw68" alt=""><figcaption></figcaption></figure>

## Drivers and DriverPacks

Drivers are downloaded directly from Microsoft Update Catalog, and DriverPacks from Dell, HP, Lenovo, and Microsoft Surface are downloaded directly from the OEMs.

<figure><img src="/files/DR9TAGaveYKKcHyFZZNf" alt=""><figcaption></figcaption></figure>

## OOBE Autopilot Ready

Finally, local PowerShell Modules are updated so you can immediately start using your device in OOBE.

<figure><img src="/files/m1PFU7jzOQE1KcDcmQlj" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/about-osdcloud.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
