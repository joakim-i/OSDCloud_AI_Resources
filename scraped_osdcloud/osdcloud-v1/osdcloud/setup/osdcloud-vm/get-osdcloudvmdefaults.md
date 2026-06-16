> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-vm/get-osdcloudvmdefaults.md).

# Get-OSDCloudVMDefaults

There function is used to return the OSDCloudVM defaults.  The defaults are set in the OSD Module by importing the settings from the **`OSD.json`** file that exists in the root of the OSD Module.  This file cannot be changed

<figure><img src="/files/jPtI3xUm6Yz6cChImqM1" alt=""><figcaption></figcaption></figure>

When creating a new OSDCloud VM, these defaults will be used to create the Virtual Machine.  Most of the values used are defaults that are required for Windows 11, although I would recommend using more powerful settings if your system can handle it.  The defaults represent the Minimum level that should be used with an OSDCloud VM

```json
{
  "CheckpointVM": true,
  "Generation": 2,
  "MemoryStartupGB": 4,
  "NamePrefix": "OSDCloud",
  "ProcessorCount": 1,
  "StartVM": true,
  "SwitchName": null,
  "VHDSizeGB": 64
}
```

<figure><img src="/files/FaODxAmHo6rRqPsM5d21" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-vm/get-osdcloudvmdefaults.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
