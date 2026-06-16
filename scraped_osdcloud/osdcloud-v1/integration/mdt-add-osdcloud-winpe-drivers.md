> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/integration/mdt-add-osdcloud-winpe-drivers.md).

# MDT: Add OSDCloud WinPE Drivers

You can add WinPE Drivers to MDT using **Import-OSDCloudWinPEDriverMDT**.  This function can automatically import the following Manufacturer drivers into MDT

* Dell
* HP
* Lenovo
* Microsoft Surface
* Nutanix
* VMware

Additionally, the following Hardware Drivers can also be added

* Intel Ethernet
* Intel Wireless (Requires WinPE created with WinRE)
* Generic USB
* by HardwareID (Microsoft Catalog)

{% hint style="success" %}
Its a good idea to update your WinPE Drivers from time to time to ensure you have the latest. Simply delete the **OSDCloud WinPE x64** folder from **Out-of-Box Drivers** and repeat this process
{% endhint %}

## Import HP Drivers

In this example, I'll import the HP WinPE DriverPack using the following command

```powershell
Import-OSDCloudWinPEDriverMDT -Driver HP
```

This will download the current HP Client Windows PE 10 x64 Driver Pack, expand the contents, and add it to Out-of-Box Drivers

<figure><img src="/files/kFZvZPhzULo5FdGwhj6C" alt=""><figcaption><p>Import-OSDCloudWinPEDriverMDT -Driver HP</p></figcaption></figure>

## Import All Drivers

In this example, I'll import all available Drivers to MDT using the following command

```powershell
Import-OSDCloudWinPEDriverMDT -Driver *
```

<figure><img src="/files/MN8o8HyiEXfbi2SwuW5v" alt=""><figcaption><p>Import-OSDCloudWinPEDriverMDT -Driver *</p></figcaption></figure>

## Import a Driver by HardwareID

You can also import an individual Driver by using a simiar command line to the example below

```powershell
Import-OSDCloudWinPEDriverMDT -DriverHWID 'VEN_10EC&DEV_5261'
```

<figure><img src="/files/wTFTZQogklBrGmLw5GYM" alt=""><figcaption><p>Import-OSDCloudWinPEDriverMDT -DriverHWID 'VEN_10EC&#x26;DEV_5261'</p></figcaption></figure>

## Out-of-Box Drivers

Drivers will be added to Out-of-Box Drivers automatically in a folder called OSDCloud WinPE x64

<figure><img src="/files/wBRjPsT5GTQh2kcxNdY9" alt=""><figcaption></figcaption></figure>

## Selection Profile

A new Selection Profile named **OSDCloud WinPE x64** will be created containing all the Drivers

<figure><img src="/files/h55Eco4Hcu2kzcm49g1l" alt=""><figcaption></figcaption></figure>

## Deployment Share Update

Now is a good time to set your WinPE **Selection Profile** in your MDT Deployment Share properties to **OSDCloud WinPE x64**.  Once this is complete, you can **Update Deployment Share** to add the WinPE Drivers to your Boot Image

<div><figure><img src="/files/RhNvAvalq0mFDVf46lvo" alt=""><figcaption><p>Include all drivers from the selection profile</p></figcaption></figure> <figure><img src="/files/DBt2v8bHoGNBcy9Qaq4N" alt=""><figcaption><p>Update Deployment Share</p></figcaption></figure> <figure><img src="/files/mCHSdAauo57aR28m1oUB" alt=""><figcaption><p>Completely regenerate the boot images</p></figcaption></figure> <figure><img src="/files/jUxwe6btMBNCIar7Qmzb" alt=""><figcaption></figcaption></figure> <figure><img src="/files/cYvXzPoO9KihqEXYSjXg" alt=""><figcaption></figcaption></figure></div>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/integration/mdt-add-osdcloud-winpe-drivers.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
