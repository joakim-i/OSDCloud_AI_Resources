---
title: OSDCloud Workspace Architecture and Transformations
source_url: https://www.osdcloud.com/osdcloud-v1/osdcloud/workspace
version: OSD 23.5.21.1+
last_updated: May 21, 2023
category: Transformation
section_path: OSDCloud v1 > Transformations > Workspace Architecture
doc_type: architecture_reference
---

# OSDCloud Workspace Architecture and Transformations

## Overview

An **OSDCloud Workspace** is a structured directory derived from an OSDCloud 
Template that contains all components necessary to create bootable media (ISO, USB) 
for Windows deployment.
This document explains the complete directory architecture, 
transformation process from template to workspace, and how content is organized for 
both ISO-bootable and USB-only scenarios.
## Complete Workspace Directory Structure

??? Media\ # ISO-bootable partition (FAT32-compatible) ? ??? sources ? ? ???
boot.wim # Modified WinPE image (Edit-OSDCloudWinPE applied) ? ? ? ??? EFI\ # UEFI 
boot files ? ? ???
Boot ? ? ? ??? bootx64.efi # UEFI boot loader (x64) ? ? ??? Microsoft ? 
? ??? Boot ?
? ??? BCD # Boot Configuration Database (UEFI) ? ? ??? BCD.LOG ? ? ?
??
boot.sdi # RAM disk boot file ? ? ??? bootmgfw\.efi # Boot manager firmware ? ? ?
??
bootmgr.efi # Boot manager (UEFI) ? ? ??? memtest.efi # Memory diagnostic tool ? ? 
???
Fonts\ # Boot fonts ? ? ? ??? Boot\ # BIOS boot files ? ? ???
BCD # Boot 
Configuration Database (BIOS) ? ? ??? BCD.LOG ? ? ??? boot.sdi # RAM disk boot file 
?
? ??? bootfix.bin # Boot sector fix ? ? ??? bootsect.exe # Boot sector tool ? ? ???
etfsboot.com # El Torito boot image ? ? ??? memtest.exe # Memory diagnostic ? ? ???
Fonts\ # Boot fonts ? ? ? ??? bootmgr # Boot manager executable (BIOS) ? ???
bootmgr.efi # Boot manager executable (UEFI) ? ? ? ??? OSDCloud\ # OSDCloud 
runtime content ? ???
OS\ # Operating system images ? ? ??? Windows 11 22H2 
x64.wim ? ? ??? Windows 10 22H2 x64.wim ?
? ??? \[Additional OS WIM files] ? ? ? ??? 
DriverPacks\ # Manufacturer driver packs ? ? ??? Dell ?
? ? ??? Latitude\_5420.cab ? ? 
? ??? \[Additional Dell driver packs] ? ? ??? HP ? ? ? ???
EliteBook\_840\_G8.cab ? ? ? 
??? \[Additional HP driver packs] ? ? ??? Lenovo ? ? ? ??? ThinkPad\_T14\_Gen2.exe ? 
?
? ??? \[Additional Lenovo driver packs] ? ? ??? Microsoft ? ? ??? Surface\_Pro\_8.msi 
? ? ???
\[Additional Surface driver packs] ? ? ? ??? Automate\ # Autopilot and 
provisioning content ? ? ??? AutopilotConfigurationFile.json ? ?
??? 
CompanyBranding.ppkg ? ? ??? \[Additional provisioning packages] ? ? ? ??? Config\ # 
OSDCloud configuration files ? ? ???
Start-OSDCloudGUI.json ? ? ??? Start-
OSDCloudGUI-Auto.ps1 ? ? ??? \[Custom configuration scripts] ? ? ? ???
PowerShell\ # 
Custom PowerShell scripts ? ??? Initialize-Deployment.ps1 ? ??? \[Additional custom 
scripts] ? ???
ODTfiles\ # Office Deployment Tool content (non-Media) ? ??? 
Office365ProPlus ? ? ??? configuration.xml ? ??? setup.exe ? ???
Scripts\ # Additional 
deployment scripts (non-Media) ? ??? \[Custom scripts] ? ??? Logs\ # Build and 
deployment logs ? ???
workspace\_creation.log ? ??? .iso # Generated bootable ISO file 

