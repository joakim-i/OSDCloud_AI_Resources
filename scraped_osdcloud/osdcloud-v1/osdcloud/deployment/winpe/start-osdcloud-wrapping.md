> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/deployment/winpe/start-osdcloud-wrapping.md).

# Start-OSDCloud Wrapping

There are many variables in OSDCloud to control the process, similar to running OSDCloud with parameters to control a small set of the variables, you can script around Start-OSDCloud to configure so much more to get the exact zero touch scenario you're looking for.

Start-OSDCloud has about 60 variables in the Start-OSDCloud script beginning that are set, but along the way, several others can be used as well, which can be consumed by the OSDCloud engine which at last check, has about 130 variables. &#x20;

At the start of the OSDCloud engine, it has a default set for these variables, then it looks at what you sent along the way with Start-OSDCloud, and it overwrites the defaults with the variables you set, but if you manually set any variables ahead of time using the global variable "MyOSDCloud", it will overwrite any previous variables with what you've set in that variable, I hope you're all tracking. Let's look at an example.

NOTE: See Start-OSDCloudGUI -> Global Variable for additional details

By Default, there is a $Global:OSDCloud variable with several sub keys, once of which is "OSVersion", which is set to "Windows 10" by default.  If I run Start-OSDCloud with some parameters, I can see that a new Global variable $Global:StartOSDCloud is created with the information I just fed into it:

<figure><img src="/files/zHEhNSSu6Si1FFuvwNzJ" alt=""><figcaption><p>OSDCloud Default Variables, OSVersion set to 'Windows 10'</p></figcaption></figure>

<figure><img src="/files/qr3Noiw4fpBW27tE8iJb" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/xOL26r00Hi8rQYfnzEQC" alt=""><figcaption></figcaption></figure>

So now when OSDCloud runs, it will overwrite the defaults in $Global:OSDCloud with the ones in $Global:StartOSDCloud, updating $Global:OSDCloud.OSVersion from "Windows 10" to "Windows 11"

<figure><img src="/files/Hgzd5lB0vCBTX2nApabt" alt=""><figcaption></figcaption></figure>

So, from this small example, you can see how OSDCloud overwrites the defaults with the variables you're setting along the way using parameters, but that's just one way to set them.  The GUI? It's really just a front end that allows you to set several variables using a GUI interface.  Each drop down and check box maps directly to a variable.

Now we're finally getting to the good part, this is how I have automated several unique experiences based on a simple PowerShell wrapper file that gets called.  Lets look at some code examples.  For instance, I have a Windows 11 wrapper script that sets several items and calls OSDCloud

```
#Variables to define the Windows OS / Edition etc to be applied during OSDCloud
$OSName = 'Windows 11 23H2 x64'
$OSEdition = 'Pro'
$OSActivation = 'Retail'
$OSLanguage = 'en-us'

#Set OSDCloud Vars
$Global:MyOSDCloud = [ordered]@{
    Restart = [bool]$False
    RecoveryPartition = [bool]$true
    OEMActivation = [bool]$True
    WindowsUpdate = [bool]$true
    WindowsUpdateDrivers = [bool]$true
    WindowsDefenderUpdate = [bool]$true
    SetTimeZone = [bool]$true
    ClearDiskConfirm = [bool]$False
    ShutdownSetupComplete = [bool]$false
    SyncMSUpCatDriverUSB = [bool]$true
    CheckSHA1 = [bool]$true
}

#Launch OSDCloud
Write-Host "Starting OSDCloud" -ForegroundColor Green
write-host "Start-OSDCloud -OSName $OSName -OSEdition $OSEdition -OSActivation $OSActivation -OSLanguage $OSLanguage"

Start-OSDCloud -OSName $OSName -OSEdition $OSEdition -OSActivation $OSActivation -OSLanguage $OSLanguage
```

When I trigger that script, it launches OSDCloud with the OS I want deployed, and presets several variables that are in the Global:MyOSDCloud variable.&#x20;

<figure><img src="/files/8x08I1o1HAruaRCZOiZa" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/YrQ5im1loE7jaHz70gcp" alt=""><figcaption></figcaption></figure>

You can see the variables in my script have been merged into the $global:OSDCloud variable

<figure><img src="/files/bCLukzjIktkohEvc5o2n" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/LlBt1milcKa5zzglqc5X" alt=""><figcaption></figcaption></figure>

I keep a few variations of my wrapper scripts in GitHub, which I then call and based on hardware models, will also set additional variables, like for HP, I have it update TPM, BIOS, and run HPIA to update Drivers during Setup Complete.  <br>

As all of the available variables do change, I'm not going to list them here, but feel free to look at things in the code in the module to see a full list.  If you'd ever like to see my of my examples, please reach out via Discord (WinAdmins) or X - @gwblok


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/deployment/winpe/start-osdcloud-wrapping.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
