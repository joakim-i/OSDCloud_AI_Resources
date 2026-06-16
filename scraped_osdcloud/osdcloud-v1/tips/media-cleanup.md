> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/tips/media-cleanup.md).

# Media Cleanup

The default **OSDCloud Template** Media directory contains quite a bit of language resources

![](/files/vIp9aP5dMKrERu11TQjT)

These don't really do much for me as the only language in my WinPE is **en-us**.  This can be cleaned up a bit in PowerShell with these commands

```powershell
$KeepTheseDirs = @('boot','efi','en-us','sources','fonts','resources')
Get-ChildItem $env:ProgramData\OSDCloud\Media | Where {$_.PSIsContainer} | Where {$_.Name -notin $KeepTheseDirs} | Remove-Item -Recurse -Force
Get-ChildItem $env:ProgramData\OSDCloud\Media\Boot | Where {$_.PSIsContainer} | Where {$_.Name -notin $KeepTheseDirs} | Remove-Item -Recurse -Force
Get-ChildItem $env:ProgramData\OSDCloud\Media\EFI\Microsoft\Boot | Where {$_.PSIsContainer} | Where {$_.Name -notin $KeepTheseDirs} | Remove-Item -Recurse -Force
```

![](/files/TdnrpbhZAK5uSQtAKPMf)

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
GET https://www.osdcloud.com/osdcloud-v1/tips/media-cleanup.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
