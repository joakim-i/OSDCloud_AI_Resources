> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/integration/adk-use-the-osdcloud-boot.wim.md).

# ADK: Use the OSDCloud Boot.wim

If you feel brave, you can update the Windows ADK with an OSDCloud Template.  This will ensure that any MDT and CM Boot Images are automatically updated with an OSDCloud certified WinPE

## Backup ADK amd64

First thing is first, make a backup of of your ADK WinPE amd64.  I prefer to make a copy in place.

{% code fullWidth="true" %}

```
C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64
```

{% endcode %}

<figure><img src="/files/dHaTaX6z8ZRhD9lYFcbG" alt=""><figcaption></figcaption></figure>

## Delete Media Contents

Delete the contents of your Media directory

```
C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Windows Preinstallation Environment\amd64\Media
```

<figure><img src="/files/NUarO1S5dANAy0NKxm78" alt=""><figcaption></figcaption></figure>

## Copy OSDCloud Template Media

Copy the contents of your OSDCloud Template Media to your ADK amd64 Media except the sources directory.  You can also opt to leave out languages that you don't support

<figure><img src="/files/9RmX3WJbBxsKIZVezkyB" alt=""><figcaption></figcaption></figure>

## Media Cleanup

Optionally you can cleanup Language files in your Boot and EFI directories that you don't need

<figure><img src="/files/F3GPXWw1sIBaIYahut10" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/HYf1Dc7KxFIZsACXXKho" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/pAjRifLTkQ0WwEN5YiEK" alt=""><figcaption></figcaption></figure>

You can also delete about 25MB of fonts if you're not into supporting Asian languages too

<figure><img src="/files/hVPJaipG4aSV1xxtt8f0" alt=""><figcaption></figcaption></figure>

## Replace winpe.wim

Replace the ADK winpe.wim with your OSDCloud Template boot.wim

<figure><img src="/files/aRwJHQOVBT1qnDiesHi1" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/integration/adk-use-the-osdcloud-boot.wim.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
