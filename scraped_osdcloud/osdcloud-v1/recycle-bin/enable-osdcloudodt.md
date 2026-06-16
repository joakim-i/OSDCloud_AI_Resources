> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/enable-osdcloudodt.md).

# Enable-OSDCloudODT

{% hint style="danger" %}
This functionality will be removed in the next few weeks.  Let me know if you are using this so I can detail a workaround
{% endhint %}

{% hint style="danger" %}
I would consider this Experimental and I am unsure of the future of this function.  It will more than likely change, so consider this a Sandbox for now
{% endhint %}

This is a new function to add Office M365 and install it in the Specialize phase of Windows Setup.  I had high hopes for this process, but in my testing, there was less than 1 minute difference in installing Office in Specialize versus pulling from an Intune (Office CDN).  I'm sure one of you will look into this further, so this is for now an OSDCloud Opt-In

## Do It

This process should be done before **`Edit-OSDCloud.winpe`**, although it really doesn't matter, but remember after adding this, you need to update your WinPE to see the magic

```
Enable-OSDCloudODT -Verbose
```

![](/files/-MXmOCtPiP9nVWOsFy-p)

There is really nothing to it.  As you can see in the Verbose output, it will download the latest Microsoft ODT and expand it into subdirectories

## The Directory Structure

This is probably the most important process to understand, and the step that will probably be messed up the most on your end if you really don't understand.  For you visual people, hopefully this will help you understand, but the key is that the ODT directory sits in the ROOT of your OSDCloud Workspace

![](/files/-MXmPknUbE3kINykQapS)

### Product

In the ODT directory are two subdirectories that represent the M365 / Office Product.  You can see all the Products that can be used, but its important that your directory represent the Product for better organization.  If you have no plans to work with ProPlus2019Volume, delete it

{% embed url="<https://docs.microsoft.com/en-us/office365/troubleshoot/installation/product-ids-supported-office-deployment-click-to-run>" %}

### Channel

The next subdirectory represents the M365 / Office Channel

{% hint style="success" %}
Delete the Channel directories that you don't need!
{% endhint %}

{% embed url="<https://docs.microsoft.com/en-us/deployoffice/update-channels-changes>" %}

&#x20; It really doesn't matter what you name them, as long as the Channels are separated.  In each Channel directory there should be a copy of setup.exe which was expanded when you ran **`Enable-OSDCloudODT`**.  You can always repeat that function to add  the latest ODT setup.exe as needed, understanding that the XML files will be overwritten

![](/files/-MXmQtI9u5SaFxZoeRWh)

### XML Files

In each of the Channel directories, in addition to the setup.exe, is an Office Configuration File.  Don't edit these as they can be overwritten.  Create your own using this as an example.  The biggest thing is for the Language ID to be set to "MatchOS", but whatever

```
<Configuration ID="002634c3-bedd-416a-82ea-764d564ec07a">
  <Add OfficeClientEdition="64" Channel="MonthlyEnterprise">
    <Product ID="O365ProPlusRetail">
      <Language ID="MatchOS" />
      <ExcludeApp ID="Groove" />
    </Product>
  </Add>
  <Property Name="SharedComputerLicensing" Value="0" />
  <Property Name="SCLCacheOverride" Value="0" />
  <Property Name="AUTOACTIVATE" Value="0" />
  <Property Name="FORCEAPPSHUTDOWN" Value="FALSE" />
  <Property Name="DeviceBasedLicensing" Value="0" />
  <Updates Enabled="TRUE" />
  <RemoveMSI />
  <Display Level="Full" AcceptEULA="TRUE" />
</Configuration>
```

## USB Considerations

{% hint style="warning" %}
This isn't entirely working as planned due to the inclusion of the XML files in WinPE.  This should be considered as Concept Under Development for the time being
{% endhint %}

If you are deploying OSDCloud from a USB, you can download the content in advance.  Assuming you have copied the ODT directory to \<USBDrive>:\OSDCloud\ODT then do the following

Type cmd in the Windows Explorer Address Bar and press Enter

![](/files/-MXmSYZ2A69-pDsY-SRb)

Now use setup.exe to /download the content specified by the Office Configuration XML.  This will download your Office payload from the CDN

![](/files/-MXmT4Lts4X0P5p4cwAf)

## Edit-OSDCloud.usb

When you run this command, the necessary files will be added to WinPE

![](/files/-MXmh7Gp4l5rrUpbdbo0)

## Walkthrough

How it works has been added to the Walkthrough

{% content-ref url="/pages/-MVzRYKrha\_LohfIatwq" %}
[Deploy](/osdcloud-v1/recycle-bin/deploy.md)
{% endcontent-ref %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/enable-osdcloudodt.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
