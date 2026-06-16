> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/office365-specialize.md).

# Office365 Specialize

**The concept is simple.  Can Office 365 / 2019 be installed prior to OOBE/AutoPilot?**

Jeff was kind enough to send me his Office Configuration file for this test, so kudos for stepping up. &#x20;

{% content-ref url="/pages/-MX0kJdaY3EKEdA8GodG" %}
[Broken mention](broken://pages/-MX0kJdaY3EKEdA8GodG)
{% endcontent-ref %}

Keep in mind this is ROUGH and not automated at all.  I'm just testing the concept to make sure it works.  If so, then I'll look at automation

## Configuration File

Here's a sanitized copy of Jeff's Office Configuration file

```
<Configuration ID="INSERT GUID HERE">
  <Add OfficeClientEdition="64" Channel="SemiAnnual" MigrateArch="TRUE">
    <Product ID="O365ProPlusRetail">
      <Language ID="en-us" />
      <ExcludeApp ID="Groove" />
      <ExcludeApp ID="Lync" />
      <ExcludeApp ID="OneDrive" />
      <ExcludeApp ID="Bing" />
    </Product>
    <Product ID="VisioPro2019Volume" PIDKEY="INSERT PID HERE">
      <Language ID="en-us" />
      <ExcludeApp ID="Groove" />
      <ExcludeApp ID="Lync" />
      <ExcludeApp ID="OneDrive" />
      <ExcludeApp ID="Bing" />
    </Product>
    <Product ID="ProjectPro2019Volume" PIDKEY="INSERT PID HERE">
      <Language ID="en-us" />
      <ExcludeApp ID="Groove" />
      <ExcludeApp ID="Lync" />
      <ExcludeApp ID="OneDrive" />
      <ExcludeApp ID="Bing" />
    </Product>
  </Add>
  <Property Name="SharedComputerLicensing" Value="0" />
  <Property Name="SCLCacheOverride" Value="0" />
  <Property Name="AUTOACTIVATE" Value="0" />
  <Property Name="FORCEAPPSHUTDOWN" Value="FALSE" />
  <Property Name="DeviceBasedLicensing" Value="0" />
  <Updates Enabled="TRUE" />
  <RemoveMSI />
  <AppSettings>
    <Setup Name="Company" Value="INSERT COMPANY HERE" />
  </AppSettings>
  <Display Level="Full" AcceptEULA="TRUE" />
</Configuration>
```

## Download

For this first test, I'll download the content before the install to speed things along.  In his case, he is installing from MDT, so this will probably be the method he uses.  This is the command I will use to download the content

```
setup.exe /download Office2019Conf.xml
```

## WinPE Phase

### OSDCloud Install

I'll start out by running through an OSDCloud, it doesn't matter what OS or anything.  I just need to remember not to reboot yet!  In the screenshot below, this is my entry point for installing Office (which shouldn't have run for a VM, but I'm glad it's here)

![](/files/-MXcEaA6SASW8WfP-aig)

### Copy Content

There's no universally agreed upon path for saving the Office content, so I'll just dump it at C:\MSOffice.  Here's what that looks like in that directory with setup.exe, Office Configuration XML, and the Office Data

![](/files/-MXcE284r-Cjmd9dShmL)

### Edit&#x20;

I'll need to edit the Expand-StagedDriverPack.xml for this test ... in this example I've removed the Driver bit (since I'm on a VM, that doesn't matter)

```
C:\Windows\Panther\Expand-StagedDriverPack.xml
```

![](/files/-MXcEOdrAS5_UN6_u_Jp)

Here is how the XML looks.  The first order of business is to disable the Office Telemetry since this will prevent the Office installation from finishing.  This can be added back in the Unattend xml, or in the OS, or I can leave it disabled.  PowerShell\_ISE is not necessary, but it gives me a WAIT so I can check some things out before rebooting to OOBE

```
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="specialize">
        <component name="Microsoft-Windows-Deployment" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <RunSynchronous>
                <RunSynchronousCommand wcm:action="add">
                    <Order>1</Order>
                    <Description>Disable Telemetry</Description>
                    <Path>reg add HKCU\Software\Policies\Microsoft\Office\Common\ClientTelemetry /v DisableTelemetry /t REG_DWORD /d 1 /f</Path>
                </RunSynchronousCommand>
                <RunSynchronousCommand wcm:action="add">
                    <Order>2</Order>
                    <Description>Install Office365</Description>
                    <Path>C:\MSOffice\setup.exe /configure C:\MSOffice\Office2019Conf.xml</Path>
                </RunSynchronousCommand>
                <RunSynchronousCommand wcm:action="add">
                    <Order>3</Order>
                    <Description>PowerShell ISE</Description>
                    <Path>PowerShell_ISE.exe</Path>
                </RunSynchronousCommand>
            </RunSynchronous>
        </component>
    </settings>
</unattend>
```

### Snapshot and Reboot

Time to take a snapshot and reboot to Specialize and see if this works

## Specialize

I'd take screenshots of how it worked, but I think the video works best so you can see the process taking only a few minutes

{% embed url="<https://youtu.be/P9uhd6MPLcw>" %}

## OOBE

Another video.  Nothing much to see here, I just did a Domain setup (this was not an AutoPilot test)

{% embed url="<https://youtu.be/xmM_LDPJFOI>" %}

## Further Steps

![](/files/-MXbwfk8isC5oOFV-mD5)

* AutoPilot - this should work fine, but it will have to be tested
* Download Content - this test was done with the Office data in place, so a test downloading the content will need to be performed.  I had done this previously with another configuration, so I'm sure this will work
* Network Drivers - obviously this will run after the Driver injection, but I will need to perform some tests if the Network Adapter isn't installed


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/office365-specialize.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
