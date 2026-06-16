> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-usb/secure-usb-drives.md).

# Secure USB Drives

If you plan on keeping secure content on your OSDCloud USB, then you should absolutely use a Secure Drive.  I'll add to this page if I come across any other drives that will do, but so far, I have only found one, the Samsung S7 Touch which uses up to 4 Fingerprints to secure the content

## Samsung S7 Touch (500GB - 2TB)

You can skip reading the rest of this page because this is absolutely the USB Drive you should be using for OSDCloud.  This drive is portable, fast, and compatible with both USB-A and USB-C, so it should work on every device in your environment.  Additionally, this USB Drive has a fingerprint sensor to keep things secure.  Finally, once unlocked, this USB Drive is bootable, which makes it perfect for booting to WinPE and using OSDCloud

![](/files/7c1ZFVZXpXEfAAsxdQ9J) ![](/files/C8fCiG1wa00toiZg3N60)

You can read more about this drive from Samsung's website at the following link

{% embed url="<https://www.samsung.com/us/computing/memory-storage/portable-solid-state-drives/portable-ssd-t7-touch-usb-3-2-500gb-silver-mu-pc500s-ww>" %}

## Software Installation

Before this drive can be used securely, you need to setup the Samsung PortableSSD software on a computer.  The software that you need to install is on the drive itself, and can be installed on Windows, as well as Mac and Android

![](/files/NLwemxsbsPB7LXi3nq5J) ![](/files/g1BCJJwziX9iNowBxMKc)

There isn't much to the Windows software, just do your best pressing Next

![](/files/ehSVdCMv6TLYimrb2Lee) ![](/files/ZrtS16i23aVefAW9kGf5)

## Software Configuration

Once the Samsung PortableSSD software is installed, you will need to configure it before the fingerprint sensor will work.  The absolute first thing to check is for Software updates (which may also include Drive Firmware).  One that is complete, you can rename the Drive (I chose my phone number) and enable **Security with Password and Fingerprint**

After setting a Password (I chose a 4-digit PIN) and then scanned my first Fingerprint, my Right Index.  While I could have used any fingerprint, using your Index Finger instead of your Thumb allows you to hold the drive if necessary to get the job done.  You can register up to 4 Fingerprints, which comes in handy if you work in a small team imaging devices.

One important thing to note is that the Password (PIN) allows you to register Fingerprints, so the Password (PIN) can be used to Administer the Drive.  You can't register a new Fingerprint without the Password (PIN)

![](/files/FyQTCSRalaKAvBr2WitH) ![](/files/ix2tNvP5wIZgHtnRWfG0) ![](/files/CyrTRf1wFa5NbL8uwQdG) ![](/files/MrKyE5OfDx9L9kzbshLf) ![](/files/Mu5Pyh105c37YPvUWULq) ![](/files/pHBMx2iFzQggG42DF5Ns) ![](/files/PBloTrJ647L4krsBMB9h)

## OSDCloud Setup

Once you have your Fingerprint setup on the S7 Touch, make sure it is unlocked and run `New-OSDCloud.usb` in PowerShell.  This will wipe the S7 Touch and create WinPE and Data partitions.  You can also run other commands to get OS Images and Driver Packs on the USB Drive.  The following links will get you started

{% content-ref url="/pages/-MW3CFn415hdh7ZF4s94" %}
[New-OSDCloudUSB](/osdcloud-v1/osdcloud/setup/osdcloud-usb/new-osdcloudusb.md)
{% endcontent-ref %}

![](/files/qk3cjidBkOtfY9EL4G0S) ![](/files/l4b8meebI6zvIr4N5pjH) ![](/files/KDOCFGtfdGmlRuvHGj9b)

As you can see from the above image, copying the Windows 11 ESD and a Lenovo DriverPack took 8 seconds (27 seconds with the Sandisk Extreme Pro (USB SSD) and 51 seconds with the Samsung (USB Flash)

| Create (WRITE) | Deploy (READ)       |
| -------------- | ------------------- |
| 8 seconds      | 1 minute 50 seconds |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-usb/secure-usb-drives.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
