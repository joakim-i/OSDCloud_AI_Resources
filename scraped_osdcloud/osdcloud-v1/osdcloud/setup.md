> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup.md).

# Local Setup

## Prerequisites

### Admin Rights

You are going to be mounting wim files, so yes, this is an absolute with no way around it

### Open Internet

You are going to be downloading lots of stuff, so you need Internet access.  There is no Proxy or Firewall configuration in OSDCloud yet, but it is planned

### OSD PowerShell Module

This changes frequently until OSDCloud is working fully, so I recommend that you wash, rinse, and repeat this command frequently

```
Install-Module OSD -Force
```

### PowerShell Capable

Finally, you need to be PowerShell capable, or at least be willing to learn how to use PowerShell.  I do not offer individual training sessions

## Machine Configuration

The first decision you need to make is whether or not you want Wireless to work in WinPE.  If you do, then you must create your OSDCloud Template on Windows 10 as you will be using Windows 10's WinRE.  Windows 11 WinRE isn't compatible with older systems, and virtual machines.

If your HOST Operating System is running Windows 11, you can use the Windows 11 ADK's winpe.wim, or you can create a Hyper-V Virtual Machine and install Windows 10 21H2 and use that

### Install the Windows ADK

Once you have your OS sorted out, you will need to install the Microsoft Windows ADK.  Download the proper ADK and make sure you install the Deployment Tools

{% embed url="<https://docs.microsoft.com/en-us/windows-hardware/get-started/adk-install>" %}

![](/files/SbliLQaqjilAvQoqVRF7) ![](/files/UUKyRJIeYWaKqG84GwlW)

After the ADK Deployment Tools install is complete, download and install the Windows PE add-on for the ADK

![](/files/EfSBCBUwSXtIag90htbS) ![](/files/umYrVxNupqSTtNGAMcgP) ![](/files/cw9ctJTHER3m7Z68iLp7) ![](/files/MsPYXPN3S27XoC3i4try)

### Microsoft DaRT Integration

If you have Microsoft Desktop Optimization Pack 2015, you can install Microsoft DaRT 10.  This will allow you to have DaRT Tools in your OSDCloud WinPE Media

![](/files/l7TPW8EHfy7FwnBYbhxP) ![](/files/oRHwnK6fOY7sznngmGSf) ![](/files/VeljIFGjpW4ShFwM84nw)

### Microsoft Deployment Toolkit

{% hint style="warning" %}
If you don't have DaRT installed, skip this step
{% endhint %}

For DaRT 10 to work in WinPE you will also need a Dart Config file.  The easiest way to get this is to install Microsoft Deployment Toolkit

{% embed url="<https://www.microsoft.com/en-us/download/details.aspx?id=54259>" %}

![](/files/snx5kPqloWv63nPrOqh0) ![](/files/8cUurqdIyGVdC6WmGNMa) ![](/files/8GmCWMsw3Ed4waTfL6sy) ![](/files/nLHxcoqiizfQRhh0BSu2)

### PowerShell

The final steps are to make sure that your Execution Policy is set properly, and to install the OSD PowerShell Module if you haven't already

```powershell
Set-ExecutionPolicy RemoteSigned -Force
Install-Module OSD -Force
```

![](/files/yYDsJb4IeOQ9WPF3bqHL)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
