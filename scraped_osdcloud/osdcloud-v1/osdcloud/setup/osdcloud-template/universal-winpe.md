> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/universal-winpe.md).

# Universal WinPE

OSDCloud Template contains a Universal WinPE that can be used with Microsoft Deployment Toolkit and Configuration Manager

If you were to boot the OSDCloud Template, you will see it looks virtually identical to the ADK WinPE

![](/files/-MWUld7RxBhcGha_BJfS)

## Universal WinPE Configuration

* wgl4\_boot.ttf is applied to Media to fix bad display resolution in WinPE UEFI
  * .\Media\boot\fonts\wgl4\_boot.ttf
  * .\Media\efi\microsoft\boot\fonts\wgl4\_boot.ttf
* ADK Packages are installed for .NET and PowerShell support
* Curl.exe is added to $MountPath\Windows\System32
* Setx.exe is added to $MountPath\Windows\System32
* WinPE PowerShell Execution Policy is set to Bypass
* PowerShell Gallery support is added
  * System Variables are added for APPDATA and LOCALAPPDATA
  * PackageManagement
  * PowerShellGet
* Microsoft DaRT is added to WinPE from C:\Program Files\Microsoft DaRT\v10\Toolsx64.cab
  * WinPE winpeshl.ini is removed
  * Microsoft DaRT Config is added from C:\Program Files\Microsoft Deployment Toolkit\Templates\DartConfig8.dat
* Console Registry Changes are applied to mounted Registry (ForceV2, Buffers)
* On Screen Keyboard

**As you can see, nothing OSD, OSDCloud, or OSDeploy has been added to the boot.wim.  This can easily be copied back into ADK for MDT or Config Manager (make a backup of you ADK winpe.wim)**

## On Screen Keyboard

![](/files/-MWjGkUJXVs5HmWbrZ4C)

### Microsoft DaRT

Requires "C:\Program Files\Microsoft DaRT\v10\Toolsx64.cab" and "C:\Program Files\Microsoft Deployment Toolkit\Templates\DartConfig8.dat"

![](/files/-MWQIqVnppecOZH5CW73)

![](/files/-MWQJ3x7-mPrDK_a5vDb)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/universal-winpe.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
