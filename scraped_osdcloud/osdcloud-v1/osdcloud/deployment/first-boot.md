> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud/deployment/first-boot.md).

# First Boot

During First Boot (Specialize Phase), any EXE based DriverPacks in C:\Drivers will be expanded.  Once expanded, they will be applied using the following PowerShell commands

```powershell
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths" -Name 1 -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths\1" -Name Path -Value $DestinationPath -Force
pnpunattend.exe AuditSystem /L
Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths\1" -Recurse -Force
```

You can identify this phase by the "Getting ready"&#x20;

<figure><img src="/files/A70YAPmke5EAvdMvt16k" alt=""><figcaption></figcaption></figure>

## Dell Systems

Dell uses CAB files or EXE files that can be expanded in WinPE, so there is no activity in First Boot other than a long delay.  You can review the logs in C:\Windows\debug

```powershell
Start-Process -FilePath $ExpandFile -ArgumentList "/s /e=`"$DestinationPath`"" -Wait

Write-Verbose -Verbose "$((Get-Date).ToString('yyyy-MM-dd-HHmmss')) Applying DriverPack with PNPUNATTEND"
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths" -Name 1 -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths\1" -Name Path -Value $DestinationPath -Force
pnpunattend.exe AuditSystem /L
Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths\1" -Recurse -Force
```

## HP Devices

HP DriverPacks are silent, so there is no progress displayed during this phase other than a long delay.  You can review the logs in C:\Windows\debug

```powershell
Start-Process -FilePath $ExpandFile -ArgumentList "/s /e /f `"$DestinationPath`"" -Wait

Write-Verbose -Verbose "$((Get-Date).ToString('yyyy-MM-dd-HHmmss')) Applying DriverPack with PNPUNATTEND"
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths" -Name 1 -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths\1" -Name Path -Value $DestinationPath -Force
pnpunattend.exe AuditSystem /L
Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths\1" -Recurse -Force
```

<figure><img src="/files/UAYeymVQd7pN2at9E9FN" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/DMoK1hCXVU12jVKYdtM7" alt=""><figcaption></figcaption></figure>

## Lenovo Devices

Lenovo devices will display a progress when the DriverPacks is expanded

```powershell
Start-Process -FilePath $ExpandFile -ArgumentList "/SILENT /SUPPRESSMSGBOXES" -Wait

Write-Verbose -Verbose "$((Get-Date).ToString('yyyy-MM-dd-HHmmss')) Applying DriverPack with PNPUNATTEND"
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths" -Name 1 -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths\1" -Name Path -Value $DestinationPath -Force
pnpunattend.exe AuditSystem /L
Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UnattendSettings\PnPUnattend\DriverPaths\1" -Recurse -Force
```

<figure><img src="/files/YmoGtfFrsyTraFF9s7Z1" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/ipNP8NObBEMmzO0dckYR" alt=""><figcaption></figcaption></figure>

## Microsoft Surface Devices

Microsoft uses MSI DriverPacks which expanded silently, so there is no activity in First Boot other than a long delay.  You can review the logs in C:\Windows\debug&#x20;

```powershell
$DateStamp = Get-Date -Format yyyyMMddTHHmmss
$logFile = '{0}-{1}.log' -f $ExpandFile,$DateStamp
$MSIArguments = @(
	"/i"
	('"{0}"' -f $ExpandFile)
	"/qb"
	"/norestart"
	"/L*v"
	$logFile
)
Start-Process "msiexec.exe" -ArgumentList $MSIArguments -Wait -NoNewWindow
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud/deployment/first-boot.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
