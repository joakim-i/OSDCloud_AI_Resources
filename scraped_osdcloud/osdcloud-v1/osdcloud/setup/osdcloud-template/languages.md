> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/languages.md).

# Languages

## -Language

You can add additional languages to your WinPE by using the `Language` parameter.  In my example, I used the ADK winpe.wim and added Spanish and French to my English US WinPE so I gave a Name that will help me identify the added languages

<figure><img src="/files/DPjrvZRw9DxGQA6243bJ" alt=""><figcaption><p>New-OSDCloudTemplate -Name 'ADK en es fr' -Language es-es,fr-fr</p></figcaption></figure>

## -SetInputLocale

This parameter allows me to set the default keyboard to something else, like English (US) Dvorak

<figure><img src="/files/C4uyS4nrsDPloV8eecTL" alt=""><figcaption><p>New-OSDCloudTemplate -Name 'ADK en Dvorak' -SetInputLocale '0409:00010409'</p></figcaption></figure>

## -SetAllIntl

Finally, I can change all the International Defaults to one of the added Languages using this parameter.  This will make the following changes

* UI language
* System locale
* User locale
* Input locale

<figure><img src="/files/QSvgOVlPUx7uChfaSks4" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/languages.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
