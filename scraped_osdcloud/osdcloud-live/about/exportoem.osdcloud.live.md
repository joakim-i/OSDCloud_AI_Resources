> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-live/about/exportoem.osdcloud.live.md).

# exportoem.osdcloud.live

This endpoint is used to export OEM Drivers from Windows 11.

The exported oem drivers can then be added to your WinPE Boot Image to allow support for your device, or they can also be used in a Task Sequence to inject into your offline Windows OS.

This script will export drivers that are in-use, meaning there is hardware present that is using this specific driver.

## OEM Drivers

OEM Drivers are added to Windows to support device hardware. These drivers are also known as **Out-of-Box Drivers** as they were not included in the Windows 11 OS. Drivers that are included in the Windows 11 OS by Microsoft are referred to as **Inbox Drivers**.

**OEM Drivers** are located at **C:\Windows\INF** and are identified with the naming pattern **`oem*.inf`**

<figure><img src="/files/bKesO0qqQfl7dONpYzrE" alt=""><figcaption></figcaption></figure>

### Device Preparation

It is recommended that you allow Windows to fully install to your device, and use Windows Update or a Driver Pack to install drivers for all the hardware on your device, including attached devices such as a docking station.

i.e. Completely setup Windows on your device as soon as you unbox it

### Run exportoem.osdcloud.live

Run the following command in PowerShell as Administrator

```
Invoke-RestMethod 'https://exportoem.osdcloud.live' | Invoke-Expression
```

OEM Drivers will be exported to the following path

```powershell
$env:TEMP\exportoem
```

When the exportoem script is complete, Windows Explorer will open the above path

<figure><img src="/files/D9ebelBpsNIhHr7xwqLA" alt=""><figcaption></figcaption></figure>

Two folders will have been created in the exportoem folder. The folder with the winpe prefix is smaller in size and can be used in your WinPE Boot Image.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-live/about/exportoem.osdcloud.live.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
