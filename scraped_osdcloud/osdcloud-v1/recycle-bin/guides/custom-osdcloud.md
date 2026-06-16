> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/guides/custom-osdcloud.md).

# Custom OSDCloud

I realize there is a need to customize the OSDCloud defaults, especially when you have to keep repeating things (OSLanguage, OSBuild, OSEdition, etc).  Without setting these somehow, there is an entry point for making mistakes due to lack of consistency.

This is easily demonstrated in a post from my good virtual friend Sune Thomsen in his tweet below.  One of my hopes has been to see what the Community does with OSDCloud, and he didn't disappoint.  He took the ball and ran with it, and shared his experience.

{% embed url="<https://twitter.com/SuneThomsenDK/status/1380608006942031876>" %}

While I did Like and Comment on his Tweet because he solved a problem that he had, I didn't entirely agree with his methods for a couple of reasons

### Hardcoding

This makes things a challenge when you want to make changes.  For example, if this method were used in an Enterprise, any changes to the settings (like when the OSBuild needs to change) would need a full rebuild.  Can you guarantee that everyone's USB sticks have been updated?

### Challenging

I would probably rate this a 4 out of 10 in difficulty due to the fact that you have to Mount the image, and add your settings manually.  I'd imagine Sune had to run through this several times before getting this right, which really stretches out testing considerably.  While this wasn't difficult for him, others that may want to go down this route may have issues

## Simply OSDCloud

In keeping with my topical with my  post on [**KISS**](https://osdcloud.osdeploy.com/concepts/kiss), I'll show you how to Simplify this process and make things more Dynamic.

First and foremost, it's called OSDCloud ... so in keeping with the Cloud part of the name, I can write a PowerShell Script and put that on GitHub as a file or a Gist.  I'll add whatever I want to do in this script, such as setting the Display Resolution for Virtual Machines, or Ejecting the ISO (not solved yet).  Buried in this script is my Start-OSDCloud command line which I set my OSLanguage and other stuff.  Finally I need to get the raw URL using the Raw button

![](/files/-MYAkG5XiBWK0bWwQJtU)

So this is what I have now

```
https://raw.githubusercontent.com/OSDeploy/OSDCloud/main/Demo-CustomOSDCloud.ps1
```

## Edit-OSDCloud.winpe -WebPSScript

I added this parameter to give you the ability to execute a PowerShell script on the Internet using the **`Invoke-WebPSScript`** function, which ironically was released the same day as OSDCloud (this was not a coincidence)

![](/files/-MYArxp1n1V5at-d8grB)

This can be applied using the new **`WebPSScript`** parameter to WinPE

```
Edit-OSDCloud.winpe -WebPSScript https://raw.githubusercontent.com/OSDeploy/OSDCloud/main/Demo-CustomOSDCloud.ps1 -Verbose
```

![](/files/-MYArIqxjHxJfs16zeX1)

## Execution

As you can see from the screenshot below, Startnet.cmd is modified to execute my PowerShell script on GitHub which handles anything I want to do before and after Start-OSDCloud, as well as setting my defaults.  Changing my parameters is as easy as changing the script on GitHub and there is no need to ever go back and update WinPE unless I need to make changes.

![](/files/-MYAsvsUA-ZBPDVNrC5v)

For those that are interested, here is what the final Startnet.cmd looks like

![](/files/-MYAveE8sKljgv_UP7sC)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/guides/custom-osdcloud.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
