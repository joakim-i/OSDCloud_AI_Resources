> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/cumulative-updates.md).

# Cumulative Updates

I've added the ability to apply a Cumulative Update to an OSDCloud Template due to the Secure Boot vulnerability.  The next two links give some details on the issue

{% embed url="<https://support.microsoft.com/en-us/topic/kb5025885-how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023-24932-41a975df-beb2-40c1-99a3-b3ff139f832d>" %}

{% embed url="<https://learn.microsoft.com/en-us/windows/deployment/update/media-dynamic-update#update-winpe>" %}

## Download the Cumulative Update

Start by downloading the update from Microsoft Update Catalog and specifying the path to the downloaded update.  Start by downloading the x64 version at this link if you are using the ADK for Windows 11 version 22H2

{% embed url="<https://www.catalog.update.microsoft.com/Search.aspx?q=KB5026372>" %}

<figure><img src="/files/sk0tCNLL9nkKOC9NrN6r" alt=""><figcaption></figcaption></figure>

## Apply the Cumulative Update

Once you have the update downloaded, use the `CumulativeUpdate` parameter and supply the Path to the downloaded MSU.  In the example below I applied this in my default OSDCloud Template as this will be the one I use the most

1. Cumulative Update is applied
2. Updated Windows Information is displayed
3. Boot files are updated
4. DISM Component Cleanup is run

<figure><img src="/files/on0I7amGFXn9qQuNVNOf" alt=""><figcaption></figcaption></figure>

## Apply the WRONG Cumulative Update

It's absolutely possible to apply the wrong Cumulative Update for WinPE, so make sure you understand that the Cumulative Update that you download must match your ADK.  So if you are using the ADK for Windows 11 version 22H2, you need the Windows 11 22H2 x64 Cumulative Update

1. Cumulative Update is applied
2. Updated Windows Information is displayed.  In this case, the UBR did not change
3. Warning is displayed that the UBR has not been changed.  The Boot files will not be updated
4. DISM Component Cleanup is run

<figure><img src="/files/8qYfSzJPB3mDytRNVU7A" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
I'm not properly staffed to answer individual questions about which Cumulative Update you need for the ADK you have installed.  If this is not something you can resolve on your own, then you should probably wait for updated Media from Microsoft that already has the Secure Boot updates applied
{% endhint %}

## The Code

If you are interested in reviewing how this works, here is a snipped from the `New-OSDCloudTemplate` function

{% embed url="<https://github.com/OSDeploy/OSD/blob/a8547e4868a9ff99fe7880fea52158ee5ff7642f/Public/OSDCloudSetup/OSDCloudTemplate.ps1#L815>" %}

<figure><img src="/files/KEkLq7wqxxnegi0gtkRb" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/cumulative-updates.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
