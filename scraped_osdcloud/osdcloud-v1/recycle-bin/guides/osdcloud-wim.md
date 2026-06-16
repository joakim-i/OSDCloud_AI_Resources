> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/guides/osdcloud-wim.md).

# OSDCloud WIM

{% hint style="warning" %}
Make sure you are running OSD Module 21.4.15.4 or newer.  There was a bug in the previous version that will make this fail
{% endhint %}

So you want to use your custom WIM wth OSDCloud?  This is how you do it.  This is a LOCAL wim file for now, but this will be expanded to download a wim from a URL in the near future

## OSDCloud OS

In your OSDCloud Workspace, you have an OS directory.  Put your WIM in here.  In my case, I downloaded the Windows Server 2022 Insider Preview ISO and simply expanded it with 7-Zip.  Don't over-complicate this and make it difficult.  Give it a path so you know what it is

![](/files/-MYLy78ouP6lWvLCpNvc)

{% embed url="<https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewserver>" %}

### USB Considerations

If you are using an OSDCloud USB, then the process is similar, put it in the OSDcloud\OS directory of your OSDCloud partition.  Again, don't over-complicate this

![](/files/-MYLzHhR3DQmivFVTW0q)

## The Path

It is important for you to remember this about the Path.  For OSDCloud to find it, it must be in a similar path (which is recursed)

```
<PSDrive:>\OSDCloud\OS\* -Recurse
```

That said, if my OSDCloud Workspace is at D:\OSDCloud, and I am in a Virtual Machine on the same computer, I can simply Map a Network Drive using DaRT if you have it installed, or a command line.  Make sure you don't map to an OS Drive Letter (C: R: S: X:) and you'll be fine.  I use O: for OSDCloud personally

![](/files/-MYM-9xxvU5V5JcPNyI_)

### USB Considerations

None.  If you are on a Physical computer and you put it in the OSDCloud OS path, then you're fine

## Start-OSDCloudWim

I always recommend installing the newest OSD Module first, then get cracking.  You will be presented with a Menu to select your Wim and Image Index

```
Install-Module OSD -Force
Import-Module OSD -Force

#Set the Display Resolution to whatever you want if you are in a VM
Set-DisRes 1600

Start-OSDCloudWim
```

![](/files/-MYM2XTqZzi5EMWPM044)

![](/files/-MYM35evlq8TFeDoFx_p)

![](/files/-MYM3nNryrqLXcr93k0X)

![](/files/-MYM3p8S1z1k8dNJMaYh)

![](/files/-MYM3qasmLhGaGd7KxuF)

![](/files/-MYM3sM1ORmVqhK5fg5N)

### Parameters

The ones you know and love are all there

![](/files/-MYM0hftUDAte8bnfaq0)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/guides/osdcloud-wim.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
