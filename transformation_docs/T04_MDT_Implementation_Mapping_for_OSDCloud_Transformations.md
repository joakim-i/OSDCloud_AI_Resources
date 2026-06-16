```markdown
---
title: MDT Implementation Mapping for OSDCloud Transformations
source_url: https://www.osdcloud.com/osdcloud-v1
version: OSD 23.5.21.1+
last_updated: May 21, 2023
category: Transformation
section_path: OSDCloud v1 > Transformations > MDT Implementation
doc_type: implementation_guide
---

# MDT Implementation Mapping for OSDCloud Transformations

## Overview

This document provides complete, step-by-step mappings from every OSDCloud 
transformation to equivalent Microsoft Deployment Toolkit (MDT) and Windows ADK 
implementations.
Each section includes PowerShell code, configuration files, and 
detailed instructions for replicating OSDCloud behavior without using OSDCloud itself.
---

## Complete Transformation Mapping Table

| # | OSDCloud Transformation | MDT/ADK Equivalent Action | Implementation Method |
|---|------------------------|--------------------------|----------------------|
|
1 | Copy template to workspace | Create MDT Deployment Share | `New-Item` + 
`New-PSDrive -PSProvider MDTProvider` |
|
2 | Extract boot.wim from ADK | MDT auto-generates during Update | Run "Update 
Deployment Share" ? generates LiteTouchPE_x64.wim |
| 3 | Modify startnet.cmd | Edit in mounted WIM or Extra Files |
**Option A:** Mount WIM, 
edit, commit<br>**Option B:** Place in `Extra Files\Windows\System32\` |
| 4 | Inject PowerShell profile |
Extra Files directory | Create `Profile.ps1` in `Extra 
Files\Windows\System32\WindowsPowerShell\v1.0\` |
| 5 | Set ExecutionPolicy registry |
Unattend.xml or offline registry | **Option A:** `<OfflineServicing>` pass in unattend.xml<br>**Option B:** `reg load` ? `reg add` ?
`reg unload` |
| 6 | Initialize network in startnet | Add wpeutil InitializeNetwork |
Edit startnet.cmd to 
include `wpeutil InitializeNetwork` |
| 7 | Inject Wi-Fi drivers | Add to Out-of-Box Drivers\WinPE |
Copy drivers to `Out-of-Box 
Drivers\WinPE x64\WiFi\` ? Update share |
| 8 | Enable Wi-Fi service (wlansvc) |
Registry modification | Offline registry: 
`HKLM\SYSTEM\...\Services\WlanSvc` ? `Start` = `2` |
| 9 | Create Wi-Fi profiles |
Extra Files + netsh command | Place XML in `Extra 
Files\Windows\WiFiProfiles\` ? Add netsh to startnet.cmd |
| 10 |
Inject network drivers | Add to Out-of-Box Drivers\WinPE | Same as Wi-Fi drivers 
process, `...\Network\` subfolder |
| 11 |
Inject NVMe/storage drivers | Add to Out-of-Box Drivers\WinPE | Same process, 
`...\Storage\` subfolder |
| 12 |
Copy OSD module | Extra Files directory | `Save-Module -Name OSD` ? Copy to 
`Extra Files\Program Files\WindowsPowerShell\Modules\OSD\` |
|
13 | Auto-import OSD module | PowerShell profile script | Add `Import-Module OSD -
Force` to Profile.ps1 |
| 14 |
Create OSDCloud directory structure | Manual directory creation + Extra Files | 
Create `Media\OSDCloud\` structure ? Populate with OS/drivers/config |
| 15 | Stage OS images (.wim) | Operating Systems node in MDT | Import OS via MDT 
Workbench ?
stored in `Operating Systems\` folder |
| 16 | Stage DriverPacks | Out-of-Box Drivers node |
Import drivers via MDT Workbench ? 
organized by manufacturer/model |
| 17 | Stage Automate content (Autopilot JSON) |
Extra Files or MDT Scripts | Place in 
`Extra Files\OSDCloud\Automate\` OR reference in task sequence |
| 18 |
Stage Provisioning Packages (PPKG) | Extra Files | Place in `Extra 
Files\OSDCloud\Automate\` ? Apply via DISM in TS |
|
19 | Create Start-OSDCloudGUI.json config | CustomSettings.ini | Translate JSON 
settings to `CustomSettings.ini` properties |
| 20 |
Configure autostart behavior | Bootstrap.ini settings | Set 
`SkipBDDWelcome=YES` in `Bootstrap.ini` |
| 21 | Replace wallpaper (winpe.jpg) |
Extra Files | Copy custom `winpe.jpg` to `Extra 
Files\Windows\System32\` |
| 22 | Customize PowerShell console branding |
PowerShell profile | Add banner/colors 
to `Profile.ps1` |
| 23 | Initialize logging | MDT automatic + custom script |
MDT logs to 
`X:\MININT\SMSOSD\OSDLOGS\` automatically |
| 24 | Create bootable ISO | MDT Update Deployment Share |
Run Update ? Select 
"Completely regenerate boot images" + ISO options |
| 25 |
UEFI + BIOS dual boot support | MDT automatic | MDT generates both BIOS and 
UEFI boot files automatically |
---

## Phase 1: Create MDT Deployment Share

### Step 1.1: Install MDT Prerequisites

```powershell
# Install Windows ADK
# Download from: https://go.microsoft.com/fwlink/?linkid=2243390
# Install components: Deployment Tools, Windows Preinstallation Environment

