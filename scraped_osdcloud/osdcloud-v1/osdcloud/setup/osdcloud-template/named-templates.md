> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/named-templates.md).

# Named Templates

There may come a time when you need to create multiple OSDCloud Templates.  I'll get into this further in the next few pages, but let's cover the basics here

## -Name

To create a named OSDCloud Template, simply use the `Name` parameter

<figure><img src="/files/15RxaXsGUXBVPHShKuov" alt=""><figcaption><p>New-OSDCloudTemplate -Name 'My New Profile'</p></figcaption></figure>

## Get-OSDCloudTemplate

When you create a new OSDCloud Template, that will be the one that gets used by default going forward, until it is changed.  To find out what your current OSDCloud Template is, use this function

```powershell
PS C:\> Get-OSDCloudTemplate
C:\ProgramData\OSDCloud\Templates\My New Profile
```

## Get-OSDCloudTemplateNames

This function will return all the OSDCloud Templates that have been registered&#x20;

```powershell
PS C:\> Get-OSDCloudTemplateNames
default
My New Profile
```

## Set-OSDCloudTemplate

This function will If you have more than one OSDCloud Template, you can change between OSDCloud Templates using this function and the `Name` parameter

```powershell
PS C:\> Set-OSDCloudTemplate #without params, returns to default
C:\ProgramData\OSDCloud

PS C:\> Set-OSDCloudTemplate -Name 'My New Profile'
C:\ProgramData\OSDCloud\Templates\My New Profile

PS C:\> Set-OSDCloudTemplate -Name default
C:\ProgramData\OSDCloud
```

By the way, there is Tab-Complete to make your life easier

<figure><img src="/files/jPl7HAhaBuSojWpYoQwh" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/named-templates.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
