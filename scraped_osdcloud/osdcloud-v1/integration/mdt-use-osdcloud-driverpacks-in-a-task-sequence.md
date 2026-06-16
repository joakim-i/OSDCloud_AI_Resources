> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/integration/mdt-use-osdcloud-driverpacks-in-a-task-sequence.md).

# MDT: Use OSDCloud DriverPacks in a Task Sequence

## Preinstall Phase

### Modify Inject Drivers step

Modify your Task Sequence to include drivers from the **OSDCloud WinPE x64** selection profile that was created in the [**WinPE Drivers**](/osdcloud-v1/integration/mdt-add-osdcloud-winpe-drivers.md) configuration. This will ensure that you have the minimal Network and Disk Controller drivers needed to startup the Operating System to first boot

<figure><img src="/files/n8GsbqcGYkRqsHys6S0U" alt=""><figcaption></figcaption></figure>

## Install Phase

### Add Run Command Line step

Add a **Run Command Line** step to your Task Sequence prior to **Install Operating System** to load the [**OSDCloud Sandbox**](/osdcloud-v1/osdcloud-sandbox/sandbox.md).  This will ensure that you have the latest OSDCloud dependencies in your WinPE Session.  Use the following for the Command line

```
PowerShell -ExecutionPolicy Bypass -Command "Invoke-Expression (Invoke-RestMethod 'sandbox.osdcloud.com')"
```

Make sure you do not 'Continue on error' because if this fails to load, then you will probably not be able to download DriverPacks

<div><figure><img src="/files/JZ5XTlVf4p8obDXcpYdV" alt=""><figcaption></figcaption></figure> <figure><img src="/files/FoqsklXCmjJAnLpCp2eQ" alt=""><figcaption></figcaption></figure></div>

## Postinstall Phase

### Add Run Command Line step

After Configure, add a Run Command Line step called **OSDCloud DriverPackMDT**.  Use the following for the Command line

```
cmd.exe /c start /wait PowerShell -ExecutionPolicy Bypass -Command Invoke-OSDCloudDriverPackMDT
```

Start in should contain the following path

```
%OSDisk%\Windows\System32
```

Options should include **Continue on error**

<div><figure><img src="/files/kS7ntAT42JzmeRPQ8eRB" alt=""><figcaption><p>Run Command Line</p></figcaption></figure> <figure><img src="/files/m7q7v98oePRnEyhoCrbD" alt=""><figcaption><p><strong>Continue on error</strong></p></figcaption></figure></div>

### OSDCloud DriverPackMDT Step for VM Testing

If you want to test downloading and applying a DriverPack in a Virtual Machine, modify the above step to specify a Manufacturer and Product.  I select a Lenovo as the DriverPack as HP and Dell do not show progress in the Specialize phase during the DriverPack expansion

```
cmd.exe /c start /wait PowerShell -ExecutionPolicy Bypass -Command Invoke-OSDCloudDriverPackMDT -Manufacturer Lenovo -Product 21DC
```

## Test a Deployment

The following screenshots are from a Virtual Machine emulating a Lenovo P1 Gen 5 device

<figure><img src="/files/l58bJCH2cUmR9fJEVXsg" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/TkO9UYPoXwpNQAjknRhc" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/rjarBC8YlA9bVitSf7Gi" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/YhwylfFSLfC91unx0F62" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/AtpjT7vNT6ZWxlB0Axf3" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/r4tHQV0u3tMVqm5wKuGk" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/3ig7bEBq95u2Tikc1Emk" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/OhiC0ifb0kddLgFBfiKO" alt=""><figcaption><p>This part may take 5-10 minutes.  Most DriverPacks will not show any progress</p></figcaption></figure>

<figure><img src="/files/dYmH4VkveQh12z2FzS0V" alt=""><figcaption><p>Lenovo is the exception where you will see the expand of the DriverPack</p></figcaption></figure>

<figure><img src="/files/14GEepnYLIqH5J16eVz1" alt=""><figcaption><p>Complete deployment with no errors</p></figcaption></figure>

<figure><img src="/files/sKSgGbqX7wN0CtynCv0m" alt=""><figcaption><p>PPKG DriverPack expand and apply in Specialize will be saved in C:\Windows\debug</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/integration/mdt-use-osdcloud-driverpacks-in-a-task-sequence.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
