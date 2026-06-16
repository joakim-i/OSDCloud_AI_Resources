> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deployment/testing.md).

# Testing

Once you have your Azure Setup complete, you may want to test OSDCloud Azure to see how it will perform in your environment.  You can complete this test in Windows in an Admin Elevated PowerShell Session.  Make sure you have the OSD PowerShell Module 22.6.1 or newer

1. Run Start-OSDCloudAzure. You will be prompted to connect to Azure and may have to select your Subscription if you have more than one
2. Make a note that you are able to see your OSDCloud tagged Storage Accounts with optional BootImage and DriverPack Storage Containers
3. Verify you are able to see all your OSDCloud tagged Storage Accounts with the appropriate Containers
4. Verify that you have all your available OS Images in OSDCloud Azure.  You can press Start if you want to continue with the test

![](/files/g1LjCZAiSIy6AGrsz4b9)

The test will download the Blob Image from Azure Storage and the proper Driver Pack for your system

![](/files/iIQaUHx2u19Fmij0JktY)

When complete, the script will stop so you can verify that everything worked.  If it did, you're ready to repeat the process in WinPE

![](/files/FR58aZ0H0GGFhS3DgI9j)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deployment/testing.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
