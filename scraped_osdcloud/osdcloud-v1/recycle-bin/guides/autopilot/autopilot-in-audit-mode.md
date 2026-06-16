> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/guides/autopilot/autopilot-in-audit-mode.md).

# AutoPilot in Audit Mode

If the AutopilotConfigurationFile.json isn't going to work for you, another method to consider is Manual Registration in Audit Mode

## Use-WindowsUnattend.audit.autopilot

I've taken the time to write a function which will drop an Unattend.xml to kick off Audit Mode.  Here is what is in the XML

```
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="oobeSystem">
        <component name="Microsoft-Windows-Deployment" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <Reseal>
                <Mode>Audit</Mode>
            </Reseal>
        </component>
    </settings>
    <settings pass="auditUser">
        <component name="Microsoft-Windows-Deployment" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <RunSynchronous>
                <RunSynchronousCommand wcm:action="add">
                <Order>1</Order>
                <Description>Set ExecutionPolicy Bypass</Description>
                <Path>PowerShell -WindowStyle Hidden -Command "Set-ExecutionPolicy Bypass -Force"</Path>
                </RunSynchronousCommand>

                <RunSynchronousCommand wcm:action="add">
                <Order>2</Order>
                <Description>WaitWebConnection</Description>
                <Path>PowerShell -Command "Wait-WebConnection powershellgallery.com -Verbose"</Path>
                </RunSynchronousCommand>

                <RunSynchronousCommand wcm:action="add">
                <Order>3</Order>
                <Description>Save Get-WindowsAutoPilotInfo</Description>
                <Path>PowerShell -Command "Install-Script -Name Get-WindowsAutoPilotInfo -Verbose -Force"</Path>
                </RunSynchronousCommand>
            </RunSynchronous>
        </component>
    </settings>
</unattend>
```

You will need to run this function from WinPE after the OS has been dropped.  I'll look into adding a Start-OSDCloud parameter to do this automatically if necessary

As you can see the function will drop the Unattend.xml and Use-WindowsUnattend to inject it into the Offline OS.  Since the OSD PowerShell Module is also needed, it will copy the version that is in WinPE directly into the Offline OS.  Simply reboot after this is complete

![](/files/-MWQXQVCHueKzM84YIw6)

## Enter Audit Mode

This process on a good machine can take 5-10 minutes to generate the Administrator profile, so just be patient.

![](/files/-MWHxl_GbbnO3LAP-9Np)

Once logged in, the OSD Module will take over and **`Set-ExecutionPolicy RemoteSigned`** for you (remember to set this back), and then wait for an Internet connection to PowerShell Gallery using the new **`Wait-WebConnection`** OSD function

![](/files/-MWHxzcP1noH_XVni3P9)

Once PowerShell Gallery is available, the **`Get-WindowsAutoPilotInfo`** Script will be installed

![](/files/-MWHy3Gm5KEMtKzUe-BK)

Finally, dropping you to the Desktop.  From here, simply open PowerShell and run **`Get-WindowsAutoPilotInfo -Online`** with whatever parameters you need.  When you are all done, just press OK in the Sysprep Window to reboot to OOBE.  Enjoy!

![](/files/-MWHyCTO0t2_16OwgTI-)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/guides/autopilot/autopilot-in-audit-mode.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
