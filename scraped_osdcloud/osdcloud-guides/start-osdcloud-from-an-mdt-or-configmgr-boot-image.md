> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-guides/start-osdcloud-from-an-mdt-or-configmgr-boot-image.md).

# Start OSDCloud from an MDT or ConfigMgr Boot Image

You can use OSDCloud with an existing MDT or ConfigMgr Boot Image.

## Requirements

* Boot Image required ADK Optional Components
  * WinPE-WMI
  * WinPE-NetFX
  * WinPE-Scripting
  * WinPE-PowerShell
  * WinPE-StorageWMI
  * WinPE-DismCmdlets
* Internet connectivity
  * OSDCloud PowerShell Module
  * Microsoft Windows 11 ESD
  * OEM Driver Packs
* Device drivers installed in Boot Image

## Boot to MDT or ConfigMgr Boot Image

### MDT Boot Image

In this example, an MDT boot image is used, displaying the Welcome Wizard. You should be able to select "**Exit to Command Prompt**", or press <kbd>**F8**</kbd> to open a command prompt.

<figure><img src="/files/mFpAUUCKjKaV4TqEdwoa" alt=""><figcaption></figcaption></figure>

### Start PowerShell

In the Command Prompt, enter start powershell to open PowerShell in a new window.

<figure><img src="/files/F1JT9MwzY5vshNPwczOR" alt=""><figcaption></figcaption></figure>

### Bootstrap deploy.osdcloud.live

Run the following command in PowerShell to bootstrap OSDCloud

```
Invoke-RestMethod 'https://deploy.osdcloud.live' | Invoke-Expression
```

<figure><img src="/files/nMknun3u1jSYZruDTltW" alt=""><figcaption></figcaption></figure>

### OSDCloud

Deploy-OSDCloud should start automatically

<figure><img src="/files/uF88kOzEmX4604ZOPzI4" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-guides/start-osdcloud-from-an-mdt-or-configmgr-boot-image.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
