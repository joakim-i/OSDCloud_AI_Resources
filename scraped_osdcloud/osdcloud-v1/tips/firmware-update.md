> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/tips/firmware-update.md).

# Firmware Update

OSDCloud has the ability to update Device Firmware if it is published in Microsoft Update Catalog.  You can read how this works at this link

{% embed url="<https://osd.osdeploy.com/docs/guides/uefi-system-firmware-update>" %}

## Start-OSDCloudGUI

This feature is enabled (checked) by default when using the OSDCloud GUI

![](/files/rLoVTG7mWqpG74ZUuH6M)

## Start-OSDCloud

When using OSDCloud Command Line, use the Firmware parameter to enable this feature

![](/files/7c9Dj1yOplmJ2UHyENl6)

## Invoke-OSDCloud

When using Invoke-OSDCloud, this feature is controlled by setting the MyOSDCloud Global Variable

```powershell
$Global:MyOSDCloud = @{
	ApplyManufacturerDrivers = $false
	ApplyCatalogDrivers = $false
	ApplyCatalogFirmware = $false
}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/tips/firmware-update.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
