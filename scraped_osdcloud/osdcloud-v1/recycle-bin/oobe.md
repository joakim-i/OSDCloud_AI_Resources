> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/oobe.md).

# OOBE

These functions should help you out when you are in OOBE

![](/files/-MWNfUhDcCs2PKEvqqJB)

Start by pressing SHIFT + F10 to open a Command Prompt

![](/files/-MWNfjiPrPTfO1HqaOQE)

Now run PowerShell

![](/files/-MWNfr8RgoRgNZqbKCNp)

And Set your ExecutionPolicy to RemoteSigned

{% hint style="warning" %}
Yes, I set it to Bypass in these screenshots and didn't feel like starting over ... this is addressed in **`Start-OOBE.autopilot`**
{% endhint %}

![](/files/-MWNgFm-dUs7ekTRCzcW)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/oobe.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
