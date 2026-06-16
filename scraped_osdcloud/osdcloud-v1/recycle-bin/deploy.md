> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/deploy.md).

# Deploy

Once you boot to the OSDCloud.iso, you will need to install the OSD Module first since it is not installed in the ISO by default. While you can add it, I recommend NOT so that you can always get the latest version

Once the OSD Module is installed, go ahead and change the Display Resolution (Virtual Machine) to your liking

```
Install-Module OSD -Force
Set-DisRes 1600
```

![](/files/-MXmizJYX7JJBuI0MD0S)

## Start-OSDCloud

In the screenshot below, you can see I added the **`-Screenshot`** parameter.  This will be covered at the end of this page.  Once OSDCloud has started, you will go through a series of menus to select the OSBuild, OSEdition, and OSLanguage.  These can be set by Start-OSDCloud parameters

![](/files/-MXmj1H7iD5zWx-b1oJY)

![](/files/-MXmjFEsGNjABnwVImtT)

## Deploy-OSDCloud.ps1

After the Start-OSDCloud (preflight) is complete, the work shifts to Deploy-OSDCloud.ps1.  I'll discuss this further in another page

### AutoPilot Profiles

If you added AutoPilot Profiles to your OSDCloud.template, or in your OSDCloud.workspace, they should be in WinPE.  You can select one, or skip this entirely

![](/files/-MXmjLXMYDjUrbQ6pFV4)

### OSDCloudODT

This is a new addition to OSDCloud where you can inject an Office or M365 ODT Configuration file.  If you enabled this, make a selection or skip this step.  In my example below I have mapped a drive with OSDCloud offline content, so it shows a different directory for the ODT files

{% content-ref url="/pages/-MXmN3jXvihoq06G7yK4" %}
[Enable-OSDCloudODT](/osdcloud-v1/recycle-bin/enable-osdcloudodt.md)
{% endcontent-ref %}

![](/files/-MXmnCH-R3ksu2n1-M5M)

### Clear-Disk.fixed and New-OSDisk

You will be prompted to Clear any Fixed Disks and then a new OSDisk will be created

![](/files/-MXmn_12-R9BeKxajpuH)

### Feature Update

The next step is to download (or copy from USB) the Feature Update ESD and to expand the required Index to C:\\

![](/files/-MXmo24DMzGLB9PImqrb)

### Final Steps

In these last few steps, Drivers are downloaded, as well as the required Unattend.xml Specialize content to expand and installed them.  Office / M365 ODT Configuration and offline Content will be staged, and finally required PowerShell Modules will be applied to the Offline OS

![](/files/-MXmodV-EwesUz9HKONZ)

![](/files/-MXmog9qNtN0o8s5QJos)

![](/files/-MXmoomC7CdkxFVLA3ib)

## Screenshots

They are saved on your Local Disk in C:\OSDCloud\ScreenPNG

![](/files/-MVzUDJSGnpHOwmTy2HK)

{% embed url="<https://www.recastsoftware.com/?utm_source=osdeploy&utm_medium=ad&utm_campaign=web>" %}
OSDeploy is sponsored by Recast Software
{% endembed %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/deploy.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
