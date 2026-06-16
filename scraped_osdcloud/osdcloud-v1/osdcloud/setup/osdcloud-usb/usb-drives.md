> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-usb/usb-drives.md).

# USB Drives

There isn't a day that goes by that I get asked about what USB Drives should be used for **OSDCloud**, so let me get ahead of the apparent lack of curiosity and detail my findings anyway

![](/files/tIYKmxhZQ3EAbcvOHUhU)

## The Brand

For starters, when it comes to USB Drives, there are only two brands that I use, and that is Samsung and Sandisk, which are the #1 and #2 USB Flash Drive manufacturers respectively.  That said, Sandisk makes a considerable amount of ~~junk~~ budget USB Flash Drives, so the only Sandisk USB Flash Drive that I can recommend is the Extreme Pro

## Size Matters

When it comes to USB Flash Drives, the general rule is that larger is better.  This is because a larger capacity USB Flash Drive has more channels of memory that run in parallel

## Read and Write Testing

I tested each of these drives by creating OSDCloud Offline using Update-OSDCloud.usb.  This command was used to copy Windows 11 VOL (3.46GB) and the Lenovo P17 Driver Pack (1.06GB) for a total of 4.53GB.  Keep in mind WRITE speeds are slower (creating the USB) then the READ speeds (deploying from USB), so there shouldn't be much difference in an OSDCloud deployment since only the copying of the OS and DriverPack to the OSDisk wlil be the only change.  In plain english, the Deployment times consisted of preparing OSDisk, copying the OS and Driver Pack, and expanding the OS.  Of that 2 minutes, only about 5-15 seconds were dependent on the USB Drive speed

## Samsung USB Flash Drives

Samsung makes three USB Drives that can work equally well with booting to WinPE or imaging using OSDCloud.  Each of these drives have a specific purpose, and they are quite inexpensive.  You can find the 32GB drives for about $10, and the 256GB at $40.  The price difference between the 32GB and 64GB is about $3, so I'd opt for the 64GB as the sweet spot.  If speed is important, go with the 256GB.

### Samsung BAR Plus USB 3.1 64GB

This is absolutely the most durable USB Drive that Samsung makes.  You won't break this drive, ever.  Additionally, it is as wide as the USB-A port it plugs into, meaning it will not block any other ports when connected to your computer.  Finally, it has a hole so this can be attached to a keychain.  While the write speeds seemed slow in my example below, this is due to the size tested.  at 64GB, it is 4 x smaller than the other Samsung drives.  If this were a 256GB, I would expect it to perform identically to the other Samsung drives.

| Create (WRITE)       | Deploy (READ)       |
| -------------------- | ------------------- |
| 2 minutes 45 seconds | 2 minutes 2 seconds |

{% embed url="<https://www.samsung.com/us/computing/memory-storage/usb-flash-drives/usb-3-1-flash-drive-bar-plus-64gb-champagne-silver-muf-64be3-am>" %}

### Samsung FIT Plus USB 3.1 256GB

While the Samsung BAR is my favorite for general use, when I am writing code to create USB Drives, I enjoy using the Samsung FIT.  This is because it fits almost flush with my computer, so there isn't much sticking out to get snagged on anything, or to get bent and broken.  This form factor is best used for leaving in a USB port for an extended amount of time.

| Create (WRITE) | Deploy (READ)       |
| -------------- | ------------------- |
| 53 seconds     | 1 minute 57 seconds |

{% embed url="<https://www.samsung.com/us/computing/memory-storage/usb-flash-drives/usb-3-1-flash-drive-fit-plus-256gb-muf-256ab-am>" %}

### Samsung DUO Plus USB 3.1 256GB

I'm only going to recommend this USB Drive if you need it for USB-C, but in all honestly, use a USB-A drive with a USB-C hub or dock.  This USB drive is all plastic and it comes in three pieces.  The USB Drive, a USB-C cap, and a USB-C to USB-A adapter.  You're going lose one or two of these, and you are certain to break the USB drive after some extended use.

| Create (WRITE) | Deploy (READ)      |
| -------------- | ------------------ |
| 51 seconds     | 2 minutes 1 second |

{% embed url="<https://www.samsung.com/us/computing/memory-storage/usb-flash-drives/usb-3-1-flash-drive-duo-plus-256gb-muf-256db-am>" %}

## Sandisk USB SSD

### Sandisk Extreme Pro USB 3.2 256GB

This isn't a Flash Drive like the Samsung drives, this is a legit SSD.  While this sounds great, it will demand a $20 premium over the equivalent Samsung drives.  When imaging a computer, you won't notice much difference, but when you are writing to the drive, it should be twice as fast.

Sadly, while I love the speed of this drive, it is much larger than the Samsung drives.  Additionally, the smoothness of the drive make it hard to get a grip when removing.  Finally, I own three of these drives.  The first was damaged because it got bent when I was trying to remove it, the second is headed to the same fate.  At $60 a pop for 256GB, it won't last longer than the Samsung BAR or FIT.  Pass on this USB Drive.

| Create (WRITE) | Deploy (READ)       |
| -------------- | ------------------- |
| 27 seconds     | 1 minute 51 seconds |

{% embed url="<https://www.westerndigital.com/products/usb-flash-drives/sandisk-extreme-pro-usb-3-2#SDCZ880-256G-A46>" %}

## Conclusion

If you need an USB Drive to boot WinPE, I can only recommend the Samsung USB Drives or Sandisk Extreme Pro, but pick a drive that best suits your purpose

* **Samsung BAR - Rugged.  Ideal for general purpose**
* Samsung FIT - for Development and Long Term use
* Samsung DUO - for USB-C only
* Sandisk Extreme Pro - Don't do it


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-usb/usb-drives.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
