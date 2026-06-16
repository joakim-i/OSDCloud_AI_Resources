> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-automate/provisioning/msi-application-ppkg.md).

# MSI Application PPKG

I'll walk you through how to create a Provisioning Package for OS Deployment. In this example, I'll be working with Google Chrome Enterprise.  Start by downloading the MSI from this link

{% embed url="<https://chromeenterprise.google/browser/download/#windows-tab>" %}

On that link, you can select the Google Chrome you want to download.  I'm following these options

1. Stable
2. MSI (not bundle)
3. 64 bit Architecture
4. Make a note of the version, in my case it is 113.0.5672.127
5. Download the file to your Downloads directory

<figure><img src="/files/nrJqLKAs4jsxBZ81nbmh" alt=""><figcaption></figcaption></figure>

## Windows Configuration Designer

You should have Windows Configuration Designer installed.  Open it and select Advanced provisioning

<figure><img src="/files/YJKd81tOCVxkta9v7RPT" alt=""><figcaption></figcaption></figure>

Enter the details of your Project.  The Name field doesn't take periods well, so keep that in mind.  Pres Next

<figure><img src="/files/QtOr3PxAfr8NdLOziy2f" alt=""><figcaption><p>(1) Enter project details (2) Press Next</p></figcaption></figure>

<figure><img src="/files/D9tHw0oQskNvx7MoJ20S" alt=""><figcaption><p>(1) All Windows desktop editions (2) Press Next</p></figcaption></figure>

<figure><img src="/files/c8B4GlhX8rhyGnuVHFbG" alt=""><figcaption><p>Press Finish</p></figcaption></figure>

## Runtime settings

Complete the following steps

1. Expand Runtime settings
2. Expand to ProvisoiningCommands, Primary Context, Command
3. Add a Name for the install.  I chose Install
4. Press the Add button

<figure><img src="/files/tYkhfZusahRMbjcR5Ek5" alt=""><figcaption></figcaption></figure>

Complete the following steps

1. Select the Name that you selected for step 3 in the last screenshot. For me, this is Install
2. CommandFile: Browse to the Google Chrome Enterprise that was downloaded earlier
3. Commands
   1. CommandLine: msiexec /i "googlechromestandaloneenterprise64.msi" /passive /norestart
   2. ContinueInstall:  TRUE.  You don't want this to kill your deployment if the installation fails
   3. RestartRequired:  FALSE.
4. Export Provisioning Package

<figure><img src="/files/OV23OlCbQr2GZPdDC8bb" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/C8eQrVvkrL4xRB2l23ju" alt=""><figcaption><p>(1) Describe the provisioning package (2) Press Next</p></figcaption></figure>

<figure><img src="/files/gqPfGiE8ZNo2dK1coK8a" alt=""><figcaption><p>Press Next</p></figcaption></figure>

<figure><img src="/files/rXv904Oeg2SmN8Si3lGI" alt=""><figcaption><p>Press Next</p></figcaption></figure>

<figure><img src="/files/inEwdMTUiSM64GJB1roJ" alt=""><figcaption><p>Press Build</p></figcaption></figure>

<figure><img src="/files/1K5hQnLr2BotzRCgcipP" alt=""><figcaption><p>Click on the Project folder link</p></figcaption></figure>

<figure><img src="/files/YRH4BRX3g2lVOEq9XLnT" alt=""><figcaption><p>Complete Provisioning Package</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-automate/provisioning/msi-application-ppkg.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
