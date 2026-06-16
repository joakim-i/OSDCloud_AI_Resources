> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-usb/new-osdcloudusb.md).

# New-OSDCloudUSB

{% hint style="info" %}
**This function requires elevated Admin Rights**
{% endhint %}

{% embed url="<https://github.com/OSDeploy/OSD/blob/master/Docs/New-OSDCloudUSB.md>" %}
Online Help
{% endembed %}

There are two reasons for creating an **OSDCloudUSB**.  The first reason is to simply boot to WinPE and let everything download from the Internet.  The second reason is to support OSDCloud Offline, which works without any internet connection at all

To create an OSDCloud USB, use the **`New-OSDCloudUSB`** OSD function.  This OSD Function is used for both **OSDCloud WinPE** and **OSDCloud Offline**

### Requirements

* [ ] Operating System - To create an OSDCloudUSB from a USB Drive, make sure you are running Windows 10 1703+ or Windows 11.  This minimum requirement is to create a USB Drive with 2 Partitions
* [ ] Admin Rights - Since you need to mess with Disk Partitions, you will need Admin Rights to Clear-Disk and New-Partition

### \[Default] fromWorkspace

To get started, open PowerShell with Admin rights.  Simply enter **`New-OSDCloudUSB`**&#x74;o prepare a new or used USB Drive

You will be presented with a table of the USB Drives that are present on your system, regardless of whether you have 1 or 5.  Simply enter the DiskNumber to make a selection

After selecting a DiskNumber, you will be prompted to Confirm the selection as this is a destructive process.  Once you Confirm, the USB Drive will be Cleared, Initialized, Partitioned, and Formatted.  When the USB Volumes are ready, your OSDCloud Media will be copied to the Boot partition.  The whole process should take between 1-2 minutes to complete

![](/files/SsE0ACMUYnIFNDxromLb)

### fromIsoFile

If you have an OSDCloud ISO, you can use this to create an OSDCloud USB using the **`-fromIsoFile`** parameter

![](/files/GFfiXMLgxyhsyZDJ6AdK)

### fromIsoUrl

If you have an ISO saved on the Internet, you may be able to use the **`-fromIsoUrl`** parameter

![](/files/cGMqjXLHeMpoDoN9cIRy)

{% hint style="warning" %}
This is not guaranteed to work in all situations due to firewall and proxy configuration
{% endhint %}

## USB Content

When you create a new OSDCloud USB, only the WinPE partition will contain files.  If you do not plan on using OSDCloud Offline, you can rename the OSDCloud partition and use it for something else

![](/files/fMixhhFT7q07VKSwJVoh)

## Disk Management

As you can see in Disk Management, the USB Drive will contain two partitions.  The first partition will be the OSDCloud NTFS partition, with the second being the 2GB FAT32 Partition.  Other guides may tell you to create the FAT32 partition first, but they are wrong, and I am right.  For one reason, FAT32 gets corrupted all the time.  Its easier to destroy and recreate at the end of the drive without messing with the NTFS partition.  Secondly, you are free to shrink and extend this smaller partition.  If the partitions were reversed, you would not be able to extend the start point of the second partition without losing all the NTFS data

![](/files/cAwKntK9AcK0awEXe8Kc)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-usb/new-osdcloudusb.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