## Template to Workspace Derivation Process

### Step 1: Template Retrieval

```powershell
# OSDCloud retrieves template location
$TemplatePath = Get-OSDCloudTemplate

# Default template locations:
# - C:\ProgramData\OSDCloud\Templates\Default
# - Custom path specified during template creation
What Exists in Template:
*	Base WinPE boot.wim from Windows ADK
*	Standard EFI and Boot directory structures
*	Boot manager files (bootmgr, bootmgr.efi)
*	No modifications applied yet (vanilla ADK content)
Step 2: Workspace Directory Creation
# Create workspace from template
New-OSDCloudWorkspace -WorkspacePath "C:\OSDCloud\Workspace-Production"

# This performs:
# 1. Copy template directory structure to workspace path
# 2. Create Media\ subdirectory for ISO-bootable content
# 3. Initialize OSDCloud\ runtime directories
# 4. Prepare boot.wim for modification
Directory Creation Sequence:
1.	<WorkspacePath>\ (root)
2.	<WorkspacePath>\Media\ 
(ISO content)
3.	<WorkspacePath>\Media\sources\
4.	<WorkspacePath>\Media\EFI\ (copied from template)
5.	<WorkspacePath>\Media\Boot\ (copied from template)
6.	<WorkspacePath>\Media\OSDCloud\ (created empty)
7.	<WorkspacePath>\Media\OSDCloud\OS\ (created empty)
8.	<WorkspacePath>\Media\OSDCloud\DriverPacks\ (created empty)
9.	<WorkspacePath>\Media\OSDCloud\Automate\ (created empty)
10.	<WorkspacePath>\Media\OSDCloud\Config\ (created empty)
Step 3: boot.wim Extraction and Modification
# Extract boot.wim from ADK
$ADKPath = "C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment 
Kit\Windows Preinstallation Environment\amd64\en-us\winpe.wim"
Copy-Item -Path $ADKPath -Destination "$WorkspacePath\Media\sources\boot.wim"

# Apply Edit-OSDCloudWinPE transformations
Edit-OSDCloudWinPE -WorkspacePath $WorkspacePath

# This modifies boot.wim with:
# - Startup flow changes (winpeshl.ini, startnet.cmd)
# - PowerShell configuration
# - Network and Wi-Fi enablement
# - Driver injection
# - Registry modifications
# - OSD module integration
# - Branding and logging
Transformations Applied: See T02_Edit-
OSDCloudWinPE_Complete_Transformation_Reference.md for complete details.
Step 4: EFI and Boot File Population
EFI Directory (UEFI Boot):
Source: Windows ADK media files + OSDCloud modifications
Destination: <WorkspacePath>\Media\EFI\

Files copied:
- EFI\Boot\bootx64.efi (UEFI boot loader)
- EFI\Microsoft\Boot\bootmgfw.efi (boot manager firmware)
- EFI\Microsoft\Boot\bootmgr.efi (boot manager)
- EFI\Microsoft\Boot\BCD (Boot Configuration Database for UEFI)
- EFI\Microsoft\Boot\boot.sdi (RAM disk image)
- EFI\Microsoft\Boot\memtest.efi (memory diagnostic)
- EFI\Microsoft\Boot\Fonts\ (TrueType fonts for boot UI)
BCD Configuration (UEFI):
Device: ramdisk=[boot]\sources\boot.wim,{ramdiskoptions}
Path: \Windows\System32\boot\winload.efi
Locale: en-US
OSDevice: ramdisk=[boot]\sources\boot.wim,{ramdiskoptions}
SystemRoot: \Windows
Boot Directory (BIOS Boot):
Source: Windows ADK media files
Destination: <WorkspacePath>\Media\Boot\

Files copied:
- Boot\BCD (Boot Configuration Database for BIOS)
- Boot\boot.sdi (RAM disk image)
- Boot\bootfix.bin (boot sector repair)
- Boot\bootsect.exe (boot sector management tool)
- Boot\etfsboot.com (El Torito bootable CD image)
- Boot\memtest.exe (memory diagnostic)
- Boot\Fonts\ (bitmap fonts for BIOS boot)
BCD Configuration 
(BIOS):
Device: ramdisk=[boot]\sources\boot.wim,{ramdiskoptions}
Path: \Windows\System32\boot\winload.exe
Locale: en-US
OSDevice: ramdisk=[boot]\sources\boot.wim,{ramdiskoptions}
SystemRoot: \Windows
Root Boot Managers:
<WorkspacePath>\Media\bootmgr (BIOS boot manager - 512 KB)
<WorkspacePath>\Media\bootmgr.efi (UEFI boot manager - 1.2 MB)
Step 5: OSDCloud Runtime Directory Initialization
Purpose: Staging locations for deployment content that OSDCloud cmdlets reference 
during execution.
Directory: Media\OSDCloud\OS\
*	Purpose: Store Windows operating system image files (.wim)
*	Content: OS images downloaded or staged by user
*	Example: 
*	Windows 11 22H2 x64 Enterprise.wim (4.8 GB)
*	Windows 10 22H2 x64 Pro.wim (4.2 GB)
*	ISO Limitation: Files >4GB cannot fit on FAT32 ISO media
*	USB Workaround: Use NTFS USB media for large images
Directory: Media\OSDCloud\DriverPacks\
*	Purpose: Store manufacturer-specific driver packs
*	Supported Formats: 
o	Dell: .cab, .exe
o	HP: .exe
o	Lenovo: .exe
o	Microsoft Surface: .msi
*	Auto-Detection: OSDCloud detects hardware and applies appropriate pack
*	Example: 
*	Dell\Latitude_7420_Win11_A12.cab (850 MB)
*	HP\EliteBook_840_G8_Win11_sp142567.exe (1.2 GB)
Directory: Media\OSDCloud\Automate\
*	Purpose: Store Autopilot profiles and provisioning packages
*	Content: 
o	AutopilotConfigurationFile.json - Autopilot profile exported from Intune
o	*.ppkg - Windows Configuration Designer provisioning packages
*	Example: 
*	AutopilotConfigurationFile.json (2 KB)
*	CompanyBranding.ppkg (15 MB)
*	DefaultApps.ppkg (8 MB)
*	Application Timing: JSON 
applied during OOBE, PPKG applied post-OS 
deployment
Directory: Media\OSDCloud\Config\
*	Purpose: Store OSDCloud GUI and automation configuration
*	Primary File: Start-OSDCloudGUI.json
*	Structure: 
*	{
*	  "AutoStart": true,
*	  "ImageIndex": 6,
*	  "ScreenshotCapture": true,
*	  "Restart": true,
*	  "Manufacturer": "Dell",
*	  "Product": "Latitude",
*	  "OSName": "Windows 11 22H2 x64",
*	  "OSEdition": "Enterprise",
*	  "OSLanguage": "en-us",
*	  "OSLicense": "Volume"
*	}
*	Purpose: Pre-configure GUI selections for zero-touch deployment
Directory: Media\OSDCloud\PowerShell\
*	Purpose: Custom PowerShell scripts for deployment customization
*	Use Cases: 
o	Hardware-specific configurations
o	Post-deployment tasks
o	Custom branding
o	Application installation
Step 6: Non-Media Content (USB-Only)
Directory: <WorkspacePath>\ODTfiles\
*	Purpose: Office Deployment Tool files
*	Why Non-Media: Large size (>1GB Office source files)
*	Content: 
o	setup.exe (Office installer)
o	configuration.xml (Office configuration)
o	Office 365 source files
*	Access: Only available on USB media (not ISO)
Directory: 
<WorkspacePath>\Scripts\
*	Purpose: Additional deployment scripts not needed in WinPE
*	Content: Post-deployment automation, reporting scripts
*	Access: Only available on USB media
Media vs Non-Media Partition Strategy
ISO-Bootable Media Partition (Media\)
File System: FAT32 (UEFI firmware requirement)
Size Limit: 4 GB (FAT32 maximum file size)
Contents:
*	boot.wim (typically 400-600 MB after modifications)
*	EFI boot files (~50 MB)
*	Boot manager files (~2 MB)
*	OSDCloud\OS\ - Only if OS images <4GB each
*	OSDCloud\DriverPacks\ - Only if total <4GB
*	OSDCloud\Automate\ - Small files (typically <100 MB)
*	OSDCloud\Config\ - Small files (<1 MB)
Bootability:
*	?
ISO media (CD/DVD)
*	? USB flash drive (formatted FAT32)
*	? Network boot (PXE/iPXE with ISO extraction)
Limitations:
*	Cannot store OS images >4GB (e.g., Windows 11 with Office)
*	Cannot store large DriverPack collections
*	Cannot store Office Deployment Tool content
Non-Media Partition (Workspace Root)
File System: NTFS (when on USB) or host file system
Size Limit: No practical limit (NTFS supports files up to 16 TB)
Contents:
*	ODTfiles\ (Office Deployment Tool)
*	Scripts\ (post-deployment automation)
*	Large OS images (>4GB)
*	Complete DriverPack libraries
Bootability:
*	?
ISO media (not included in ISO)
*	? USB flash drive (accessible after WinPE boot via drive letter)
*	?
Network boot (not accessible)
Access Method:
# In WinPE, after booting from USB
$USBDrive = Get-Volume | Where-Object {$_.FileSystemLabel -eq "OSDCloud"} |
Select-
Object -ExpandProperty DriveLetter
$ODTPath = "$($USBDrive):\ODTfiles"
Hybrid USB Strategy (Recommended)
USB Partition Layout:
USB Flash Drive (32 GB+)
???
Partition 1: FAT32 (8 GB) - Bootable
?   ??? [Contents of Media\ directory]
?       ??? sources\boot.wim
?       ??? EFI\
?       ??? Boot\
?       ???
bootmgr, bootmgr.efi
?       ??? OSDCloud\
?           ??? Automate\
?           ??? Config\
?
??? Partition 2: NTFS (24 GB) - Data
    ???
OS\
    ?   ??? [Large OS images >4GB]
    ??? DriverPacks\
    ?   ???
[Complete driver library]
    ??? ODTfiles\
        ???
[Office deployment content]
Creation Process:
# Format USB with dual partitions
$USBDisk = Get-Disk |
Where-Object {$_.BusType -eq 'USB'}
Clear-Disk -Number $USBDisk.Number -RemoveData -Confirm:$false

# Create FAT32 boot partition (8 GB)
New-Partition -DiskNumber $USBDisk.Number -Size 8GB -IsActive |
Format-Volume -FileSystem FAT32 -NewFileSystemLabel "OSDCloudBoot"

# Create NTFS data partition (remaining space)
New-Partition -DiskNumber $USBDisk.Number -UseMaximumSize |
Format-Volume -FileSystem NTFS -NewFileSystemLabel "OSDCloudData"

# Copy Media\ to FAT32 partition
Copy-Item -Path "C:\OSDCloud\Workspace-Production\Media\*" -Destination "E:\" -
Recurse

# Copy large files to NTFS partition
Copy-Item -Path "C:\OSDCloud\Workspace-Production\ODTfiles" -Destination "F:\" -
Recurse
Copy-Item -Path "C:\OSDCloud\LargeOSImages\*.wim" -Destination "F:\OS\" -Recurse
Transformation Summary: Template ?
Workspace
Component
Template State
Workspace State
Transformation Applied
boot.wim
Vanilla ADK 
WinPE
OSDCloud-modified 
WinPE
Edit-OSDCloudWinPE 
(15+ modifications)
EFI\ directory
Standard ADK 
files
Copied unchanged
Direct copy
Boot\ 
directory
Standard ADK 
files
Copied unchanged
Direct copy
bootmgr files
Standard ADK 
files
Copied unchanged
Direct copy
BCD files
Default boot 
configuration
OSDCloud boot 
configuration
Modified to point to 
sources\boot.wim
*OSDCloud*
Does not exist
Created with 
subdirectories
New directory structure
OS images
Does not exist
User-staged
Manual copy or download
DriverPacks
Does not exist
User-staged
Manual copy or download
Automate 
content
Does not exist
User-staged
Manual copy
Config files
Does not exist
Created (Start-
OSDCloudGUI.json)
Generated by user or 
script
Content Staging Workflow
1. Stage OS Images
# Download OS from Microsoft servers
Get-OSDCloudOS -Name "Windows 11 22H2 x64" -Edition Enterprise -Language en-us

# Staged to: <WorkspacePath>\Media\OSDCloud\OS\
# File: Windows 11 22H2 x64 Enterprise en-us.wim
2. Stage DriverPacks
# Download manufacturer driver packs
Get-OSDCloudDriverPack -Manufacturer Dell -Product 
"Latitude 7420"

# Staged to: <WorkspacePath>\Media\OSDCloud\DriverPacks\Dell\
# File: Latitude_7420_Win11_A12.cab
3. Stage Autopilot Profile
# Export from Intune and copy
Copy-Item -Path "C:\Autopilot\AutopilotConfigurationFile.json" `
          -Destination "<WorkspacePath>\Media\OSDCloud\Automate\"
