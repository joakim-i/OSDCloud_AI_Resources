> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/features/datetime-internet-sync.md).

# DateTime Internet Sync

Devices that do not have a current DateTime can experience issues with SSL/TLS handshakes whic will cause failures downloading DriverPacks over HTTPS. This issue typically occurs when a device has been disconnected from power for an extended period of time. Additionally, a DateTime that is not correctly set will impact Autopilot or Entra Join.

This feature will set the accurate internet DateTime, regardless of the WinPE TimeZone.

***

## OSDCloud Comparison

| Function            | Module       | Version  | Status      |
| ------------------- | ------------ | -------- | ----------- |
| **Deploy-OSDCloud** | **OSDCloud** | 26.3.4.2 | **Enabled** |
| Start-OSDCloud\*    | OSD          | -        | Not Planned |

## Feature

In WinPE, if the device is connected to the internet, OSDCloud will automatically sync the system clock to the Google's UTC DateTime if the difference is greater than 5 minutes.

In the screenshot below the Windows PowerShell Title Bar displays the existing DateTime. When `Sync-WinPEInternetDateTime` is automatically invoked by `Deploy-OSDCloud`, the device will be automatically set to the current internet DateTime using Set-Date.

{% hint style="info" %}
`Sync-WinPEInternetDateTime` is a private function in the OSDCloud PowerShell Module
{% endhint %}

<figure><img src="/files/DSssrHtWd0aKT92PrXEr" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/features/datetime-internet-sync.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
