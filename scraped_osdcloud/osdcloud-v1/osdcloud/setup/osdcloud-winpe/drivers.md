> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-winpe/drivers.md).

# Drivers

## CloudDriver

I spent some time automating the download, extraction, and injecting the drivers in OSDCloud's WinPE.  I call these CloudDrivers.  For this parameter I recommend you use install everything with the following command line&#x20;

```
Edit-OSDCloudWinPE -CloudDriver *
```

This will download and inject the following drivers

* Dell Enterprise Driver Cab
* HP WinPE 10 Driver Pack
* Intel Ethernet Drivers
* Lenovo Dock Drivers (Microsoft Catalog)
* Nutanix
* USB Dongles (Microsoft Catalog)
* VMware (Microsoft Catalog)
* WiFi (Intel Wireless Drivers) \[Requires WinRE]

These are handled by mixing and matching the following values

```
Edit-OSDCloudWinPE -CloudDriver Dell,HP,IntelNet,LenovoDock,Nutanix,USB,VMware,WiFi
```

Here's an example using Dell, USB, and Intel WiFi

```
Edit-OSDCloudWinPE -CloudDriver Dell,USB,WiFi
```

![](/files/WdGka6aLy7LmFmfHfzjF)

### DriverHWID

If you have a HardwareID, you can specify that with this parameter.  This will download the appropriate driver from Microsoft Catalog and inject it into WinPE.  Here's an example

```powershell
Edit-OSDCloudWinPE -DriverHWID 'VID_045E&PID_0927','VID_0B95&PID_7720'
```

![](/files/8aI0FLDbgtBjJBKeNRuz)

### DriverPath

Finally, you can use a Driver Path to specify a folder containing driver INF's that you want to install

```powershell
Edit-OSDCloudWinPE -DriverPath 'C:\SomePath'
```

![](/files/5uW8kS5sfrgEQlwhOgh7)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-winpe/drivers.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