4. Stage Provisioning Packages
# Created with Windows Configuration Designer
Copy-Item -Path "C:\PPKG\CompanyBranding.ppkg" `
          -Destination "<WorkspacePath>\Media\OSDCloud\Automate\"
5. Configure GUI Defaults
# Create Start-OSDCloudGUI.json
$Config = @{
    AutoStart = $true
    OSName = "Windows 11 22H2 x64"
    OSEdition = "Enterprise"
    OSLanguage = "en-us"
    Restart = $true
} |
ConvertTo-Json

$Config | Out-File -FilePath "<WorkspacePath>\Media\OSDCloud\Config\Start-
OSDCloudGUI.json"
ISO Generation Process
# Generate bootable ISO from workspace
New-OSDCloudISO -WorkspacePath "C:\OSDCloud\Workspace-Production"

# This process:
# 1. Validates Media\ directory structure
# 2. Creates El Torito boot catalog
# 3. Generates ISO with dual BIOS/UEFI boot support
# 4. Output: <WorkspacePath>\<WorkspaceName>.iso
ISO Characteristics:
*	Format: ISO 9660 with El Torito boot specification
*	Boot Support: BIOS (legacy) and UEFI (x64)
*	File System: FAT32 (for UEFI compatibility)
*	Size: Typically 500 MB - 4 GB (depending on staged content)
*	Bootable: CD, DVD, USB (via Rufus/other tools), virtual machine
Key Differences: Workspace vs Template
Aspect
Template
Workspace
Purpose
Reusable base for multiple 
workspaces
Single-use deployment 
environment
boot.wim
Unmodified ADK WinPE
Modified with Edit-
OSDCloudWinPE
OSDCloud\ 
directory
Does not exist
Fully populated with staged 
content
Bootable
No
Yes (after ISO generation or 
USB 
creation)
Customization
Generic
Specific to deployment scenario
Modification 
frequency
Rarely (ADK updates)
Frequently (OS updates, driver 
updates)
Implementation Notes for MDT Replication
MDT Equivalent of OSDCloud Workspace:
*	MDT Deployment Share = OSDCloud Workspace
*	*DeploymentShare\Boot* = Media\ directory
*	*DeploymentShare\Operating Systems* = OSDCloud\OS\
*	*DeploymentShare\Out-of-Box Drivers* = OSDCloud\DriverPacks\
*	*DeploymentShare\Applications* = OSDCloud\Automate\ (for PPKG)
*	DeploymentShare\Control\CustomSettings.ini = OSDCloud\Config\Start-
OSDCloudGUI.json
Key MDT Differences:
1.	MDT uses task sequences instead of PowerShell cmdlets
2.	MDT auto-generates boot.wim during "Update Deployment Share"
3.	MDT stores configuration in .ini files, not .json
4.	MDT uses VBScript/HTA for GUI, OSDCloud uses PowerShell/WPF
See T04_MDT_Implementation_Mapping_for_OSDCloud_Transformations.md for 
complete MDT replication guide.