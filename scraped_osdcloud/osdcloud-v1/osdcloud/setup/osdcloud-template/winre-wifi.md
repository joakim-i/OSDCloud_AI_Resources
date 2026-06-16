> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/winre-wifi.md).

# WinRE WiFi

In addition to using the winpe.wim that is in the ADK, you can also create an OSDCloud Template using WinRE

## -WinRE

To do this, use the `WinRE` parameter.  The benefit of using WinRE is you gain Wireless support.  One thing you need to remember is that the ADK you are using needs to match your running OS, so if your OS is Windows 11 22H2, you need to use the ADK for Windows 11 22H2.  Finally, make sure you use the `Name` parameter to keep things tidy

In my example below, you can see the WinPE-WiFi Packages that come with WinRE

<figure><img src="/files/Y9sP9kCA1kTcwnQdPtmy" alt=""><figcaption><p>New-OSDCloudTemplate -Name WinRE -WinRE</p></figcaption></figure>

## Additional Information

{% embed url="<https://msendpointmgr.com/2018/03/06/build-a-winpe-with-wireless-support/>" %}

{% embed url="<https://github.com/okieselbach/Helpers/tree/master/WirelessConnect>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/winre-wifi.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
