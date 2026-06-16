> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-sandbox/sandbox/oobe-usage.md).

# OOBE Usage

**OSDCloud Sandbox** is configured to get all your **Autopilot** requirements in **OOBE** (Out-of-Box Experience).  This process works in both Windows 10 and Windows 11

![](/files/2xXCbPwukvYT59Z9X8sk)

## Network Requirements

You will need an internet connection before getting started.  If you need to connect to a Wireless Network, open Windows Settings by pressing`Shift + F10` to open a Command Prompt.  Type in the following command line and press enter

```
start-ms-settings:
```

![](/files/H3KDIQPyIHhmSgdtLT6c)

## Command Prompt

Press `Shift + F10` to open a Command Prompt.  Type in the following command line and press enter to start **OSDCloud Sandbox**

{% code title="Command Prompt" %}

```powershell
powershell iex(irm sandbox.osdcloud.com)
```

{% endcode %}

![](/files/L2DGuUcolFZHgRslW1GN)

## Windows Settings

You will be prompted to verify some Windows Settings during this process.  **OSDCloud Sandbox** will continue after closing the open Windows Setting

{% hint style="info" %}
You can navigate in Windows Settings to access other things like Networking and Wireless
{% endhint %}

### Display Settings

This is the first Windows Setting that will open.  This comes in handy when you want to expand the screen of a Virtual Machine for screenshots.  **OSDCloud Sandbox** will continue when you close Display Settings

![](/files/ubrWFWvVTuDm8nTR3k1a)

### Language and Region

This Windows Setting will allow you to add additional Languages or a Keyboard Layout if necessary

![](/files/HdmDUGSqU9Kqt3KU59cN)

### Date and Time

This is probably the most important Windows Setting as this allows you to set the Time Zone for your location and to sync the clock.  It is essential if you want to ensure that Autopilot registers and that certificates work properly

![](/files/fDgEkzGAwQnwq0rV7ue2)

## Autopilot Ready

All the required PowerShell Modules and Scripts needed for **Autopilot Registration** are installed and ready to go

![](/files/Be9mbEl1aZPs7wr4Gzsp)

## Get-WindowsAutopilotInfo

To register the device in **Windows Autopilot**, use the following steps (with your own parameters)

{% code title="Command Prompt" %}

```
start PowerShell
```

{% endcode %}

{% code title="PowerShell" %}

```powershell
Get-WindowsAutopilotInfo -Online -GroupTag <YourGroupTag>
```

{% endcode %}

![](/files/zPrgKGDBwdll0tHqsz8O)

![](/files/o0ZfQSBjn2bPFnjoz7iT)

## Autopilot Registered

If the device is already **Autopilot Registered** (or has an **AutopilotConfigurationFile.json**), then **OSDCloud Sandbox** will display your **Autopilot Configuration** automatically.  This is good for validation

![](/files/4ylK2NPhxuq02glrqy1I)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-sandbox/sandbox/oobe-usage.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
