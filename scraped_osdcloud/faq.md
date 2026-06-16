> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/faq.md).

# OSDCloud FAQ

## What is OSDCloud?

OSDCloud is a tool to deploy Windows Operating Systems, without a network infrastructure (servers). Windows Image and OEM Driver Packs are downloaded at runtime. This method is also considered Cloud OS Deployment.

## What Operating Systems are supported?

Windows 11 23H2/24H2/25H2 x64 (both amd64 and arm64)

## What Devices are supported?

Any UEFI device compatible with Windows should work with OSDCloud.

## What are some OSDCloud use cases?

OSDCloud is used to reimage a device.

* Preparing a device for Windows Autopilot as Intune does not have a method to apply an image to a not-existing device. Intune is used for preparing existing devices with a Reset or a Refresh.
* Replacement for existing OS Deployment technologies, such as MDT or ConfigMgr
* Disaster Recovery in cases where existing methods may be compromised
* Hardware replacement without an OS. For example, installing a new disk which contains no existing Operating System.

## What are the Requirements?

As OSDCloud is run from WinPE (Windows Preinstallation Environment), many of these dependencies need to be included in WinPE, typically by mounting and injecting the dependencies.

* WinPE Boot Image. Can be built using the Windows ADK, MDT, ConfigMgr, OSDCloud (Cmdlets) or OSDWorkspace.
* Boot Method. Typically this is a USB Drive, but can be ISO for a VM, CD/DVD ROM for drives, or PXE for Network Boot.
* Hardware Drivers. These should be injected in the WIM Boot Image and should support the device hardware.
* Internet access. Windows Images are downloaded from Microsoft. DriverPacks are downloaded from OEMs (HP, Dell, Lenovo, Microsoft Surface).
* curl.exe (WinPE)
  * Used for downloading large files. This is not included in WinPE by default.
* PowerShell (WinPE)
  * This is added to WinPE by the Windows ADK.
* PowerShell Cmdlets (WinPE)
  * Dism for applying the Windows Image. This is added to WinPE by the Windows ADK.
  * Storage for disk partitioning and formatting. This is added to WinPE by the Windows ADK.
* PowerShell Modules (WinPE)
  * OSDCloud <https://www.powershellgallery.com/packages/OSDCloud/>
  * OSD <https://www.powershellgallery.com/packages/OSD/>
* PowerShell functionality (WinPE)
  * PowerShell should be able to install and update PowerShell Modules.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/faq.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
