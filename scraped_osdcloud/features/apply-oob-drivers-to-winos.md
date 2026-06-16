> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/features/apply-oob-drivers-to-winos.md).

# Apply OOB Drivers to WinOS

This is possibly the most impactful feature of Deploy-OSDCloud in allowing any device to work with OSDCloud. In a nutshell, if your hardware devices work in WinPE (disk, network), they should work in OOBE, allowing you to perform Autopilot or Entra Join, even without a supported DriverPack.

***

## OSDCloud Comparison

| Function            | Module       | Version   | Status      |
| ------------------- | ------------ | --------- | ----------- |
| **Deploy-OSDCloud** | **OSDCloud** | 25.3.27.1 | **Enabled** |
| Start-OSDCloud\*    | OSD          | -         | Not Planned |

## Feature

In WinPE, OSDCloud will perform the following steps:

* Export the in-use out-of-box drivers to `C:\Windows\Temp\osdcloud-drivers-winpe` using pnputil.exe
* Drivers in `C:\Windows\Temp\osdcloud-drivers-winpe` are imported in the offline Windows 11 installation at `C:\`

<figure><img src="/files/Mn1UsS1MoJ238mGVYIWR" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/features/apply-oob-drivers-to-winos.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
