> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/deployment/winpe/start-osdcloudgui.md).

# Start-OSDCloudGUI

{% embed url="<https://github.com/OSDeploy/OSD/blob/master/Docs/Start-OSDCloudGUI.md>" %}

After WinPE startup is complete, enter **`Start-OSDCloudGUI`** at the PowerShell prompt

<figure><img src="/files/EHo2h1HHI6GXBAp2P2rf" alt=""><figcaption></figcaption></figure>

You will briefly see the OSDCloudGUI Configuration and the TPM/Autopilot status before this PowerShell window is minimized

<figure><img src="/files/rxXgRnd7SgYdYz8XSJqW" alt=""><figcaption></figcaption></figure>

## Operating System

You can select an Operating System from the combobox.  The default Operating System will always be the latest, which is currently Windows 11 22H2 x64

<figure><img src="/files/qMLXyqfplZbAPhb03SVR" alt=""><figcaption></figcaption></figure>

Currently, there are 760 Operating System combinations (OS, Language, Activation) that are available which you can review using the **`Get-OSDCloudOperatingSystems`** function

<figure><img src="/files/MiD0ft03gnSK8Lgk9I8Q" alt=""><figcaption></figcaption></figure>

## Edition

The Windows Edition is set to **Enterprise** by default

<figure><img src="/files/koDTYnCRvNyjB1aCgdL8" alt=""><figcaption></figcaption></figure>

## Language

The Windows Language is set to **en-us** by default

<figure><img src="/files/9wWsbxR0x3lKuwQTJI90" alt=""><figcaption></figcaption></figure>

## Activation (License)

The Windows Activation is set to Volume by default due to the default Windows Edition being set to Enterprise

<figure><img src="/files/isdKcIksZUlN5t51wb0p" alt=""><figcaption></figcaption></figure>

## DriverPack

Depending on the Computer Model and Operating System, a Driver Pack will automatically be selected for you.  In the case of a Virtual Machine or an unknown Computer Model, Microsoft Update Catalog will be selected.  You can also select None for a DriverPack if you would prefer to go a different route

<figure><img src="/files/vKHjECeV8tMFF7D9Rifi" alt=""><figcaption></figcaption></figure>

## Deployment Options

By default, you will need to confirm the Clear-Disk operation during a deployment.  You can unselect this requirement from the Deployment Options menu.  After the deployment is complete, the computer will automatically restart.  This can be disabled from this menu

{% hint style="warning" %}
capture Screenshots isn't working at this time
{% endhint %}

<figure><img src="/files/N5irt9Vv6AuuzvnfaEhw" alt=""><figcaption></figcaption></figure>

## Microsoft Update Catalog

Disk, Network, and SCSI Adapter drivers will be downloaded from Microsoft Update Catalog by default.  Optionally, you can download Firmware updates for your device

<figure><img src="/files/NCXd2xy30RLX3MtK4E8w" alt=""><figcaption></figcaption></figure>

## Start

When you are ready to deploy, press the Start button.  You should get prompted to confirm the Clear-Disk step

<figure><img src="/files/F5sK19MhuORc1nhjb7wi" alt=""><figcaption><p>Clear-Disk Confirm</p></figcaption></figure>

The Operating System ESD will be downloaded from Microsoft

<figure><img src="/files/0Zsl9vA2tU5up0boEff5" alt=""><figcaption></figcaption></figure>

Once the ESD has been downloaded, it is expanded to C:\\

<figure><img src="/files/t9hvcQIv087onGJYTnCW" alt=""><figcaption></figcaption></figure>

The DriverPack will be expanded in WinPE, or staged for first boot.  PowerShell Modules that are required for Autopilot will be updated in the offline Operating System

<figure><img src="/files/gBcBSiXTjwz22315WLG3" alt=""><figcaption></figcaption></figure>

Finally, the computer should reboot to OOBE.  At this point, OSDCloud is complete

<figure><img src="/files/t2t54pcXTChVWJs4t4v0" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/deployment/winpe/start-osdcloudgui.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
