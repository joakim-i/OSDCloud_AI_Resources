> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/build-process.md).

# Build Process

The next few screenshots will detail the steps that are needed to make OSDCloud work

### Initialize

1. Start writing the PowerShell Transcript
2. Mirror the ADK Media directory to the OSDCloud Template
3. Copy the ADK winpe.wim to the OSDCloud Template boot.wim
4. Mount the boot.wim
5. Mount the WinPE registry to get the WinPE Info

<figure><img src="/files/eUNa5bOQdw0gXqYe2akx" alt=""><figcaption></figcaption></figure>

### ADK Packages

1. Inject ADK Packages for PowerShell functionality
2. Save the Windows Image

<figure><img src="/files/hECLEN2S4vnMknW0uNG1" alt=""><figcaption></figcaption></figure>

### Tweaks

1. Copy some helper files from the running OS
2. If MDT is installed, add the Dart Configuration
3. If Microsoft Dart is installed, inject the Tools
4. Save the Windows Image
5. Set the WinPE PowerShell ExecutionPolicy
6. Enable PowerShell Gallery support
7. Remove winpeshl.ini if it is present
8. Change some settings for a better Command Prompt experience

<figure><img src="/files/UaaL0PSWaGSQkJEmNo6Y" alt=""><figcaption></figcaption></figure>

### Packages

1. Display the installed Windows Packages

<figure><img src="/files/kXOQD9hMgtE6tKCoMBUo" alt=""><figcaption></figcaption></figure>

### Complete

1. Dismount the Windows Image
2. Export the Boot.wim to compress the file
3. Create empty configuration directories
4. Create the ISOs
5. Set the OSDCloud Template to the new path
6. Stop writing the PowerShell Transcript

<figure><img src="/files/IpQXpElxHNNYi3NCzffK" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/setup/osdcloud-template/build-process.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
