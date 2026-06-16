> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-accounts.md).

# Storage Accounts

{% embed url="<https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview>" %}

## Basics

To deploy from Azure, you will first need a Storage Account.  Make sure you pick a good Region as this will impact costs.  Don't go crazy here, you are serving up a 4GB WIM, so Standard Performance and Local Redundancy should work fine

![](/files/sKroknl9nbGBWEEEHVje)

## Advanced

You will need to decide if you want Public Access or not. This does not enable it by default, it only gives the option to enable it later.  I recommend this as a method of keeping a WinPE ISO that can be easily accessed if needed, but you will need to decide what is best for your environment

Yes, default to Azure Active Directory authorization

Do the math on the calculator.  You will be accessing date more frequently than writing data, and I have found that the Hot comes out cheaper than Cool for the Access Tier

![](/files/88waEzJYAyvZb7syv1WB)

## Networking

This will vary, but I generally leave the defaults

## Data Protection

You should not need Recovery ... but that's your call

It's a good idea to enable Tracking if multiple people have write access to the Storage Account.  Versioning is not necessary, just upload an image with a different name as that should contain version information as a best practice anyway

![](/files/byeqIMiChvnjMtamcfiE)

## Encryption

I leave this as Default

## Tags

OSDCloud requires a Storage Account Tag for proper integration.  The Name should be OSDCloud and the Value can be anything you want.  Make sure to select the Tag only for the Storage Account

![](/files/QFKEoZwjwR38Gx7P4cbj)

During the WIM selection of the Azure OSDCloud Deployment, the Tag is displayed with the Storage Account

![](/files/CGllumUlU1VbxUB4vnAk)

## Review + Create

Do it.

![](/files/xnDQ1ecKPikHyid0IKUI)

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
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/azure-setup/azure-portal/storage-accounts.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