# Install MDT
# Download from: https://www.microsoft.com/en-us/download/details.aspx?id=54259
# Run MicrosoftDeploymentToolkit_x64.msi

# Verify installation
Get-Module -ListAvailable MicrosoftDeploymentToolkit
Step 1.2: Create Deployment Share
# Import MDT PowerShell module
Import-Module "C:\Program Files\Microsoft Deployment 
Toolkit\bin\MicrosoftDeploymentToolkit.psd1"

# Create deployment share directory
$DeploymentSharePath = "C:\DeploymentShare"
New-Item -Path $DeploymentSharePath -ItemType Directory -Force

# Create MDT deployment share
$ShareName = "DeploymentShare$"
New-SmbShare -Name $ShareName -Path $DeploymentSharePath -FullAccess 
"Everyone"

# Create MDT PSDrive
New-PSDrive -Name "DS001" -PSProvider MDTProvider -Root $DeploymentSharePath -
Description "OSDCloud-Style Deployment Share" |
Add-MDTPersistentDrive
Result:
*	MDT deployment share created at C:\DeploymentShare
*	Network share \\<ComputerName>\DeploymentShare$ available
*	MDT PowerShell drive DS001: mounted
 
Phase 2: Configure Extra Files Directory Structure
Step 2.1: Create Extra Files Hierarchy
# Base Extra Files directory
$ExtraFiles = "$DeploymentSharePath\Extra Files"

# Create directory structure matching OSDCloud
$Directories = @(
    "$ExtraFiles\Windows\System32"
    "$ExtraFiles\Windows\System32\WindowsPowerShell\v1.0"
    "$ExtraFiles\Program Files\WindowsPowerShell\Modules\OSD"
    "$ExtraFiles\OSDCloud\Automate"
    "$ExtraFiles\OSDCloud\Config"
    "$ExtraFiles\Windows\WiFiProfiles"
)

foreach ($Dir in $Directories) {
    New-Item -Path $Dir -ItemType Directory -Force
    Write-Host "Created: $Dir" -ForegroundColor Green
}
Purpose of Each Directory:
Path
Purpose
OSDCloud Equivalent
Extra Files\Windows\System32\
Startup 
scripts 
(startnet.cmd
), wallpaper 
(winpe.jpg)
\Windows\System32\ in boot.wim
Extra 
Files\Windows\System32\WindowsP
owerShell\v1.0\
PowerShell 
profile 
(Profile.ps1)
\Windows\System32\WindowsPo
werShell\v1.0\
Extra Files\Program 
Files\WindowsPowerShell\Modules\
OSD\
OSD 
PowerShell 
module
\Program 
Files\WindowsPowerShell\Modul
es\OSD\
Extra Files\OSDCloud\Automate\
Autopilot 
JSON, 
provisioning 
packages
X:\OSDCloud\Automate\
Extra Files\OSDCloud\Config\
Start-
OSDCloudG
UI.json 
equivalents
X:\OSDCloud\Config\
Extra Files\Windows\WiFiProfiles\
Wi-Fi profile 
XMLs
X:\Windows\WiFiProfiles\
 
