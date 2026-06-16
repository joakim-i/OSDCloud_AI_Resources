> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-automate/autopilot.md).

# Autopilot

In this example, I'm going to copy an AutopilotConfigurationFile.json in my OSDCloud Workspace in the Media\OSDCloud\Automate directory.  Additionally, I'll copy a WIM to Media\OSDCloud\OS so that don't have to download an OS for my testing.

<figure><img src="/files/JI3TljtXCXfDzXaZAVC9" alt=""><figcaption></figcaption></figure>

## Boot to WinPE

Now I'll boot to a Virtual Machine to this ISO and start an OSDCloud deployment.  The screenshot below should help you visualize where the Autopilot file is on the ISO

<figure><img src="/files/dfON3ljxd5ljqLl6ylQ3" alt=""><figcaption></figcaption></figure>

You will see the AutopilotConfigurationFile.json is identified before the disk is wiped.  This is for you to validate that your process worked.

<figure><img src="/files/3ncXqvY0fouR7nQM4U5Y" alt=""><figcaption></figcaption></figure>

At the end of the OSDCloud deployment, the OSDCloud Automate will inject the Autopilot Configuration File automatically

<figure><img src="/files/0OT3gEbJRqTSB0EWb106" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-automate/autopilot.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
