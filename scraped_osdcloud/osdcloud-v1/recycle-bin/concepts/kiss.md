> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/kiss.md).

# K.I.S.S.

There is one thing that I have tried to focus on with OSDCloud from the beginning, it is to KEEP IT SIMPLE SIMPLE

For example in the picture below ... adding parameters to do anything imaginable is not simple, or easy to work with, nor should this be the goal.  This is a good example of the Law of Diminishing Returns.  At some point you end up over-complicating something that should never be that difficult

![](/files/-MYAbN32YeJYKuz7o8DW)

All of this should be common sense with OSDCloud, from the way you create your OSDCloud.template.  I didn't leave you with a list of which ADK Optional Components that you needed to add manually, I did that for you without parameters or any DISM knowledge.  CloudDrivers is another point.  This could have been left for you to download and apply, but that's not a simple task for lots of people.  And the creation of two different ISOs for satisfying the needs of the people that don't need a prompt to boot to ISO.

OSDCloud was not intended to only be used by the Technically apt, but everyone

## The Non-Solution

Finally, if you are looking at **OSDCloud** as the Solution, then you haven't been listening to what I've said, or what I've demonstrated.  It is not a Solution.  It is not the Solution.

I have said from the beginning that it is an Example of what YOU can do.  I strongly suggest you read my thoughts on the Wizard of Oz in the following link

{% content-ref url="/pages/-MX0kFNKXKsnVuObSV\_4" %}
[Broken mention](broken://pages/-MX0kFNKXKsnVuObSV_4)
{% endcontent-ref %}

Hopefully it will be crystal clear, the Solution is not OSDCloud, but the OSD Module which can be added to so you can do all the customizations you want, or to simplify your Deployments.  The people that have taken from OSDCloud to put DriverPacks in CM or MDT get it.  They are using what they need from the OSDCloud Example to solve things.

That said, if you feel that there is something that needs to be simplified, like installing Updates to the Offline OS, updating OneDrive, or DAT files, or enabling NetFX, then let's put that in a simple Function in the OSD Module to do all the manual work, and to simplify things.  Look for a follow-up to this on how to use those simple Functions to be YOUR Solution


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/concepts/kiss.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