Phase 3: Create and Configure startnet.cmd
Step 3.1: Create OSDCloud-Equivalent startnet.cmd
# Create startnet.cmd with OSDCloud features
$StartNetContent = @'
@echo off
echo ============================================
echo MDT OSDCloud-Style Deployment Environment
echo ============================================
echo.
REM Initialize WinPE
echo [1/8] Initializing WinPE...
wpeinit

REM Initialize network stack
echo [2/8] Initializing network stack...
wpeutil InitializeNetwork

REM Wait for network stabilization (10 seconds)
echo [3/8] Waiting for network stabilization...
ping 127.0.0.1 -n 11 > nul

REM Display network configuration
echo [4/8] Network configuration:
ipconfig /all

REM Set PowerShell execution policy
echo [5/8] Configuring PowerShell execution policy...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy 
Bypass -Scope Process -Force"

REM Load offline registry and set permanent execution policy
echo [6/8] Setting permanent execution policy...
reg load HKLM\TempSoftware X:\Windows\System32\config\SOFTWARE
reg add "HKLM\TempSoftware\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell" 
/v ExecutionPolicy /t REG_SZ /d Bypass /f
reg unload HKLM\TempSoftware

REM Import OSD module (if present)
echo [7/8] Loading OSD PowerShell module...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Import-Module OSD -
Force -ErrorAction 
SilentlyContinue"

REM Check for OSDCloud-style autostart scripts
if exist X:\OSDCloud\Config\Start-OSDCloudGUI-Auto.ps1 (
    echo [8/8] Auto-starting OSDCloud GUI...
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File X:\OSDCloud\Config\Start-
OSDCloudGUI-Auto.ps1
    goto :END
)

if exist X:\OSDCloud\Config\Start-OSDCloud-Auto.ps1 (
    echo [8/8] Auto-starting OSDCloud CLI...
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File X:\OSDCloud\Config\Start-
OSDCloud-Auto.ps1
    goto :END
)

REM Launch MDT deployment (standard path)
if exist X:\Deploy\Scripts\LiteTouch.wsf (
    echo [8/8] Launching MDT deployment...
    wscript.exe X:\Deploy\Scripts\LiteTouch.wsf
    goto :END
)

REM Fallback to PowerShell console
echo [8/8] Starting PowerShell console...
echo.
echo Type 'Start-OSDCloudGUI' to launch OSDCloud deployment (if OSD module is 
loaded)
echo Type 'wscript X:\Deploy\Scripts\LiteTouch.wsf' to launch MDT deployment
echo.
powershell.exe -NoExit -ExecutionPolicy Bypass

:END
'@

# Write to Extra Files
$StartNetPath = "$ExtraFiles\Windows\System32\startnet.cmd"
$StartNetContent |
Out-File -FilePath $StartNetPath -Encoding ASCII -Force
Write-Host "Created: $StartNetPath" -ForegroundColor Green
Key Features:
*	? Automatic network initialization
*	? 10-second network stabilization wait
*	?
PowerShell execution policy configured
*	? OSD module auto-import
*	? Support for OSDCloud-style autostart scripts
*	?
Falls back to MDT deployment or PowerShell console
 
Phase 4: Create PowerShell Profile
Step 4.1: Create OSDCloud-Style Profile.ps1
$ProfileContent = @'
# MDT OSDCloud-Style PowerShell Profile
# Automatically loaded when PowerShell starts in WinPE

# Configure console appearance
$Host.UI.RawUI.WindowTitle = "MDT OSDCloud-Style Deployment Environment"
$Host.UI.RawUI.BackgroundColor = "Black"
$Host.UI.RawUI.ForegroundColor = "Cyan"
Clear-Host

# Set execution policy
Set-ExecutionPolicy Bypass -Scope Process -Force -ErrorAction SilentlyContinue

# Set working directory
Set-Location X:\

# Import OSD module if available
$OSDModulePath = "X:\Program Files\WindowsPowerShell\Modules\OSD"
if (Test-Path $OSDModulePath) {
    Write-Host "Loading OSD module..." -ForegroundColor Yellow
    try {
        Import-Module OSD -Force -Global -ErrorAction Stop
        
Write-Host "OSD module loaded successfully." -ForegroundColor Green
    } catch {
        Write-Host "Failed to load OSD module: $_" -ForegroundColor Red
    }
}

