> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/release.md).

# Release Notes

## 21.11+ November Update

![](/files/DVCmstCLaPP6E0CEgu6J)

### New Pages

{% content-ref url="/pages/LEHpPvN1uZWtzDjzHaxw" %}
[Firmware Update](/osdcloud-v1/tips/firmware-update.md)
{% endcontent-ref %}

### Updated Pages

{% content-ref url="/pages/-MVUKpo37jZaOpoF1AoE" %}
[Broken mention](broken://pages/-MVUKpo37jZaOpoF1AoE)
{% endcontent-ref %}

{% content-ref url="/pages/-MginbxGF-lVRsBMtfhK" %}
[Quick Setup](/osdcloud-v1/tips/quick-setup.md)
{% endcontent-ref %}

{% content-ref url="/pages/-MVzHdFvdqGIEVJC9FOQ" %}
[OSDCloud Template](/osdcloud-v1/osdcloud/setup/osdcloud-template.md)
{% endcontent-ref %}

{% content-ref url="/pages/-MVzK3ISEWm30EgCTeGD" %}
[Configuration Files](/osdcloud-v1/osdcloud/setup/osdcloud-workspace/configuration-files.md)
{% endcontent-ref %}

{% content-ref url="/pages/-MVzK\_o-xGl49jwx5-Vn" %}
[OSDCloud Workspace](/osdcloud-v1/osdcloud/setup/osdcloud-workspace.md)
{% endcontent-ref %}

{% content-ref url="/pages/-MVzM277SWCnSBWy3isj" %}
[OSDCloud ISO](/osdcloud-v1/osdcloud/setup/osdcloud-iso.md)
{% endcontent-ref %}

## 21.10.20 October Update

This update for OSDCloud is all about Drivers.

* **Invoke-ParseDate bug may have been resolved**
* **Edit-OSDCloud.winpe**
  * CloudDriver Dell updated from A24 to A25
  * CloudDriver Dell no longer imports 32-Bit Drivers
  * CloudDriver HP updated from sp110326.exe to sp112810.exe
  * CloudDriver WiFi (Intel) updated from 22.50.1 to 22.80.1
* **Start-OSDCloudGUI**
  * Apply Manufacturer Drivers
    * Checked by Default (True)
  * Apply Microsoft Catalog Drivers
    * Checked by Default (True)
    * By default, if Manufacturer Drivers are found and downloaded, Microsoft Catalog Drivers defaults to updating Network Drivers only
  * Apply Microsoft Catalog Firmware
    * Checked by Default (True)

Parameters to control Driver functionality is not being added in Start-OSDCloud (Command Line) at this time to allow for proper feedback from the Start-OSDCloudGUI changes. As an override to directly control this behavior in Invoke-OSDCloud, use the following Global Variable in the same PowerShell session

```powershell
$Global:MyOSDCloud = @{
	ApplyManufacturerDrivers = $false
	ApplyCatalogDrivers = $false
	ApplyCatalogFirmware = $false
}
```

## 21.8.10 August Update

There typically aren't any Release Notes for OSDCloud as they are bundled in with the OSD Module, but this release has quite a few changes, so it's important to get through them

## OSDCloud Config Files

Autopilot Profiles are being relocated.  Review the following link

{% content-ref url="/pages/-MVzK3ISEWm30EgCTeGD" %}
[Configuration Files](/osdcloud-v1/osdcloud/setup/osdcloud-workspace/configuration-files.md)
{% endcontent-ref %}

In previous releases, the Autopilot Profiles were located in the following location

```
C:\ProgramData\OSDCloud\Autopilot\Profiles
```

While this made sense in the beginning, the addition of other configuration for AutopilotOOBE and OOBEDeploy makes it necessary to bundle files used for configuration into a proper parent directory

The next time you update your OSDCloud Template you will receive a Warning (and a short delay).  This Warning will continue (and the delay will increase in the future) until you remove **C:\ProgramData\OSDCloud\Autopilot** manually

![](/files/-MgZ3MI6BHN774UGKo2H)

![Remove these directories!](/files/-MgZ35Anp-C0yoRUUVBJ)

## Template and Workspace Issues

You will be unable to create or update an OSDCloud Workspace until the Autopilot Profiles are moved in both your OSDCloud Template and your working OSDCloud Workspace

![](/files/-MgZC4X-IURsOkcH1UgH)

This change will impact the following commands

```
New-OSDCloud.workspace
Edit-OSDCloud.winpe
```

## ODT Changes

I plan on phasing out the Office 365 installation during the Specialize phase in the next few weeks.  Pleae contact me if you use this and I'll help you come up with a workaround.  There are no changes ODT in this release

## Edit-OSDCloud.winpe

I strongly recommend rebuilding your WinPE by rebuilding your OSDCloud Template and OSDCloud Workspace to ensure full compatibility with the new changes in WinPE

### Drivers

In addition to the **`CloudDriver`** and **`DriverPath`** parameters, you now have the option to use the **`DriverHWID`** parameter to ensure that a driver for a specific Hardware ID is installed.  All three Driver parameters are arrays, so you can add multiple options for each parameter

```
$Params = @{
    CloudDriver = 'Dell','WiFi'
    DriverHWID = 'PCI\VEN_8086&DEV_2526','PCI\VEN_8086&DEV_15BB'
    DriverPath = 'D:\OSDCloud\Drivers\Chipset','D:\OSDCloud\Drivers\SATA'
}
Edit-OSDCloud.winpe
```

When using DriveHWID, the driver will be downloaded from Microsoft Update Catalog and added to WinPE.  This feature has been present in the OSD Module for the last month, but has not been fully documented yet

![](/files/-MgZKF1O9ImXmAcuR1kp)

### Startup

There are several changes to the WinPE startup, so I hope you can keep up

#### StartOSDCloudGUI

This parameter will add **`Start-OSDCloudGUI`** to the Startnet.cmd

```
Edit-OSDCloud.winpe -StartOSDCloudGUI
```

![](/files/-MgZRgjMxFXAaFKmOub4)

**`Start-OSDCloudGUI`** will automatically minimize the Startnet.cmd window

![](/files/-MgZTmIUnSITvG5V-Dss)

#### StartOSDCloud

If you prefer to stick to the Command Line, then use the **`StartOSDCloud`** parameter.  Unlike the Switch parameter of **`StartOSDCloudGUI`**, this is a String, meaning you need to provide your **`Start-OSDCloud`** switches for it to work properly

```
Edit-OSDCloud.winpe -StartOSDCloud '-OSBuild 1909 -OSEdition Pro -OSLanguage es-es -OSLicense Retail'
```

![](/files/-MgZV7IHBlCRNc8w_OZ_)

![](/files/-MgZVvLEsoXSWmedQTsK)

#### StartOSDPad

This parameter will allow you to use OSDPad to deploy using scripts on GitHub. I'd with I could say more now, but this is still being developed

![](/files/-MgZazXufHX_HlQ688dH)

![](/files/-MgZbVgggsavXOV34Toh)

#### StartScript

This parameter is simply a rename of WebPSScript, although its important to understand the position. This will add an entry to the Startnet.cmd after StartUpdate and before any StartOSDCloud or StartOSDCloudGUI lines.  This will allow you to completely any pre-flight, although since this is in a separate PowerShell session, Variables cannot be carried outside of the WebPSScript.  Be aware this doesn't work well with URL's with spaces (working on it)

#### Startnet

Finally, the **`Startnet`** parameter will add whatever you want to the **`Startnet.cmd`** file so if you want to tinker and play around, this is for you.

```
$Startnet = @'
start /wait PowerShell -NoL -C Install-Module OSD -Force -Verbose
start PowerShell -NoL -C Start-OSDCloudGUI
'@

Edit-OSDCloud.winpe -Startnet $Startnet
```

More information on these changes are included in the following link

{% content-ref url="/pages/-MWQ9Iok5nzMif3H27gi" %}
[Broken mention](broken://pages/-MWQ9Iok5nzMif3H27gi)
{% endcontent-ref %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/release.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
