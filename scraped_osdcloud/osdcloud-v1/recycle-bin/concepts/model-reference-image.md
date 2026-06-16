> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/model-reference-image.md).

# Model Reference Image

{% hint style="warning" %}
Wait for the next update to the OSD Module before trying this out as these functions have not been released yet
{% endhint %}

OSDCloud provides an absolutely perfect method for creating a Reference Image that supports specific Computer Models, including all the necessary Hardware Drivers.  Additionally, you don't need to create the image on any Hardware, just a Virtual Machine.  Think of this as a Virtual to Physical image

## Virtual Machine Configuration

Create a Hyper-V Virtual Machine with the following configuration

* Generation 2 UEFI
* 2+ Processors
* Fixed (not Dynamic) memory
* 30GB+ Fixed Size (not Dynamically Expanding)
* Disable Snapshots
* Boot to ISO

## Disk Partitioning

Its important that you understand what is required for your Disk Partitions when creating a Reference FFU.  OSDCloud currently configures the Recovery Partition at the end of the disk, but I will be adding Parameters for you to control this

![](/files/-MWrg4OFiBvxrxwOXaOf)

## Start-OSDCloud

OSDCloud supports specifying a specific Manufacturer and Product (SystemSKU, BaseBoard Product).  In this example, I an selecting one for my Lenovo T14

![](/files/-MWrcEpGQTAND0NGYaBY)

If you need to look up a Product value, you can use **`Get-MyDriverPack`**

```
PS C:\> Get-MyDriverPack | FL


Name          : Precision 7730
Product       : 0832
DriverPackUrl : http://downloads.dell.com/FOLDER06809542M/1/7730-win10-A12-6WD5G.CAB
FileName      : 7730-win10-A12-6WD5G.CAB
```

Any of these functions will work as well

```
Get-DellDriverPack
Get-HPDriverPack
Get-LenovoDriverPack
```

## Additional Computer Models

You can easily add additional Dell or HP Driver Packs by using the **`Save-MyDriverPack`** function, or by doing this in Audit Mode.  Adding additional Lenovo Products must be done in Audit Mode due to the way the Driver extracts

![](/files/-MWrdhe_99ShjtnHRUsA)

## Specialize

Once the WinPE phase has completed, the Driver Packs will be expanded and added to the DriverStore using **`PnPUnattend.exe`**

![](/files/-MWreL3d3JKNTWMOq81Q)

## Audit Mode or OOBE

Ideally you should boot into Audit Mode to complete the configuration of the system.  You can do this by executing **`Use-WindowsUnattend.audit`** from WinPE.  I'll work on adding this as a Post Action in OSDCloud in the future

When you have completed your customizations in Audit Mode or in OOBE, execute **`sysprep /generalize /shutdown`**

![](/files/-MWrei10WPzctLCK4e5R)

![](/files/-MWrfHERNsE0xRpGpm7n)

## Create an FFU

Make sure you change your Boot Order in Hyper-V Virtual Machine settings as this will have changed to File.  Boot to OSDCloud.winpe and either Map a Network Drive or insert a USB Drive, then capture an FFU image.  You can easily do this with **`Backup-Disk.ffu`**

![](/files/-MWrfX5n-jd5YgzR4F4q)

## Apply an FFU

Unfortunately I don't have a function to do this (yet), but it should be easy enough to figure out from the following example

```
DISM /apply-ffu /ImageFile=N:\WinOEM.ffu /ApplyDrive:\\.\PhysicalDrive0
```

## Reference

{% embed url="<https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/deploy-windows-using-full-flash-update--ffu>" %}

{% embed url="<https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/wim-vs-ffu-image-file-formats>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/model-reference-image.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