# Display banner
Write-Host @"

  ????   ??????????? ?????????    ??????? ??????????????? ???      
??????? ???   ???
  ????? ??????????????????????    
???????????????????????????     ????????????? ????
  ??????????????  ???   ???       ???  ?????????  ???????????     ???   
??? ??????? 
  
??????????????  ???   ???       ???  ?????????  ??????? ???     ???   
???  ?????  
  ??? ??? ???????????   ???       ???????????????????     
?????????????????   ???   
  ???     ??????????    ???       ??????? ???????????     ???????? 
???????    ???   
              
                                                                        
  OSDCloud-Style Deployment Environment (MDT Backend)
  https://github.com/OSDeploy/OSD

"@ -ForegroundColor Cyan

Write-Host "Available Commands:" -ForegroundColor Yellow
Write-Host "  Start-OSDCloudGUI           
  - Launch OSDCloud graphical deployment (if 
OSD module loaded)" -ForegroundColor White
Write-Host "  Start-OSDCloud                - Launch OSDCloud command-line deployment (if 
OSD module loaded)" -ForegroundColor White
Write-Host "  wscript X:\Deploy\Scripts\LiteTouch.wsf - Launch MDT deployment" -
ForegroundColor White
Write-Host ""

# Display network status
Write-Host "Network Status:" -ForegroundColor Yellow
$NetAdapters = Get-NetIPAddress -AddressFamily IPv4 -PrefixOrigin Dhcp -ErrorAction 
SilentlyContinue
if ($NetAdapters) {
    $NetAdapters |
Select-Object InterfaceAlias, IPAddress, PrefixLength | Format-Table -
AutoSize
} else {
    Write-Host "  No DHCP-assigned IPv4 addresses found. Run 'wpeutil 
InitializeNetwork' if needed."
-ForegroundColor Red
}

Write-Host "Ready for deployment.`n" -ForegroundColor Green
'@

$ProfilePath = "$ExtraFiles\Windows\System32\WindowsPowerShell\v1.0\Profile.ps1"
$ProfileContent |
Out-File -FilePath $ProfilePath -Encoding UTF8 -Force
Write-Host "Created: $ProfilePath" -ForegroundColor Green
 
Phase 5: Add Wi-Fi Support
Step 5.1: Copy Wi-Fi Drivers to Deployment Share
# Assumes Wi-Fi drivers are staged in C:\Drivers\WiFi
$WiFiDriverSource = "C:\Drivers\WiFi"
$WiFiDriverDest = "$DeploymentSharePath\Out-of-Box Drivers\WinPE x64\WiFi"

if (Test-Path $WiFiDriverSource) {
    Copy-Item -Path "$WiFiDriverSource\*" -Destination $WiFiDriverDest -Recurse -Force
    Write-Host "Wi-Fi drivers copied to: $WiFiDriverDest" -ForegroundColor Green
} else {
    Write-Host "Wi-Fi driver source not found: $WiFiDriverSource" -ForegroundColor Red
    Write-Host "Please download Wi-Fi drivers from manufacturer websites:" -
ForegroundColor Yellow
    Write-Host "  - Intel: 
https://www.intel.com/content/www/us/en/download/19351/wireless-intel-proset-
wireless-software-and-drivers-for-windows-10.html" -ForegroundColor White
    
Write-Host "  - Realtek: 
https://www.realtek.com/en/component/zoo/category/network-interface-controllers-
10-100-1000m-gigabit-ethernet-pci-express-software" -ForegroundColor White
}
Step 5.2: Create Wi-Fi Profile XML
# Create corporate Wi-Fi profile
$WiFiProfileContent = @'
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>CorporateWiFi</name>
    <SSIDConfig>
        <SSID>
            <name>CorporateWiFi</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
        
        <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
    
            <keyMaterial>YourWiFiPasswordHere</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
'@

