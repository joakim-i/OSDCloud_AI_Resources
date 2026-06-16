> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/oobe/start-oobe.autopilot.md).

# Start-OOBE.autopilot

This function makes it easy for AutoPilot Manual Registration.  It will get stuck in a loop if you don't have an internet connection to powershellgallery.com

![](/files/-MWNhaOKE68FQ5PO7xRb)

If you need to connect Wi-Fi, just **`CTRL + C`** to break out of this function and run **`Start-OOBE.wifi`**

![](/files/-MWNhnbJ8OPL3xRIfVIN)

Once you have a good internet connection, run **`Start-OOBE.autopilot`** again and it will install all the Required Modules

![](/files/-MWNi1w-hA4t2olHQkxX)

![](/files/-MWNiDLH7VR8v42o60Sf)

![](/files/-MWNiKsb-s42La5xHK2O)

## Get-WindowsAutoPilotInfo Script

Finally the script you need will be installed

![](/files/-MWNiS-k9pr7VUI7T-El)

## New PowerShell Session

A new PowerShell session will open so you can do your AutoPilot business.  This lets you break out of the **`Start-OOBE.autopilot`** routine if there are additional steps that you need to run

![](/files/-MWNiWhUNQEL77teNjij)

![](/files/-MWNifA0FvnCE3qSEIkt)

![](/files/-MWNinx-zhH0TBIiNPF2)

![](/files/-MWNislPEQZteRdmxvJn)

## Sysprep

Finally when you close the new PowerShell session, you will be prompted to press Enter to start Sysprep.  One you press Enter, the following steps will occur

1. Set-ExecutionPolicy RemoteSigned
2. Sysprep /oobe /reboot

Once this is complete you should be back in OOBE ready for AutoPilot

![](/files/-MWNj1XiswkZ3jBxQQ11)

![](/files/-MWNj7UussZSpzaBIIIY)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/oobe/start-oobe.autopilot.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
