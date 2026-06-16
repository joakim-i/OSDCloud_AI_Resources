> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup.md).

# Azure Setup

## Considerations

Before taking a Deep Dive at imaging from Azure, it's only fair to discuss some considerations

#### #1: This is New

It's so new that there isn't anything I can copy from, so I'm going to share as much information as possible so the Community can make some decisions going forward.  I'm just making this up as I go

#### #2: I'm no Expert

See #1

#### #3: Change is Likely

At this point, nothing is set in stone, so things will likely change, and you will need to adapt and get over it.  If you prefer things being more stable, come back in a few months

#### #4: Feedback

I'm not a mind reader.  Hit me up on Twitter and let's get a Community Pulse

#### #5: Goal

To deploy a Windows Image from Azure (Storage).  For now, this is a WIM file.  Nothing else at this time

#### #6: Differences

What works for me may not work for you

#### #7: Custom Development

Unless I'm on your Payroll, not likely.  See #4

#### #8: Training

I'll gladly help you with OSDCloud, but if you have specific Azure questions, consult Microsoft Docs.  I'll link where applicable

#### #9: Costs

Azure is not free, and Storage has costs, but it's cheap.  It should cost about $.50 per deployment.  Do the math to determine if this is a good fit for you

{% embed url="<https://azure.microsoft.com/en-us/pricing/calculator>" %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
