> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-automate/osdcloudgui-defaults.md).

# OSDCloudGUI Defaults

Several of you have been asking me about setting the OSDCloudGUI defaults.  So let's get into it.  First of all you need to be running OSD PowerShell Module 23.5.24.1 or newer, so make sure you have that updated

## Start-OSDCloudGUI.json

In Windows, launch Start-OSDCloudGUI and focus on the first line.  This is the default OSDCloudGUI configuration

<figure><img src="/files/uesCNPZ3epTSDnPYQehL" alt=""><figcaption></figcaption></figure>

Copy this file to your OSDCloud Automate directory in your OSDCloud Workspace

<figure><img src="/files/5aOqiZIvVCprUydvHsPx" alt=""><figcaption></figcaption></figure>

## Edit Start-OSDCloudGUI.json

Start cleaning up this file and remove everything that does not need to be modified, especially the Computer information and the DriverPacks.  You should end up with something similar to what I have below

{% code lineNumbers="true" %}

```json
 {
    "BrandName":  "OSDCloud",
    "BrandColor":  "#0096D6",
    "OSActivation":  "Volume",
    "OSEdition":  "Enterprise",
    "OSLanguage":  "en-us",
    "OSImageIndex":  6,
    "OSName":  "Windows 11 22H2 x64",
    "OSReleaseID":  "22H2",
    "OSVersion":  "Windows 11",
    "OSActivationValues":  [
                               "Retail",
                               "Volume"
                           ],
    "OSEditionValues":  [
                            "Home",
                            "Home N",
                            "Home Single Language",
                            "Education",
                            "Education N",
                            "Enterprise",
                            "Enterprise N",
                            "Pro",
                            "Pro N"
                        ],
    "OSLanguageValues":  [
                             "ar-sa",
                             "bg-bg",
                             "cs-cz",
                             "da-dk",
                             "de-de",
                             "el-gr",
                             "en-gb",
                             "en-us",
                             "es-es",
                             "es-mx",
                             "et-ee",
                             "fi-fi",
                             "fr-ca",
                             "fr-fr",
                             "he-il",
                             "hr-hr",
                             "hu-hu",
                             "it-it",
                             "ja-jp",
                             "ko-kr",
                             "lt-lt",
                             "lv-lv",
                             "nb-no",
                             "nl-nl",
                             "pl-pl",
                             "pt-br",
                             "pt-pt",
                             "ro-ro",
                             "ru-ru",
                             "sk-sk",
                             "sl-si",
                             "sr-latn-rs",
                             "sv-se",
                             "th-th",
                             "tr-tr",
                             "uk-ua",
                             "zh-cn",
                             "zh-tw"
                         ],
    "OSNameValues":  [
                         "Windows 11 22H2 x64",
                         "Windows 11 21H2 x64",
                         "Windows 10 22H2 x64",
                         "Windows 10 21H2 x64",
                         "Windows 10 21H1 x64",
                         "Windows 10 20H2 x64",
                         "Windows 10 2004 x64",
                         "Windows 10 1909 x64",
                         "Windows 10 1903 x64",
                         "Windows 10 1809 x64"
                     ],
    "OSReleaseIDValues":  [
                              "22H2",
                              "21H2",
                              "21H1",
                              "20H2",
                              "2004",
                              "1909",
                              "1903",
                              "1809"
                          ],
    "OSVersionValues":  [
                            "Windows 11",
                            "Windows 10"
                        ],
    "captureScreenshots":  false,
    "ClearDiskConfirm":  true,
    "restartComputer":  true,
    "updateDiskDrivers":  true,
    "updateFirmware":  false,
    "updateNetworkDrivers":  true,
    "updateSCSIDrivers":  true
}
```

{% endcode %}

Collapsing a few items will help you see the design of this file.  There is Branding, Defaults, Values, and Menu Options

<figure><img src="/files/f6BBaNqwm6U0b4EWPeZ1" alt=""><figcaption></figcaption></figure>

## Branding

In my configuration, I'll change the default branding to the following.  If you have no plans on changing the branding, you can remove these entries

```
"BrandName":  "David Cloud",
"BrandColor":  "RED",
```

## Defaults

These can be difficult to configure since you have to get the OSImageIndex correct, but you can use the GUI to get that value.  In my case I changed the defaults from Enterprise Volume to Pro Retail, as well as changing the Language to en-gb

