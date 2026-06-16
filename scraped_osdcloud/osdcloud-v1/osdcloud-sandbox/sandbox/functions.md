> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-sandbox/sandbox/functions.md).

# Functions

I've added some functions to help you with customizing Windows in OOBE.  You can access them by running either of the following commands in PowerShell

```
iex (irm sandbox.osdcloud.com)
iex (irm functions.osdcloud.com)
```

The PowerShell Prompt will display **\[OSDCloud]** when they are enabled and ready for use

![](/files/k24FG6N4ooxHMy5KoGap)

{% hint style="info" %}
These functions only exist in the current PowerShell session.  Additionally, they will only work in OOBE at this time, not full Windows
{% endhint %}

## AddCapability

This function will let you add any Windows Capability as needed by GridView, or matching a String

![](/files/CZaFprydmD4TPNK7wwU2)

## NetFX

This should be self explanatory

![](/files/wVxWWNlCodKLdSnvEfmg)

## RemoveAppx

This function will remove Appx Provisioned Packages by matching a string, or displaying a GridView if you do not add a string to the command line

![](/files/SlmtU0s1I3wMnRfLfnKd)

## Rsat

If you are looking to add some Rsat Tools, then this function will either match a string, or display a GridView to select from

![](/files/c0in82OTlryuAb9cU3bi)

## TestAutopilot

This will check to see if an Autopilot Profile has been downloaded to the device

![](/files/DALwk4tJAl8ibTLJ3whT)

## UpdateDrivers

This function will update Hardware Drivers from Microsoft.  `Alt + Tab` to the minimized window to view progress

![](/files/DXsFP94UZGfZFaUmukWY)

## UpdateWindows

This function will do exactly what you think it does.  Windows will be fully up to date including Defender&#x20;

![](/files/ZMTgkjz8RyAdZyK2zwxu)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-sandbox/sandbox/functions.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
