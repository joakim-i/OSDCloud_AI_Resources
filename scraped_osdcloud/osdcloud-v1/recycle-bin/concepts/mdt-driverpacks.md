> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/mdt-driverpacks.md).

# MDT DriverPacks

{% hint style="info" %}
This feature will be completed and released in mid April, as well as a Driverless MDT using OSDCloud's DriverPacks
{% endhint %}

**Will you still use Out-of-box-Drivers when you can use Driver Packs in MDT?**

As OSDCloud has demonstrated, it is easy to pull Drivers from the Cloud, but its also designed to search for the required files locally in the case an of OSDCloud.usb.  I wanted to give you an example of how DriverPacks can replace Out-of-box-Drivers in MDT by using some of the concepts of OSDCloud, like Specialize DriverPacks

{% content-ref url="/pages/-MWrFbEgR1O-u0rrENEH" %}
[Specialize DriverPacks](/osdcloud-v1/recycle-bin/concepts/specialize-driverpacks.md)
{% endcontent-ref %}

## Deployment Share

The Deployment Share should be configured with a DriverPacks directory.  The folder structure doesn't matter at all

![](/files/-MWtrELMBrAv1dalVrUi)

## OSD Module

For this to work properly, you will need the OSD Module in WinPE, as well as in the Offline OS BEFORE you restart from WinPE.  I'll work on a new function to copy it to an Offline OS, similar to **`Copy-PSModuleToFolder`**

## Task Sequence

A single Command Line step is needed to get the proper Driver Pack name and search for it in the DriverPacks folder.  In this step, I have the Command line set to the following

```
PowerShell.exe -Command Add-OSDMDTDriverPack
```

This may likely change before it is finalized for release

![](/files/-MWtqVZUaGGR2jmzSdED)

## Unattend.xml

You will need to add this code to the Specialize pass of your Unattend.xml.  This is what launches the Expand-StagedDriverPack function

```
<RunSynchronousCommand wcm:action="add">
    <Order>5</Order>
    <Description>Expand-StagedDriverPack</Description>
    <Path>Powershell -ExecutionPolicy Bypass -Command Expand-StagedDriverPack</Path>
</RunSynchronousCommand>
```

![](/files/-MWtpJekVKrMaKcmCgy6)

This is how it looks in an MDT Deployment, staged to C:\MININT\Unattend.xml

![](/files/-MWtoohmAPHB9v0O4dRD)

## Deployment Process

You really shouldn't notice anything different during the MDT Deployment process.  here are some screenshots anyway

![](/files/-MWtnzaupKzKjto4z8e0)

![](/files/-MWto3FPBNkfnYAUOQfQ)

![](/files/-MWto5TRNIRaaefB3Gii)

![](/files/-MWts51HwuTm211tOkXl)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/mdt-driverpacks.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
