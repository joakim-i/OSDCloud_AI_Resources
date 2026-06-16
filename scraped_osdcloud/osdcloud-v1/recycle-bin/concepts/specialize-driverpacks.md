> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/specialize-driverpacks.md).

# Specialize DriverPacks

{% hint style="warning" %}
Wait for the next update to the OSD Module before trying this out as these functions have not been released yet
{% endhint %}

OSDCloud applies HP and Lenovo DriverPacks in the Specialize Phase of Windows Setup.  The reason this is done is because HP and Lenovo Driver Packs are in 32-Bit EXE format, so they cannot be executed and expanded in WinPE x64.  This page will detail how OSDCloud handles this

## Save-MyDriverPack (WinPE)

When OSDCloud encounters an EXE Driver Pack (HP and Lenovo) a warning is displayed in WinPE that it is unable to be expanded.  **`Deploy-OSDCloud.ps1`** addresses this by executing the function **`Add-StagedDriverPack.specialize`**

![](/files/-MWrhcIjJGysXx47BvZu)

![](/files/-MWricw4H06k1JcmAWwj)

## Add-StagedDriverPack.specialize

This function will create an Unattend file in the following location

```
C:\Windows\Panther\Expand-StagedDriverPack.xml
```

The contents of the Unattend are to simply execute the function Expand-StagedDriverPack

```
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="specialize">
        <component name="Microsoft-Windows-Deployment" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <RunSynchronous>
                <RunSynchronousCommand wcm:action="add">
                    <Order>1</Order>
                    <Description>Expand-StagedDriverPack</Description>
                    <Path>Powershell -ExecutionPolicy Bypass -Command Expand-StagedDriverPack</Path>
                </RunSynchronousCommand>
            </RunSynchronous>
        </component>
    </settings>
</unattend>
```

To ensure that this Unattend file is run, the following Registry entry is made in the Offline OS

```
PS C:\> (Get-ItemProperty -Path HKLM:\SYSTEM\Setup).UnattendFile
C:\Windows\Panther\Expand-StagedDriverPack.xml
```

## Answer File Search Order

By doing this method, it ensures that if you have an Unattend.xml file placed in C:\Windows\Panther, it will not interfere with the Specialize pass, nor will an existing Unattend.xml file be overwritten.  Additionally, the Registry method is the first Answer File that is processed if it exists

![](/files/-MWrJytv6K-bZkYwCvOJ)

For more details about the Answer File settings, see the following link

{% embed url="<https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-automation-overview#implicit-answer-file-search-order>" %}

## Expand-StagedDriverPack

Once the Specialize phase has started, the Answer File will expand any DriverPacks and apply the drivers using pnpunattend.exe.  A quick look at the code will do a better job of explaining how this needs to work

![](/files/-MWrkm54mDk6au4tu56z)

And here is a video of how the process looks

{% embed url="<https://youtu.be/Fbb_hoYQph4>" %}

## Next Steps

If you think this applies only to OSDCloud, you are missing the big picture.  This process opens the way to replacing Out-of-box-Drivers in MDT with DriverPacks.  More details on this to come shortly


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/specialize-driverpacks.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
