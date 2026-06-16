> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deep-dive/log-files.md).

# Log Files

If you run into issues in WinPE, there are several files that you can use for reference.  The details of the Windows Image or ISO that you selected are contained in root of X:\\.  These files are only available in WinPE and are destroyed as soon as the computer reboots

![](/files/9zUGr5V3obQAs59g0I4A)

More detailed logs are located in X:\OSDCloud\Logs. These files are also no longer available after you reboot

![](/files/ZEcsLk9chS1aKDkJ64R9)

Finally, C:\OSDCloud\Logs will contain OSDCloud.json which is an export of all the OSDCloud Variables. This file will persist after rebooting from WinPE

![](/files/puHXDDDM4q3ZMJ8AZW6W)

## Sponsor

{% embed url="<https://www.recastsoftware.com/?utm_source=osdeploy&utm_medium=ad&utm_campaign=web>" %}
OSDeploy is sponsored by Recast Software
{% endembed %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deep-dive/log-files.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
