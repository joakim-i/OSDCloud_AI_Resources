> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/features/apply-oob-drivers-to-winre.md).

# Apply OOB Drivers to WinRE

Similar to the [Apply OOB Drivers to WinOS](/features/apply-oob-drivers-to-winos.md) feature, this feature will apply the same drivers to the offline WinRE Recovery Image, ensuring that your device will be able to use the Recovery Environment with your existing hardware (disk, network) fully functional.

***

## OSDCloud Comparison

| Function            | Module       | Version   | Status      |
| ------------------- | ------------ | --------- | ----------- |
| **Deploy-OSDCloud** | **OSDCloud** | 25.9.30.3 | **Enabled** |
| Start-OSDCloud\*    | OSD          | -         | Not Planned |

## Feature

In WinPE, OSDCloud will perform the following steps:

* Export the in-use out-of-box drivers to `C:\Windows\Temp\osdcloud-drivers-winpe` using pnputil.exe
* WinRE Recovery Image at `C:\Windows\System32\Recovery\Winre.wim` is mounted
* Drivers in `C:\Windows\Temp\osdcloud-drivers-winpe` are imported to the mounted WinRE Recovery Image
* WinRE Recovery Image is dismounted

<figure><img src="/files/WsJD0PnyK4hwCsM3Xgkq" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/features/apply-oob-drivers-to-winre.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
