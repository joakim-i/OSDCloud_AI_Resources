> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/features/driverpack-catalog-raw-format.md).

# DriverPack Catalog Raw Format

DriverPack Catalogs used by OEMs are in varying formats and are not universal. In previous versions of OSDCloud, these files were compiled and converted into JSON format, known as the OSDCloud DriverPack Catalog. This format sometimes required some time to build before being published in an updated OSDCloud, leading to out of date or unavailable DriverPacks.

DriverPack Catalogs in Raw Format (unmodified) allow for faster updates of OSDCloud to use the latest available OEM DriverPacks.

***

## OSDCloud Comparison

| Function            | Module       | Version  | Status      |
| ------------------- | ------------ | -------- | ----------- |
| **Deploy-OSDCloud** | **OSDCloud** | 26.3.4.2 | **Enabled** |
| Start-OSDCloud\*    | OSD          | -        | Not Planned |

## Feature

In the screenshot below, the DriverPack Catalogs are included their native format in the OSDCloud PowerShell Module. When launching Deploy-OSDCloud, these files are used to generate the DriverPack options for OSDCloud, without the need for a master DriverPack Catalog.

<figure><img src="/files/RMdueNDARiYzMawhOjwM" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/features/driverpack-catalog-raw-format.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
