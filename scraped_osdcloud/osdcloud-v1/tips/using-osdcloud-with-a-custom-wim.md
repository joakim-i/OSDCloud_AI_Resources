> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/tips/using-osdcloud-with-a-custom-wim.md).

# Using OSDCloud with a Custom WIM

You can use a CustomImage with Start-OSDCloud by either specifying a URL, or placing the file on a USB or Network Share

## -ImageFileUrl

If you happen to have a URL for a WIM or an ESD, you can specify that using the **`-ImageFileUrl`** parameter.  Make sure you include **`-ImageIndex`**, otherwise it will default to 1

![](/files/-MZ12p94JwzoegwZwye8)

![](/files/-MZ145LSqQYsUI1tzU8v)

### Invoke-OSDCloud Variables

These are passed from **`Start-OSDCloud -ImageFileUrl`** to **`Invoke-OSDCloud`** for processing

![](/files/-MZ136XUplec5SgzcmDo)

## -FindImageFile

If you have a Custom WIM or an ESD file, simply place it in a the following path (subdirectories are good) on a USB Drive or Network Share

```
<DriveLetter>:\OSDCloud\OS\*
```

OSDCloud will scan the above path on available drives for image files, as long as they are WIM or ESD Files

{% hint style="warning" %}
Only Drive Letters D-Z  except X: because that's WinPE (C: isn't checked because it will be wiped)
{% endhint %}

In my example below, I have mapped a Network Drive which contains the OSDCloud OS Path and 4 OS Images have been found.  After selecting an ImageFile, I will be prompted to select an ImageIndex

![](/files/-MYpxddl_gOOYk6s2k2w)

### Invoke-OSDCloud Variables

My example above will pass these variables to Invoke-OSDCloud for processing

![](/files/-MYpyO_xUk5mmAGNZjcx)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/tips/using-osdcloud-with-a-custom-wim.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
