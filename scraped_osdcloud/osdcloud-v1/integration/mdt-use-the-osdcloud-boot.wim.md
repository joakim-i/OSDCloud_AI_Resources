> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/integration/mdt-use-the-osdcloud-boot.wim.md).

# MDT: Use the OSDCloud Boot.wim

If you've replaced your ADK with OSDCloud ADK, using Microsoft Deployment Toolkit is about to get much easier

## Create an ADK x86 directory

To prevent errors in MDT, you will need to make sure the following directories exist

{% code fullWidth="true" %}

```
C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Windows Preinstallation Environment\x86
C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Windows Preinstallation Environment\x86\WinPE_OCs
```

{% endcode %}

<figure><img src="/files/5ppvpQZPIlqJjmWVF94j" alt=""><figcaption></figcaption></figure>

## Create a new MDT Deployment Share

<figure><img src="/files/jD5ckbXSdE54aO4jJvuE" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/aJFUxsVbHaFPdHaBniC8" alt=""><figcaption></figcaption></figure>

## Remove x86 Support

Because ADK doesn't support that anymore

<figure><img src="/files/BeNyv41QJMWqEeRIl2es" alt=""><figcaption></figcaption></figure>

## Configure x64

Configure how you want your MDT x64 boot image

<figure><img src="/files/MWZqOooHK6IITAam7WMU" alt=""><figcaption></figcaption></figure>

If you don't need Microsoft Data Access Components (MDAC/ADO) support, uncheck that.  Everything else you need should already be configured with your OSDCloud ADK

<figure><img src="/files/xjIWRH1kxBqPjBnYC8dD" alt=""><figcaption></figcaption></figure>

## Update Deployment Share

Now you can update your Deployment Share and build your WinPE.  If you're not adding Drivers, it should take less than a minute since all the WinPE Packages you need are already installed

<figure><img src="/files/N3r0APxi3wUBzvqp8dKk" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/jHMNo5XsdLbhKVQCivaq" alt=""><figcaption></figcaption></figure>

## Test Boot

Looks perfect with Windows Recovery Wizard since I used WinRE and DaRT already installed

<figure><img src="/files/vJfSi5NI7jKVze3XeUot" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/iubAOC6jdqg53hf6z7o5" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/NLglMAWhH8oP6WaOrXqr" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/integration/mdt-use-the-osdcloud-boot.wim.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
