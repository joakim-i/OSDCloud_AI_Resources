> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/public-content.md).

# Public Content

I really enjoy having Microsoft DaRT in my WinPE so I can use Explorer, but I also share out my ISO's sometimes and I can't really do that as Microsoft DaRT is licensed.   The way I get around this is by adding the word 'Public' in the `Name` and DaRT won't be added.  This makes it easy to share out some of my work and not forgetting about breaking the Microsoft rules

<figure><img src="/files/oESOxeCGnPRhzcfr36if" alt=""><figcaption><p>New-OSDCloudTemplate -Name Public</p></figcaption></figure>

<figure><img src="/files/ph0iUKUmMIKsZFsTGaM3" alt=""><figcaption><p>New-OSDCloudTemplate -Name 'Public WinRE' -WinRE</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/public-content.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
