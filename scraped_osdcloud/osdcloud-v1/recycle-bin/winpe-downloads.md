> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/winpe-downloads.md).

# WinPE Downloads

{% hint style="warning" %}
This media is being shared on a temporary basis only
{% endhint %}

## WinPE Boot Media

The following ISO's are just WinPE with minor changes to support PowerShell Gallery and OSDCloud.  There are no Drivers, and the OSD PowerShell Module is not installed.  You can use these to replace the winpe.wim in your ADK for use with CM or MDT.  This boot media will boot to wpeinit, but you can easily start PowerShell and install your favorite Modules

<figure><img src="/files/23E3k1neZc71zepJgVME" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/xpOyllBl6dQU7vxa4Gdp" alt=""><figcaption></figcaption></figure>

#### Windows 11 22H2 ADK

```
https://winpe.blob.core.windows.net/public/WinPE_Win11_22H2_ADK.iso
```

* Windows 11 22H2 ADK winpe.wim

#### Windows 11 22H2 ADK with KB5026372

{% code fullWidth="false" %}

```
https://winpe.blob.core.windows.net/public/WinPE_Win11_22H2_ADK_KB5026372.iso
```

{% endcode %}

* Windows 11 22H2 ADK winpe.wim
* [2023-05 Cumulative Update for Windows 11 Version 22H2 for x64-based Systems (KB5026372)](https://support.microsoft.com/en-us/topic/may-9-2023-kb5026372-os-build-22621-1702-ce93c18e-e819-458f-abcf-dc7154ce7e40)
* [CVE-2023-24932](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24932)

#### Windows 11 22H2 WinRE

{% code fullWidth="false" %}

```
https://winpe.blob.core.windows.net/public/WinPE_Win11_22H2_WinRE.iso
```

{% endcode %}

* Windows 11 22H2 WinRE
* Supports Wi-Fi
* Supports Recovery Environment

#### Windows 11 22H2 WinRE with KB5026372

```
https://winpe.blob.core.windows.net/public/WinPE_Win11_22H2_WinRE_KB5026372.iso
```

* Windows 11 22H2 WinRE
* Supports Wi-Fi
* Supports Recovery Environment
* [2023-05 Cumulative Update for Windows 11 Version 22H2 for x64-based Systems (KB5026372)](https://support.microsoft.com/en-us/topic/may-9-2023-kb5026372-os-build-22621-1702-ce93c18e-e819-458f-abcf-dc7154ce7e40)
* [CVE-2023-24932](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24932)

## Create a bootable USB Drive

If you have the latest OSD PowerShell Module, use the New-OSDCloudUSB function to create a bootable USB

<figure><img src="/files/GKjPWiW8DQjMlofdcoZb" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/winpe-downloads.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
