> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-vm/new-osdcloudvm.md).

# New-OSDCloudVM

You can customize the defaults of the Virtual Machine by using the parameters of this function.  When you change any of the parameters, it will save the configuration in the OSDCloud Workspace.  Every subsequent OSDCloud VM that you create in the same OSDCloud Workspace will use these settings.  In this example I have set my OSDCloud VM Settings (Template) with the following configuration

<figure><img src="/files/FVZh83grOX0fRlrdmXDr" alt=""><figcaption></figcaption></figure>

## First Run

When I run **`New-OSDCloudVM`**, it will inherit my OSDCloud VM Settings that were created in my OSDCloud Template by **`Set-OSDCloudVMSettings`**

<figure><img src="/files/iMT0DeDnYwa1moHKvMxc" alt=""><figcaption></figcaption></figure>

## SwitchName

This should absolutely be one of the first things you set in your Virtual Machine.  Ideally it should be inherited from Set-OSDCloudVMSettings

And yes, you will be able to Tab Complete through your available Virtual Switches

<figure><img src="/files/xDWNX6JcrumqV4hsRKA5" alt=""><figcaption></figcaption></figure>

If you need your VM set to 'Not connected', just use a **`$null`** value

<figure><img src="/files/yBT3mjHPccME2uZOWeDM" alt=""><figcaption></figcaption></figure>

## StartVM

By default, OSDCloud VM will startup automatically.  I can prevent this from happening by using this parameter and setting the value to **`$false`**

<figure><img src="/files/YrzS7JRAR7CcOkJZrAPN" alt=""><figcaption></figcaption></figure>

## CheckpointVM

This value determines if a New VM Checkpoint will be created or not, which is incredibly helpful if you need to reset the VM to a clean state.  You can change this at the command line as well

<figure><img src="/files/wATeJoUk0eninofn3kjp" alt=""><figcaption></figcaption></figure>

## NamePrefix

This Prefix is given to the Virtual Machine name created with **`New-OSDCloudVM`**.  By default, this is **OSDCloud**, but you can also configure this at the command line

<figure><img src="/files/RcQ0o9hW8oWIQ0GElQLG" alt=""><figcaption></figcaption></figure>

## Generation

By default, the VM will be created as Generation 2, which is UEFI.  But if you want to live in a world of pain, you can create a Generation 1 Virtual Machine.

{% hint style="danger" %}
**Seriously don't do this.  OSDCloud will partition your disk as GPT, which won't boot your Generation 1 VM.  This feature was added for testing only.  I will not address any questions about this parameter, so you're on your own here.**
{% endhint %}

<figure><img src="/files/y8UsDYau2Pfv3jRRltp8" alt=""><figcaption></figcaption></figure>

## MemoryStartupGB

The minimum requirements for Windows 11 are 4GB, but I've seen some things not work right, so I suggest bumping this up a little

<figure><img src="/files/p5WrJokqRiuCBvirXhG0" alt=""><figcaption></figcaption></figure>

## ProcessorCount

I recommend setting this to at least 2, but that's your call.

<figure><img src="/files/fsSwZ5m22R6EM10D6AFh" alt=""><figcaption></figcaption></figure>

If you are curious as to how many processors you can use at the same time across all Virtual Machines ...

<figure><img src="/files/z4MZLUU1bIXF1KsDjZI6" alt=""><figcaption></figcaption></figure>

Can you create a Virtual Machine with a Processor Count greater than the number of Processors?  Yes you can, but you'll have problems getting it to start

<figure><img src="/files/JtynTjssVWK0STtpn7ye" alt=""><figcaption></figcaption></figure>

## VHDSizeGB

Finally feel free to give your Virtual Machine a few extra GB's of space.  Enjoy!

<figure><img src="/files/cz1Sj5su5vMA9XNo4CCb" alt=""><figcaption></figcaption></figure>

## Final Words

As a reminder, you can reset things back to default if you need to

<figure><img src="/files/VLeR62SZeCdPX0w39mVa" alt=""><figcaption></figcaption></figure>

A TimeStamp is used in the Virtual Machine Name so you should always be able to quickly identify the last one you created.  Finally, if you have a failed deployment, you can Apply the initial Checkpoint to reset the Virtual Machine to a newly created state

<figure><img src="/files/NurhYMlOXg7Yi9FwI8jK" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-vm/new-osdcloudvm.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
