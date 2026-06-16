> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/mdt-osdcloud-driverpacks.md).

# MDT OSDCloud DriverPacks

This is a concept that is taken from the way OSDCloud downloads DriverPacks during the deployment in WinPE, rather than a traditional MDT Total Control or Modern Driver Management.  Implementing this requires no infrastructure other than open Internet access.  By implementing this concept, your MDT infrastructure will fully support 724 different Computer Models from Dell, HP , and Lenovo

![](/files/-MWw_oVKgNwJ8uOahRog)

## TODO

This process is currently in Development with the following items needing to be resolved

#### Logging

This function writes to a Transcript in C:\Drivers and will need to be expanded to logging in the BDD.log.  Reach out to me if you want to work on this

#### Proxy

Support for a Proxy has not been implemented yet, but is planned.  Reach out to me if you would like to contribute

#### Configuration Manager

This has not been tested in Configuration Manager at this time

## WinPE Requirements

PowerShell support is required for this to work, so at a minimum, you need to make sure that PowerShell is fully functional in WinPE

### Curl.exe

This is absolutely required for downloading the DriverPack.  If it is not in your WinPE, it will be sourced from your Offline OS.  If it is not in the OfflineOS, then it will exit out

{% hint style="danger" %}
In simple terms, if you are deploying an old OS that does not have $SystemRoot\System32\Curl.exe and you did not inject Curl.exe into WinPE at $MountDirectory\SystemRoot\System32\Curl.exe then you will not be able to download a DriverPack
{% endhint %}

### OSD PowerShell Module

The OSD Module will need to be added to your MDT Boot Image.  This is best handled by making sure your computer has the latest OSD Module and running the following commands

```
Import-Module OSD -Force

#The DeploymentShare needs to be local and writable as you are mounting a WIM
$DeploymentShare = "D:\DeploymentShare"

Copy-PSModuleToWim -Name OSD -ImagePath "$DeploymentShare\Boot\LiteTouchPE_x64.wim"
```

## Microsoft Deployment Toolkit

### Boot Images

After making sure you have added the OSD PowerShell Module to your LiteTouchPE\_x64.wim you will need to Update your Deployment Share

![](/files/-MWzSw2x3jO9GVCChy5o)

Make sure you do not completely regenerate your boot images

![](/files/-MWzT20v__f_x5J6qALd)

You are good to go as long it uses the OSD enabled LiteTouchPE\_x64.wim.  If it pulls a new wim from the ADK, then let that complete, and add the OSD PowerShell Module to the LiteTouchPE\_x64.wim and repeat this process.

![](/files/-MWzTC-SV7Kvls2z4ylg)

### Unattend.xml Template

{% hint style="warning" %}
This step is not completely necessary if you plan on just editing an individual Task Sequence Unattend.xml
{% endhint %}

Edit the following file and add the XML snippet.  This is what expands the DriverPack in the Specialize Phase

```
"C:\Program Files\Microsoft Deployment Toolkit\Templates\Unattend_x64.xml.10.0"
```

```
<RunSynchronousCommand wcm:action="add">
    <Order>5</Order>
    <Description>Expand-ZTIDriverPack</Description>
    <Path>Powershell -ExecutionPolicy Bypass -Command Expand-ZTIDriverPack</Path>
</RunSynchronousCommand>
```

![](/files/-MWyrubK2xapUl7mSCwu)

### Task Sequence

You will need to add a Run Command Line step in your Postinstall group with the following configuration. **I strongly recommend to Continue on error**

**Command line:**

```
cmd.exe /c start /wait PowerShell.exe -ExecutionPolicy Bypass -Command Save-ZTIDriverPack
```

**Start in:**

```
%OSDisk%\Windows\System32
```

![](/files/-MWz3cpjvIQtwxD2PI1a)

![](/files/-MWz3ipPwyB7Ch_VyWm-)

### Task Sequence Unattend.xml

Similar to the process detailed in the Unattend.xml Template section earlier, if you have an existing Task Sequence, you will need to edit the Unattend.xml file located in the following path

```
$DeploymentShare\Control\$TaskSequenceId\Unattend.xml
```

![](/files/-MWwS65LVu9CyHHkE6yA)

Add this snipped to your specialize settings pass.  Make sure that the Order Number is unique and next in line to the previous RunSynchronousCommand

```
<RunSynchronousCommand wcm:action="add">
    <Order>5</Order>
    <Description>Expand-ZTIDriverPack</Description>
    <Path>Powershell -ExecutionPolicy Bypass -Command Expand-ZTIDriverPack</Path>
</RunSynchronousCommand>
```

![](/files/-MWz2gb7pHuiY583SIE-)

## Deployment

![](/files/-MWwUHtRZkLe52acdda1)

![](/files/-MWz6cQpZZLbHmZXiWAz)

![](/files/-MWz6oXA731CDRlZD8A-)

### Save-ZTIDriverPack

This is the function that gets the OSDCloud Driver Pack and stages it in $OSDisk\Drivers.  It handles both a Copy if it exists in the DeploymentShare, or a Download if it does not.  The following is a brief summary of the actions

1. Connects to the MDT Task Sequence Environment (TSEnv)
2. Copies the OSD PowerShell Module from WinPE to the Offline OS
3. Identifies the required DriverPack using Get-MyDriverPack
4. Determines if the DriverPack is in $DeployRoot\DriverPacks
   1. True: Copy the DriverPack to $OSDisk\Drivers
   2. False
      1. Checks for curl.exe in WinPE
         1. False: Copy from $OSDisk\Windows\System32
      2. Downloads the DriverPack to $OSDisk\Drivers

![](/files/-MWz7qZW9YvsUGuMNIyD)

### Expand-ZTIDriverPack

During the Specialize phase, this function will scan all files in the root of C:\Drivers and expand them (if it can).  If it expands the DriverPack, it will also apply them to the Offline OS

![](/files/-MWz83v4SLTeDJIxYaTJ)

![](/files/-MWwSgLWiZ3Yv2Mt8Ua_)

{% embed url="<https://youtu.be/MfWA1tJpMM4>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/mdt-osdcloud-driverpacks.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
