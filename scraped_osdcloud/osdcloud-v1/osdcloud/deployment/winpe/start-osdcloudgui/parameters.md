> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/deployment/winpe/start-osdcloudgui/parameters.md).

# Parameters

This is the default OSDCloudGUI.  There are a few parameters that you can use for minimal customization

<figure><img src="/files/cZFXfO481EhcxAwadJVv" alt=""><figcaption></figcaption></figure>

## -BrandName

Change the Brand Name

```powershell
Start-OSDCloudGUI -BrandName 'MMSMOA2023'
```

<figure><img src="/files/9YsPqfwFeIpeS9vzoOVF" alt=""><figcaption></figcaption></figure>

## -BrandColor

Change the Brand Color

```powershell
Start-OSDCloudGUI -BrandColor '#ED1C24'
```

<figure><img src="/files/t9A3cjeBsJ0S2ytnH7ir" alt=""><figcaption></figcaption></figure>

## -ComputerManufacturer

This parameter is helpful in testing Manufacturer customizations in a Virtual Machine.  You can see the Manufacturer displayed in the Title Bar

```powershell
Start-OSDCloudGUI -ComputerManufacturer 'HP'
```

<figure><img src="/files/aXd1romRIZx1TDLdQ6SE" alt=""><figcaption></figcaption></figure>

## -ComputerProduct

OSDCloud matches the Driver Pack based on the computer Product.  This parameter is helpful for testing a Driver Pack on a Virtual Machine.  You can see the Computer Product displayed in the Title Bar

```powershell
#HP Dragonfly G2
Start-OSDCloudGUI -ComputerProduct '8716'
```

<figure><img src="/files/qrOzEdaDFFuKMWgvDx67" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/deployment/winpe/start-osdcloudgui/parameters.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
