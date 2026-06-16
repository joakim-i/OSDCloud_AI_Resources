> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-live/about/deploy.osdcloud.live.md).

# deploy.osdcloud.live

This endpoint is used to repair issues with WinPE, bootstrap dependencies for OSDCloud, and to start an OSDCloud deployment by invoking Deploy-OSDCloud

## Requirements

* ADK related Boot Image with the following Optional Components
  * WinPE-WMI
  * WinPE-NetFX
  * WinPE-Scripting
  * WinPE-PowerShell
  * WinPE-StorageWMI
  * WinPE-DismCmdlets
* Internet connectivity
* Drivers for boot device

{% hint style="info" %}
For assistance on creating a WinPE boot image, review the following article
{% endhint %}

{% embed url="<https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-adding-powershell-support-to-windows-pe?view=windows-11>" %}

## Boot to a WinPE Boot Image

### MDT Boot Image

In this example, an MDT boot image is used, displaying the Welcome Wizard. You should be able to select "**Exit to Command Prompt**", or press <kbd>**F8**</kbd> to open a command prompt.

<figure><img src="/files/mFpAUUCKjKaV4TqEdwoa" alt=""><figcaption></figcaption></figure>

### Start PowerShell

In the Command Prompt, enter start powershell to open PowerShell in a new window.

<figure><img src="/files/F1JT9MwzY5vshNPwczOR" alt=""><figcaption></figcaption></figure>

### Run deploy.osdcloud.live

Run the following command in PowerShell

```
Invoke-RestMethod 'https://deploy.osdcloud.live' | Invoke-Expression
```

<figure><img src="/files/nMknun3u1jSYZruDTltW" alt=""><figcaption></figcaption></figure>

### OSDCloud

Deploy-OSDCloud should start automatically. Press Start to deploy Windows to this device

<figure><img src="/files/uF88kOzEmX4604ZOPzI4" alt=""><figcaption></figcaption></figure>

## OSDWorkspace Example

A typical boot image created with `OSDWorkspace` 26.2.12+ should already have most of these items resolved.

<figure><img src="/files/js7SdnAjFOaAZkZx4XoV" alt=""><figcaption></figcaption></figure>

## Failure Example&#x20;

This ConfigMgr Boot Image does not have ADK Optional Components for Dism or StorageWMI and cannot be updated online. You will need to rebuild your Boot Image with these components.

<figure><img src="/files/ACAmyJUhS3MmiZG8NI2q" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-live/about/deploy.osdcloud.live.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
