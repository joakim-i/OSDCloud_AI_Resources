> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-sandbox/sandbox.md).

# OSDCloud

The **Sandbox** is a way test OSDCloud without using a dedicated OSDCloud WinPE.  It is a PowerShell that will setup all of the OSDCloud prerequesties, although you will need to have PowerShell working in your WinPE

## Sandbox URL

The **OSDCloud Sandbox** can be accessed at this URL

```
sandbox.osdcloud.com
```

If you open this URL in your web browser, you will be redirected to the following RAW link on GitHub where you can review the script

{% embed url="<https://raw.githubusercontent.com/OSDeploy/OSD/master/cloud/subdomains/sandbox.osdcloud.com.ps1>" %}

## Invoke-RestMethod

You can return the script in PowerShell using this cmdlet

```powershell
Invoke-RestMethod sandbox.osdcloud.com
```

<figure><img src="/files/d1npU0gEaVObvqVwldNy" alt=""><figcaption></figcaption></figure>

## Invoke-Expression

This cmdlet is used to run a PowerShell script.  Understanding that, you can use any of the following one-liners to execute the OSDCloud Sandbox PowerShell script in WinPE

```powershell
Invoke-Expression (Invoke-RestMethod 'https://sandbox.osdcloud.com')
Invoke-Expression (Invoke-RestMethod sandbox.osdcloud.com)
iex (irm sandbox.osdcloud.com)
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-sandbox/sandbox.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