$WiFiProfilePath = "$ExtraFiles\Windows\WiFiProfiles\CorporateWiFi.xml"
$WiFiProfileContent |
Out-File -FilePath $WiFiProfilePath -Encoding UTF8 -Force
Write-Host "Created: $WiFiProfilePath" -ForegroundColor Green
Step 5.3: Add Wi-Fi Connection Commands to startnet.cmd
# Append Wi-Fi commands to startnet.cmd
$WiFiCommands = @'

REM Add Wi-Fi profile and connect
if exist X:\Windows\WiFiProfiles\CorporateWiFi.xml (
    echo Adding Wi-Fi profile...
    netsh wlan add profile filename="X:\Windows\WiFiProfiles\CorporateWiFi.xml"
    echo Connecting to Corporate Wi-Fi...
    netsh wlan connect name="CorporateWiFi"
)
'@

Add-Content -Path "$ExtraFiles\Windows\System32\startnet.cmd" -Value 
$WiFiCommands
Write-Host "Wi-Fi commands added to startnet.cmd" -ForegroundColor Green
Step 5.4: Enable WlanSvc via Offline Registry
# This will be applied when MDT builds boot.wim
# Create registry modification script
$RegModScript = @'
@echo off
REM Enable Wi-Fi service (WlanSvc)
reg load HKLM\WIM_SYSTEM 
X:\Windows\System32\config\SYSTEM
reg add "HKLM\WIM_SYSTEM\ControlSet001\Services\WlanSvc" /v Start /t 
REG_DWORD /d 2 /f
reg add "HKLM\WIM_SYSTEM\ControlSet001\Services\WlanSvc" /v DelayedAutoStart /t 
REG_DWORD /d 0 /f
reg unload HKLM\WIM_SYSTEM
'@

$RegModPath = "$ExtraFiles\Windows\System32\Enable-WiFiService.cmd"
$RegModScript |
Out-File -FilePath $RegModPath -Encoding ASCII -Force

# Add to startnet.cmd to run at WinPE startup
$RegModCall = @'

REM Enable Wi-Fi service
call X:\Windows\System32\Enable-WiFiService.cmd
'@
Add-Content -Path "$ExtraFiles\Windows\System32\startnet.cmd" -Value $RegModCall 
-Force
Write-Host "Wi-Fi service enablement script created and integrated" -ForegroundColor 
Green
 
Phase 6: Configure Bootstrap.ini and CustomSettings.ini
Step 6.1: Configure Bootstrap.ini (Auto-Start)
$BootstrapIniPath = "$DeploymentSharePath\Control\Bootstrap.ini"
$BootstrapContent = @"
[Settings]
Priority=Default

[Default]
DeployRoot=\\$env:COMPUTERNAME\DeploymentShare$
SkipBDDWelcome=YES
UserDomain=$env:USERDOMAIN
UserID=MDTUser
UserPassword=P@ssw0rd
"@

$BootstrapContent |
Out-File -FilePath $BootstrapIniPath -Encoding ASCII -Force
Write-Host "Bootstrap.ini configured for auto-start" -ForegroundColor Green
Key Settings:
*	SkipBDDWelcome=YES ?
Skip MDT welcome screen (equivalent to OSDCloud 
autostart)
*	Credentials auto-provided ?
No manual authentication needed
Step 6.2: Configure CustomSettings.ini (Deployment Defaults)
$CustomSettingsPath = "$DeploymentSharePath\Control\CustomSettings.ini"
$CustomSettingsContent = @"
[Settings]
Priority=Default
Properties=MyCustomProperty

[Default]
; OSDCloud-style auto-configuration
OSInstall=Y
SkipCapture=YES
SkipAdminPassword=YES
SkipProductKey=YES
SkipComputerBackup=YES
SkipBitLocker=YES
SkipApplications=NO
SkipPackageDisplay=YES
SkipLocaleSelection=YES
SkipTimeZone=YES
SkipSummary=NO
SkipFinalSummary=NO

; Pre-select OS (equivalent to Start-OSDCloudGUI.json)
TaskSequenceID=WIN11-ENT
SkipTaskSequence=YES

; Driver injection
DriverGroup001=WinPE x64\%Make%\%Model%
DriverGroup002=Windows 11 x64\%Make%\%Model%

; Computer naming
OSDComputerName=%SerialNumber%

; Logging
SLShare=\\$env:COMPUTERNAME\Logs$\%OSDComputerName%
EventService=http://$env:COMPUTERNAME:9800

