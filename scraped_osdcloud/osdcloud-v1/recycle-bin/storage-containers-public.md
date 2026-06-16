> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/storage-containers-public.md).

# Storage Containers (Public)

{% embed url="<https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction>" %}

A Public Container should only be used to store a Public WinPE ISO for easy access.  You should not store anything else in this container.  This step is completely optional, but this process allows for downloading an ISO whenever needed

To create a Public Container, follow these steps

![](/files/ZMFSDlbfRpxOy9TwZmVh)

![](/files/XRBNZw117aRrKAxj7BXA)

## Upload OSDCloud ISO

You can now select your public Storage Container and upload a WinPE ISO.  Make sure this does not contain any Autopilot Configuration files

Select Upload and then browse to your ISO.  You will need to select Overwrite since we have not added any Access Control yet, and use the Account key option for the upload

![](/files/UIofFwynchkpJzAZf33Z)

## Download OSDCloud ISO

After the ISO has been uploaded to the Container, you should now have an ISO that can be downloaded at any time needed&#x20;

![](/files/h7JDHg5mQlEU0TutDrJV)

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
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/storage-containers-public.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