```
"OSActivation":  "Retail",
"OSEdition":  "Pro",
"OSLanguage":  "en-gb",
"OSImageIndex":  9,
"OSName":  "Windows 11 22H2 x64",
"OSReleaseID":  "22H2",
"OSVersion":  "Windows 11",
```

## Values

These are all the possible Values that appear in the combobox.  I'll make some minor adjustments and limit my deployment to 22H2 only, as well as cleaning up the Editions

```
"OSActivationValues":  [
                            "Retail",
                            "Volume"
                        ],
"OSEditionValues":  [
                        "Home",
                        "Education",
                        "Enterprise",
                        "Pro"
                    ],
"OSLanguageValues":  [
                            "en-gb",
                            "en-us"
                        ],
"OSNameValues":  [
                        "Windows 11 22H2 x64",
                        "Windows 10 22H2 x64"
                    ],
"OSReleaseIDValues":  [
                            "22H2"
                        ],
"OSVersionValues":  [
                        "Windows 11",
                        "Windows 10"
                    ],
```

## Menu Options

Finally some changes to the Menu Options, enabling Firmware updates and removing the Clear-Disk confirmation prompt (dangerous)

```
"ClearDiskConfirm":  false,
"restartComputer":  true,
"updateDiskDrivers":  true,
"updateFirmware":  true,
"updateNetworkDrivers":  true,
"updateSCSIDrivers":  true
```

## Complete JSON

Here's what my complete file looks like.  I'll give it a quick save

{% code lineNumbers="true" %}

```
{
    "BrandName":  "David Cloud",
    "BrandColor":  "RED",
    "OSActivation":  "Retail",
    "OSEdition":  "Pro",
    "OSLanguage":  "en-gb",
    "OSImageIndex":  9,
    "OSName":  "Windows 11 22H2 x64",
    "OSReleaseID":  "22H2",
    "OSVersion":  "Windows 11",
    "OSActivationValues":  [
                                "Retail",
                                "Volume"
                            ],
    "OSEditionValues":  [
                            "Home",
                            "Education",
                            "Enterprise",
                            "Pro"
                        ],
    "OSLanguageValues":  [
                                "en-gb",
                                "en-us"
                            ],
    "OSNameValues":  [
                            "Windows 11 22H2 x64",
                            "Windows 10 22H2 x64"
                        ],
    "OSReleaseIDValues":  [
                                "22H2"
                            ],
    "OSVersionValues":  [
                            "Windows 11",
                            "Windows 10"
                        ],
    "ClearDiskConfirm":  false,
    "restartComputer":  true,
    "updateDiskDrivers":  true,
    "updateFirmware":  true,
    "updateNetworkDrivers":  true,
    "updateSCSIDrivers":  true
}
```

{% endcode %}

## Rebuild ISO

Now I can rebuild my OSDCloud ISO so my saved file will be available when OSDCloud starts.  I'm also side-loading the OSD Module as I have unreleased changes that I haven't released to the PowerShell Gallery yet.  Finally I set OSDCloudGUI to start automatically when WinPE starts up

<figure><img src="/files/ylPCLlz2rQnYHxAD3k0E" alt=""><figcaption></figcaption></figure>

## Boot to WinPE and Test

When WinPE started up, OSDCloudGUI automatically launched.  A quick check at my minimized PowerShell window shows that it found the configuration file and imported it.  OSDCloudGUI shows the defaults that I selected and my custom David Cloud Branding

<figure><img src="/files/QIIYjVILSL1mEyGIONrL" alt=""><figcaption></figcaption></figure>

My Operating Systems are limited to Windows 10 and Windows 11 22H2, and the Windows 11 22H2 Business WIM that I had in my ISO:\OSDCloud\OS directory

<figure><img src="/files/xzoC1Pz3BGKsxiHYLm8j" alt=""><figcaption></figcaption></figure>

Windows Edition is set properly and several values were removed

<figure><img src="/files/NqYUuKunnvUSTwA9hnvN" alt=""><figcaption></figcaption></figure>

Languages are incredibly limited to just what I have configured

<figure><img src="/files/0T3dvjc6HSI0QkFr4m3c" alt=""><figcaption></figcaption></figure>

Finally my Deployment Options are set

<figure><img src="/files/rSQXk2Ay75Da3sX2GgWO" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/kZuV8my42DmLQo9RvMKw" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-automate/osdcloudgui-defaults.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
