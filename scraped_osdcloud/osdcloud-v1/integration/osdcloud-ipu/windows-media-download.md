> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/integration/osdcloud-ipu/windows-media-download.md).

# Windows Media Download

```
New-OSDCloudOSWimFile -OSName 'Windows 11 23H2 x64' -OSEdition Pro -OSLanguage en-us -OSActivation Retail
```

This function will reach out and download the appropriate esd file, then build the media sources

Available Parameters:

* \[String] OSName:  Windows Version & Arch
* \[String] OSEdition
* \[String] OSLanguage
* \[String] OSActivation

The command will download the esd file to c:\OSDCloud\OS\\($OSName), and then build the media in c:\OSDCloud\IPU\Media\\($OSName)

First example below is downloading Windows 11 23H2 ARM64.  On this device, I had already downloaded the esd file before, so the function saw it was there, did a SHA1 HASH check, confirmed it was good, and continued to build the media folders and content

<figure><img src="/files/Z9XpnuQAxJGkRbPSGDns" alt=""><figcaption></figcaption></figure>

Second example is grabbing Windows 11 23H2 x64.

<figure><img src="/files/bXtBbvNCWB54AfDOh7Ge" alt=""><figcaption></figcaption></figure>

Here you can see the media below:

<figure><img src="/files/gKtpzxNuSh2z5qqsoT8x" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/puqrtIrNDmzEfdP2xFqU" alt=""><figcaption></figcaption></figure>

Then in ConfigMgr, when I import the install.wim for ARM64, it looks pretty good:\
![](/files/7yxjdkijRzdthkqmXmKg)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/integration/osdcloud-ipu/windows-media-download.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