; Autopilot configuration (if using OSDCloud Automate equivalent)
AutopilotConfigurationFile=AutopilotConfigurationFile.json
"@

$CustomSettingsContent |
Out-File -FilePath $CustomSettingsPath -Encoding ASCII -
Force
Write-Host "CustomSettings.ini configured with OSDCloud-style defaults" -
ForegroundColor Green
OSDCloud JSON ?
MDT CustomSettings.ini Mapping:
OSDCloud JSON Property
MDT CustomSettings.ini Property
"AutoStart": true
SkipTaskSequence=YES + TaskSequenceID=<ID>
"OSName": "Windows 11 22H2 
x64"
TaskSequenceID=WIN11-ENT (task sequence must 
match OS)
"OSEdition": "Enterprise"
Embedded in TaskSequenceID
"OSLanguage": "en-us"
UILanguage=en-US + UserLocale=en-US
"Restart": true
FinishAction=REBOOT
"Manufacturer": "Dell"
%Make% variable (auto-detected)
"Product": "Latitude"
%Model% variable (auto-detected)
 
Phase 7: Copy OSD PowerShell Module (Optional)
Step 7.1: Download OSD Module
# Download OSD module from PowerShell Gallery
Save-Module -Name OSD -Path "$env:TEMP\Modules" -Force
Write-Host "OSD module downloaded to $env:TEMP\Modules" -ForegroundColor Green
Step 7.2: Copy to Extra Files
$OSDModuleSource = "$env:TEMP\Modules\OSD"
$OSDModuleDest = "$ExtraFiles\Program Files\WindowsPowerShell\Modules\OSD"

if (Test-Path $OSDModuleSource) {
    Copy-Item -Path $OSDModuleSource -Destination $OSDModuleDest -Recurse -Force
    Write-Host "OSD module copied to Extra Files" -ForegroundColor Green
    Write-Host 
"Module will be available in WinPE at: X:\Program 
Files\WindowsPowerShell\Modules\OSD" -ForegroundColor Cyan
} else {
    Write-Host "OSD module not found.
Skipping." -ForegroundColor Yellow
}
Purpose:
*	Enables Start-OSDCloudGUI and Start-OSDCloud commands in MDT WinPE
*	Allows using OSDCloud deployment methods within MDT environment
*	Provides hybrid OSDCloud/MDT capability
 
Phase 8: Update Deployment Share and Generate Boot Media
Step 8.1: Update Deployment Share
# Update deployment share to inject Extra Files and drivers
Write-Host "Updating MDT deployment share... This may take several minutes." -
ForegroundColor Yellow

Update-MDTDeploymentShare -Path "DS001:" -Verbose -Force

Write-Host "Deployment share updated successfully." -ForegroundColor Green
What This Does:
1.	Injects all files from Extra Files\ into boot.wim
2.	Injects all drivers from Out-of-Box Drivers\WinPE x64\ into boot.wim
3.	Generates LiteTouchPE_x64.wim in Boot\ directory
4.	Generates LiteTouchPE_x64.iso (if ISO generation enabled)
5.	Applies all customizations (startnet.cmd, Profile.ps1, wallpaper, etc.)
Step 8.2: Generate Bootable ISO (if 
not auto-generated)
# Check if ISO was generated
$ISOPath = "$DeploymentSharePath\Boot\LiteTouchPE_x64.iso"
if (Test-Path $ISOPath) {
    Write-Host "Bootable ISO created: $ISOPath" -ForegroundColor Green
} else {
    Write-Host "ISO not generated.
Check deployment share properties to enable ISO 
generation." -ForegroundColor Yellow
    Write-Host "In MDT Workbench: Right-click deployment share ?
Properties ? Rules 
tab ? Enable 'Generate a Lite Touch bootable ISO image'" -ForegroundColor Cyan
}
 
Phase 9: Test and Validate
Step 9.1: Validate Extra Files Integration
# Mount generated boot.wim to verify Extra Files were injected
$MountPath = "C:\Mount"
New-Item -Path $MountPath -ItemType Directory -Force

Dism /Mount-Wim /WimFile:"$DeploymentSharePath\Boot\LiteTouchPE_x64.wim" /Index:1 /MountDir:$MountPath