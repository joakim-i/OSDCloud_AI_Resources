```markdown
---
title: Edit-OSDCloudWinPE Complete Transformation Reference
source_url: https://www.osdcloud.com/osdcloud-v1/osdcloud/workspace
version: OSD 23.5.21.1+
last_updated: May 21, 2023
category: Transformation
section_path: OSDCloud v1 > Transformations > Edit-OSDCloudWinPE
doc_type: transformation_reference
---

# Edit-OSDCloudWinPE Complete Transformation Reference

## Overview

**Edit-OSDCloudWinPE** is the core function that modifies a vanilla Windows ADK 
WinPE boot.wim into an OSDCloud-ready deployment environment.
This document 
provides exhaustive detail on all 15+ transformation categories, explaining what 
changes occur, where they occur, why they occur, and how to replicate them in 
MDT/ADK without using OSDCloud.
## Transformation Categories

1. Startup Flow Modifications
2. PowerShell Configuration
3. Network Stack Initialization
4. Wi-Fi Enablement
5. Driver Injection
6. Registry Modifications
7. OSD Module Integration
8. Autostart Behavior
9. Branding and Visual Modifications
10. Logging Configuration
11. Execution Policy
12. File System Modifications
13. Service Configuration
14. WinPE Optional Components
15. Cleanup and Optimization

---

## 1. Startup Flow Modifications

### A. winpeshl.ini Modification

**File Path:** `\Windows\System32\winpeshl.ini`

**Standard ADK Content (Before):**
```ini
[LaunchApps]
%SYSTEMDRIVE%\Windows\System32\wpeinit.exe
OSDCloud-Modified Content (After):
[LaunchApps]
%SYSTEMDRIVE%\Windows\System32\wpeinit.exe
%SYSTEMDRIVE%\Windows\System32\startnet.cmd
Purpose:
*	Launch startup script automatically after wpeinit completes
*	Enable automated environment configuration
*	Allow custom commands to run before user interaction
MDT Equivalent:
# Mount boot.wim
Dism /Mount-Wim /WimFile:"C:\DeploymentShare\Boot\LiteTouchPE_x64.wim" 
/Index:1 /MountDir:"C:\Mount"

# Modify winpeshl.ini
$WinPEShell = @"
[LaunchApps]
%SYSTEMDRIVE%\Windows\System32\wpeinit.exe
%SYSTEMDRIVE%\Windows\System32\startnet.cmd
"@
$WinPEShell |
Out-File -FilePath "C:\Mount\Windows\System32\winpeshl.ini" -
Encoding ASCII

# Unmount and commit
Dism /Unmount-Wim /MountDir:"C:\Mount" /Commit
B. startnet.cmd Creation/Modification
File Path: \Windows\System32\startnet.cmd
Standard ADK Content (Before):
wpeinit
OSDCloud-Modified Content (After):
@echo off
echo OSDCloud WinPE Environment Initializing...

REM Initialize WinPE (already called by winpeshl.ini, but ensures completion)
wpeinit

REM Initialize network stack
echo Initializing network stack...
wpeutil InitializeNetwork

REM Wait for network initialization (5 seconds)
ping 127.0.0.1 -n 6 > nul

REM Display network status
ipconfig /all

REM Set PowerShell execution policy
echo Setting PowerShell execution policy...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy 
Bypass -Scope Process -Force"

REM Load offline registry hive and set permanent execution policy
reg load HKLM\TempSoftware X:\Windows\System32\config\SOFTWARE
reg add "HKLM\TempSoftware\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell" 
/v ExecutionPolicy /t REG_SZ /d Bypass /f
reg unload HKLM\TempSoftware

REM Import OSD PowerShell module
echo Loading OSD module...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Import-Module OSD -
Force -ErrorAction SilentlyContinue"

REM Check for autostart configuration
if exist X:\OSDCloud\Config\Start-OSDCloudGUI-Auto.ps1 (
    echo Auto-starting OSDCloud GUI...
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File X:\OSDCloud\Config\Start-
OSDCloudGUI-Auto.ps1
)

if exist X:\OSDCloud\Config\Start-OSDCloud-Auto.ps1 (
    echo Auto-starting OSDCloud CLI...
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File X:\OSDCloud\Config\Start-
OSDCloud-Auto.ps1
)

REM Launch PowerShell console
echo Starting PowerShell...
powershell.exe -NoExit -ExecutionPolicy Bypass
Purpose:
*	Automate network initialization (eliminates manual wpeutil commands)
*	Configure PowerShell environment before user interaction
*	Enable auto-start capabilities for zero-touch deployment
*	Provide immediate PowerShell access instead of cmd.exe
Key Commands Explained:
Command
Purpose
Timing
wpeinit
Hardware detection and driver loading
10-15 
seconds
wpeutil InitializeNetwork
Start networking services (DHCP, DNS)
5-10 
seconds
ping 127.0.0.1 -n 6
Wait 
5 seconds for network 
stabilization
5 seconds
ipconfig /all
Display network configuration for 
troubleshooting
1 second
powershell Set-ExecutionPolicy 
Bypass
Allow unsigned scripts in current 
session
1 second
reg load/add/unload
Set permanent ExecutionPolicy in 
registry
2 seconds
Import-Module OSD
Load OSDCloud cmdlets
3 seconds
powershell.exe -NoExit
Launch interactive PowerShell console
Immediate
MDT Equivalent:
# Create startnet.cmd in Extra Files
$StartNet = @'
@echo off
wpeinit

REM Initialize network
wpeutil InitializeNetwork
ping 127.0.0.1 -n 6 > nul

REM Set PowerShell execution policy
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy 
Bypass -Force"

REM Import OSD module (if using OSD module approach)
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Import-Module OSD -
Force -ErrorAction SilentlyContinue"

REM Launch MDT deployment
wscript.exe X:\Deploy\Scripts\LiteTouch.wsf

REM Fallback to PowerShell
powershell.exe -NoExit -ExecutionPolicy Bypass
'@

$StartNet |
Out-File -FilePath "C:\DeploymentShare\Extra 
Files\Windows\System32\startnet.cmd" -Encoding ASCII
 
2. PowerShell Configuration
A. PowerShell Profile Creation
File Path: \Windows\System32\WindowsPowerShell\v1.0\Profile.ps1
Content:
# OSDCloud PowerShell Profile
# Loaded automatically when PowerShell starts in WinPE

# Configure console appearance
$Host.UI.RawUI.WindowTitle = "OSDCloud WinPE Environment - Version 23.5.21.1"
$Host.UI.RawUI.BackgroundColor = "Black"
$Host.UI.RawUI.ForegroundColor = "Cyan"
Clear-Host

# Set execution policy for current session
Set-ExecutionPolicy Bypass -Scope Process -Force -ErrorAction SilentlyContinue

# Set working directory to X:\ (RAM disk root)
Set-Location X:\

# Import OSD module if available
$OSDModulePath = "X:\Program Files\WindowsPowerShell\Modules\OSD"
if (Test-Path $OSDModulePath) {
    Write-Host "Loading OSD module..." -ForegroundColor Yellow
    Import-Module OSD -Force -PassThru -ErrorAction SilentlyContinue |
Out-Null
    Write-Host "OSD module loaded successfully." -ForegroundColor Green
} else {
    Write-Host "OSD module not found at $OSDModulePath" -ForegroundColor Red
}

# Display OSDCloud banner
Write-Host @"

   ____   _____ _____   _____ _                 _ 
  / __ \ / ____|  __ \ / ____| |               | |
 | |  | | (___ | |  | | |   
 | | ___  _   _  __| |
 | |  | |\___ \| |  | | |    | |/ _ \| | | |/ _` |
 | |__| |____) | |__| | |____| | (_) | |_| | (_| |
  \____/|_____/|_____/ \_____|_|\___/ \__,_|\__,_|
  
  OSDCloud WinPE Deployment Environment
  Version: 23.5.21.1
  https://osdcloud.com
  
  Commands:
    Start-OSDCloudGUI   - Launch graphical deployment interface
    Start-OSDCloud      - Launch command-line deployment
    Get-OSDCloudHelp    
- Display available commands
  
"@ -ForegroundColor Cyan

Write-Host "Network Status:" -ForegroundColor Yellow
Get-NetIPAddress -AddressFamily IPv4 -PrefixOrigin Dhcp -ErrorAction SilentlyContinue 
| 
    Select-Object InterfaceAlias, IPAddress | Format-Table -AutoSize

Write-Host "`nReady for deployment.`n" -ForegroundColor Green
Purpose:
*	Provide consistent, branded PowerShell experience
*	Auto-load OSD module on startup
*	Display helpful command guidance
*	Show network status immediately
*	Set optimal console colors for readability
MDT Equivalent:
# Create Profile.ps1 in Extra Files
$Profile = @'
$Host.UI.RawUI.WindowTitle = "MDT Deployment Environment"
$Host.UI.RawUI.BackgroundColor = "Black"
$Host.UI.RawUI.ForegroundColor = "Cyan"
Clear-Host

Set-ExecutionPolicy Bypass -Scope Process -Force

Set-Location X:\

if (Test-Path "X:\Program Files\WindowsPowerShell\Modules\OSD") {
    Import-Module OSD -Force
}

Write-Host "MDT Deployment Environment" -ForegroundColor Cyan
Write-Host "Commands:" -ForegroundColor Yellow
Write-Host "  wscript X:\Deploy\Scripts\LiteTouch.wsf - Start MDT deployment" 
-
ForegroundColor White
'@

$Profile | Out-File -FilePath "C:\DeploymentShare\Extra 
Files\Windows\System32\WindowsPowerShell\v1.0\Profile.ps1" -Encoding UTF8
B. PowerShell Module Path Configuration
Registry Path: HKLM\SYSTEM\CurrentControlSet\Control\Session 
Manager\Environment
Value Added:
Name: PSModulePath
Type: REG_EXPAND_SZ
Data: %ProgramFiles%\WindowsPowerShell\Modules;X:\Program 
Files\WindowsPowerShell\Modules
Purpose:
*	Ensure PowerShell can locate OSD module in WinPE environment
*	Support both default and custom module locations
MDT Equivalent:
# Apply via offline registry
reg load HKLM\WIM C:\Mount\Windows\System32\config\SYSTEM
reg add "HKLM\WIM\ControlSet001\Control\Session Manager\Environment" /v 
PSModulePath /t REG_EXPAND_SZ /d 
"%ProgramFiles%\WindowsPowerShell\Modules;X:\Program 
Files\WindowsPowerShell\Modules" /f
reg unload HKLM\WIM
 
3. Network Stack Initialization
A. Automatic Network Initialization
Implementation: wpeutil InitializeNetwork in startnet.cmd
What It Does:
1.	Starts DHCP Client service
2.	Starts DNS Client service
3.	Initializes network interfaces
4.	Requests DHCP lease
5.	Configures DNS servers from DHCP
Timing:
*	Standard ADK: Manual (user must run command)
*	OSDCloud: Automatic (runs in startnet.cmd)
*	Speed improvement: ~60 seconds saved
MDT Equivalent:
REM Add to 
startnet.cmd in Extra Files
wpeutil InitializeNetwork
ping 127.0.0.1 -n 10 > nul
B. Network Services Configuration
Services Modified:
Service
Registry Path
Start 
Value
Purpose
DHCP 
Client
HKLM\SYSTEM\CurrentControlSet\Services\Dhcp
2 
(Automatic
)
Obtain IP 
address
DNS 
Client
HKLM\SYSTEM\CurrentControlSet\Services\Dnscach
e
2 
(Automatic
)
Resolve 
DNS 
names
TCP/IP 
NetBIO
S 
Helper
HKLM\SYSTEM\CurrentControlSet\Services\lmhosts
2 
(Automatic
)
NetBIOS 
name 
resolutio
n
MDT Equivalent:
# Apply via offline registry
reg load HKLM\WIM C:\Mount\Windows\System32\config\SYSTEM

reg add "HKLM\WIM\ControlSet001\Services\Dhcp" /v Start /t REG_DWORD /d 2 /f
reg add "HKLM\WIM\ControlSet001\Services\Dnscache" /v Start /t REG_DWORD /d 2 /f
reg add "HKLM\WIM\ControlSet001\Services\lmhosts" /v Start /t REG_DWORD /d 2 /f

reg unload HKLM\WIM
 
4. Wi-Fi Enablement
A. Wi-Fi Driver Injection
Drivers Injected:
Manufacturer
Driver Package
Files
Purpose
Intel
Intel Wireless AC/AX
Netwtw*.sys, 
Netwtw*.inf
Intel Wi-Fi adapters
Realtek
Realtek Wireless LAN
rtwlane*.sys, rtw*.inf
Realtek Wi-Fi 
adapters
Broadcom
Broadcom 802.11
bcmwl*.sys, 
bcmwl*.inf
Broadcom Wi-Fi 
adapters
Qualcomm 
Atheros
Qualcomm Atheros 
Wireless
qcamain*.sys, 
qca*.inf
Qualcomm Wi-Fi 
adapters
Injection Method:
# Mount WIM
Dism /Mount-Wim /WimFile:"boot.wim" /Index:1 
/MountDir:"C:\Mount"

# Inject drivers recursively
Dism /Image:"C:\Mount" /Add-Driver /Driver:"C:\Drivers\WiFi" /Recurse /ForceUnsigned

# Unmount and commit
Dism /Unmount-Wim /MountDir:"C:\Mount" /Commit
Destination in WIM:
*	\Windows\System32\drivers\ (driver binaries)
*	\Windows\System32\DriverStore\FileRepository\ (driver packages)
MDT Equivalent:
# Add Wi-Fi drivers to deployment share
Copy-Item -Path "C:\Drivers\WiFi\*" -Destination "C:\DeploymentShare\Out-of-Box 
Drivers\WinPE x64\WiFi\" -Recurse

# Update deployment share (MDT auto-injects during boot.wim build)
Update-MDTDeploymentShare -Path "DS001:" -Verbose
B. WLAN Service Enablement
Service: WLAN AutoConfig (WlanSvc)
Registry Modifications:
Path: HKLM\SYSTEM\CurrentControlSet\Services\WlanSvc
Value: Start
Type: REG_DWORD
Data: 2 (Automatic)

Path: HKLM\SYSTEM\CurrentControlSet\Services\WlanSvc
Value: DelayedAutoStart
Type: REG_DWORD
Data: 0 (Start immediately, not delayed)
Purpose:
*	Enable Wi-Fi service to start automatically in WinPE
*	Allow Wi-Fi UI to appear during boot
*	Enable netsh wlan commands
MDT Equivalent:
# Offline registry modification
reg load HKLM\WIM C:\Mount\Windows\System32\config\SYSTEM
reg add "HKLM\WIM\ControlSet001\Services\WlanSvc" /v Start /t REG_DWORD /d 2 /f
reg add "HKLM\WIM\ControlSet001\Services\WlanSvc" 
/v DelayedAutoStart /t 
REG_DWORD /d 0 /f
reg unload HKLM\WIM
C. Wi-Fi Profile Creation (Optional)
File Path: \Windows\WiFiProfiles\CorporateWiFi.xml
Content Example:
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>CorporateWiFi</name>
    <SSIDConfig>
        <SSID>
            <hex>436F72706F7261746557694669</hex>
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
                <keyMaterial>YourWiFiPassword</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
Application Command (in startnet.cmd):
netsh wlan add profile filename="X:\Windows\WiFiProfiles\CorporateWiFi.xml"
netsh wlan connect name="CorporateWiFi"
Purpose:
*	Auto-connect to corporate Wi-Fi during WinPE boot
*	Enable zero-touch network connectivity
*	Support deployment in wireless-only environments
MDT Equivalent:
# Create Wi-Fi profile XML in Extra Files
$WiFiXML |
Out-File -FilePath "C:\DeploymentShare\Extra 
Files\Windows\WiFiProfiles\CorporateWiFi.xml" -Encoding UTF8

# Add netsh command to startnet.cmd
Add-Content -Path "C:\DeploymentShare\Extra Files\Windows\System32\startnet.cmd" 
-Value "netsh wlan add profile 
filename=`"X:\Windows\WiFiProfiles\CorporateWiFi.xml`""
Add-Content -Path "C:\DeploymentShare\Extra Files\Windows\System32\startnet.cmd" 
-Value "netsh wlan connect name=CorporateWiFi"
D. Wi-Fi UI Availability
Enablement:
*	Wi-Fi drivers injected ?
Hardware detected
*	WlanSvc set to Automatic ? Service starts
*	WinPE GUI shell running ?
Wi-Fi icon appears in system tray
User Experience:
1.	WinPE boots
2.	Wi-Fi icon appears in system tray (taskbar)
3.	User clicks icon
4.	Windows Wi-Fi connection UI appears
5.	User selects network and enters password
6.	Connection established
OSDCloud Advantage:
*	Fully automatic (no scripting required beyond driver injection + service enable)
MDT Challenge:
*	Wi-Fi UI does not appear automatically even with drivers + service
*	Requires manual PowerShell command: 
*	Start-Process "ms-availablenetworks:"
*	Or custom script to trigger UI
MDT Workaround:
# Add to startnet.cmd or LiteTouch customization
powershell.exe -Command "Start-Process 'ms-availablenetworks:'"
 
5. Driver Injection
A. Network Drivers (Ethernet)
Purpose: Enable wired network connectivity for all hardware
Drivers Injected:
Manufacturer
Driver Family
Files
Intel
I219-V, I225-V, I226-V
e1d*.sys, e1d*.inf, e1r*.sys
Realtek
RTL8111, RTL8125, RTL8168
rt640x64.sys, rt640x64.inf
Broadcom
NetXtreme, NetLink
b57nd60a.sys, b57nd60a.inf
Marvell
Yukon
yk63x64.sys, yk63x64.inf
Injection Command:
Dism /Image:"C:\Mount" /Add-Driver /Driver:"C:\Drivers\Network" /Recurse
MDT Equivalent:
Copy-Item "C:\Drivers\Network" 
"C:\DeploymentShare\Out-of-Box Drivers\WinPE 
x64\Network" -Recurse
Update-MDTDeploymentShare -Path "DS001:"
B. Storage Drivers (NVMe, RAID)
Purpose: Detect modern NVMe SSDs and RAID controllers
Drivers Injected:
Type
Manufacturer
Models
NVMe
Samsung
970 EVO, 980 PRO, 990 PRO
NVMe
Western Digital
SN750, SN850, SN770
NVMe
SK Hynix
P31, P41
NVMe
Intel
660p, 670p
RAID
Intel
RST (Rapid Storage Technology)
RAID
AMD
RAIDXpert
Injection Command:
Dism /Image:"C:\Mount" /Add-Driver /Driver:"C:\Drivers\Storage" /Recurse
C. USB 3.x Drivers
Standard in Modern ADK:
*	Windows ADK 10.0.19041+ includes USB 3.0/3.1/3.2 drivers by default
*	No additional injection needed for most hardware
Legacy Support (if needed):
Dism /Image:"C:\Mount" /Add-Driver /Driver:"C:\Drivers\USB3" /Recurse
 
6. Registry Modifications
Complete Registry Change Reference
Registry Path
Value 
Name
Type
Data
Purp
ose
HKLM\SOFTWARE\Microsoft\Po
werShell\1\ShellIds\Microsoft.Po
werShell
Executio
nPolicy
REG_S
Z
Bypass
Allow 
unsig
ned 
scrip
ts
HKLM\SYSTEM\CurrentControlS
et\Services\WlanSvc
Start
REG_D
WORD
2
Auto-
start 
Wi-Fi 
servi
ce
HKLM\SYSTEM\CurrentControlS
et\Services\WlanSvc
Delayed
AutoStart
REG_D
WORD
0
Start 
imm
ediat
ely
HKLM\SYSTEM\CurrentControlS
et\Services\Dhcp
Start
REG_D
WORD
2
Auto-
start 
DHC
P 
client
HKLM\SYSTEM\CurrentControlS
et\Services\Dnscache
Start
REG_D
WORD
2
Auto-
start 
DNS 
client
HKLM\SYSTEM\CurrentControlS
et\Control\Session 
Manager\Environment
OSDClou
dMode
REG_S
Z
1
Flag 
OSD
Clou
d 
envir
onm
ent
HKLM\SYSTEM\CurrentControlS
et\Control\Session 
Manager\Environment
PSModul
ePath
REG_E
XPAND
_SZ
%ProgramFiles%\Window
sPowerShell\Modules;X:\P
rogram 
Files\WindowsPowerShell
\Modules
Powe
rShel
l 
mod
ule 
path
s
HKLM\SOFTWARE\Microsoft\Wi
ndows\CurrentVersion\Explorer\
Advanced
HideFile
Ext
REG_D
WORD
0
Show 
file 
exten
sions
HKLM\SOFTWARE\Microsoft\Wi
ndows\CurrentVersion\Explorer\
Advanced
Hidden
REG_D
WORD
1
Show 
hidd
en 
files
HKLM\SYSTEM\CurrentControlS
et\Control\TimeZoneInformation
RealTime
IsUnivers
al
REG_D
WORD
1
Use 
UTC 
for 
RTC
HKLM\SOFTWARE\Policies\Micr
osoft\Windows\System
EnableA
ctivityFe
ed
REG_D
WORD
0
Disa
ble 
activi
ty 
feed
HKLM\SOFTWARE\Policies\Micr
osoft\Windows\System
PublishU
serActivit
ies
REG_D
WORD
0
Disa
ble 
user 
activi
ty 
publi
shing
Application 
Method
Offline Registry Editing (during WIM mount):
# Mount WIM
Dism /Mount-Wim /WimFile:"boot.wim" /Index:1 /MountDir:"C:\Mount"

# Load SOFTWARE hive
reg load HKLM\WIM_SOFTWARE C:\Mount\Windows\System32\config\SOFTWARE

# Apply SOFTWARE modifications
reg add 
"HKLM\WIM_SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell" /v 
ExecutionPolicy /t REG_SZ /d Bypass /f
reg add 
"HKLM\WIM_SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v 
HideFileExt /t REG_DWORD /d 0 /f
reg add 
"HKLM\WIM_SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v 
Hidden /t REG_DWORD /d 1 /f

# Unload SOFTWARE hive
reg unload HKLM\WIM_SOFTWARE

# Load SYSTEM hive
reg load HKLM\WIM_SYSTEM C:\Mount\Windows\System32\config\SYSTEM

# Apply SYSTEM modifications
reg add "HKLM\WIM_SYSTEM\ControlSet001\Services\WlanSvc" /v Start /t 
REG_DWORD /d 2 /f
reg add "HKLM\WIM_SYSTEM\ControlSet001\Services\Dhcp" /v Start /t REG_DWORD /d 
2 /f
reg add "HKLM\WIM_SYSTEM\ControlSet001\Control\Session Manager\Environment" /v 
OSDCloudMode /t REG_SZ /d 1 /f

# Unload SYSTEM hive
reg unload HKLM\WIM_SYSTEM

# Unmount and commit
Dism /Unmount-Wim /MountDir:"C:\Mount" 
/Commit
MDT Equivalent:
# Same offline registry process during manual WIM customization
# OR use unattend.xml OfflineServicing pass
# OR create .reg file in Extra Files and apply via startnet.cmd
 
7. OSD Module Integration
A. Module Staging
Source: OSD PowerShell module from PowerShell Gallery
Download:
Save-Module -Name OSD -Path "C:\Temp\Modules"
Destination in WIM: \Program Files\WindowsPowerShell\Modules\OSD\
Module Structure:
\Program Files\WindowsPowerShell\Modules\OSD\
???
OSD.psd1                    # Module manifest
???
OSD.psm1                    # Core module file
???
Functions\                  # Individual cmdlet files
?
??? Start-OSDCloud.ps1
?   ??? Start-OSDCloudGUI.ps1
?   ??? Get-OSDCloudOS.ps1
?   ??? Get-OSDCloudDriverPack.ps1
?   ??? [70+ additional functions]
???
Assemblies\                 # .NET DLLs for GUI
?
??? System.Windows.Forms.dll
?   ??? PresentationFramework.dll
??? Resources\                  # Images, icons
?
??? OSDCloudLogo.png
??? en-US\                     # Help files
    ???
OSD-help.xml
Injection Method:
# Mount WIM
Dism /Mount-Wim /WimFile:"boot.wim" /Index:1 /MountDir:"C:\Mount"

# Copy OSD module
Copy-Item -Path "C:\Temp\Modules\OSD" -Destination "C:\Mount\Program 
Files\WindowsPowerShell\Modules\" -Recurse

# Unmount and commit
Dism /Unmount-Wim /MountDir:"C:\Mount" /Commit
MDT Equivalent:
# Copy to Extra Files
Copy-Item "C:\Temp\Modules\OSD" "C:\DeploymentShare\Extra Files\Program 
Files\WindowsPowerShell\Modules\" -Recurse

# MDT injects during boot.wim build
Update-MDTDeploymentShare -Path "DS001:"
B. Auto-Import Configuration
Method: Profile.ps1 script (see section 2A above)
Import Command:
Import-Module OSD -Force -Global -ErrorAction SilentlyContinue
Verification in WinPE:
Get-Module OSD -ListAvailable
Get-Command -Module OSD
 
8. Autostart Behavior
A. GUI Autostart
Configuration File: X:\OSDCloud\Config\Start-OSDCloudGUI-Auto.ps1
Content:
# Auto-start Start-OSDCloudGUI with pre-configured settings
Start-OSDCloudGUI
Trigger: startnet.cmd checks for file existence and executes if present
startnet.cmd section:
if exist X:\OSDCloud\Config\Start-OSDCloudGUI-Auto.ps1 (
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File X:\OSDCloud\Config\Start-
OSDCloudGUI-Auto.ps1
)
B. CLI Autostart with Parameters
Configuration File: X:\OSDCloud\Config\Start-OSDCloud-Auto.ps1
Content 
Example:
# Auto-start Start-OSDCloud with specific parameters
Start-OSDCloud -OSName "Windows 11 22H2 x64" -OSEdition Enterprise -OSLanguage 
en-us -Restart
C. JSON-Driven Autostart
Configuration File: X:\OSDCloud\Config\Start-OSDCloudGUI.json
Content:
{
  "AutoStart": true,
  "ImageIndex": 6,
  "ScreenshotCapture": true,
  "Restart": true,
  "Manufacturer": "Dell",
  "Product": "Latitude",
  "OSName": "Windows 11 22H2 x64",
  "OSEdition": "Enterprise",
  "OSLanguage": "en-us",
  "OSLicense": "Volume"
}
Processing:
# Start-OSDCloudGUI reads JSON and applies settings
$Config = Get-Content "X:\OSDCloud\Config\Start-OSDCloudGUI.json" |
ConvertFrom-
Json
if ($Config.AutoStart -eq $true) {
    Start-OSDCloud -OSName $Config.OSName -OSEdition $Config.OSEdition -
OSLanguage $Config.OSLanguage -Restart:$Config.Restart
}
MDT Equivalent:
# Bootstrap.ini
[Default]
SkipBDDWelcome=YES

# CustomSettings.ini
[Default]
OSInstall=Y
SkipTaskSequence=YES
TaskSequenceID=WIN11-ENT
SkipComputerName=NO
SkipDomainMembership=YES
 
9. Branding and Visual Modifications
A. Wallpaper Replacement
File: \Windows\System32\winpe.jpg
Standard ADK: Solid black background
OSDCloud: Custom blue gradient with OSDCloud logo
Replacement Process:
# Mount WIM
Dism /Mount-Wim /WimFile:"boot.wim" /Index:1 /MountDir:"C:\Mount"

# Replace wallpaper
Copy-Item -Path "C:\Branding\OSDCloud-Wallpaper.jpg" -Destination 
"C:\Mount\Windows\System32\winpe.jpg" -Force

# Unmount and commit
Dism /Unmount-Wim /MountDir:"C:\Mount" /Commit
Image Specifications:
*	Format: JPEG
*	Resolution: 1920x1080 (scales for other resolutions)
*	Color depth: 24-bit
*	File size: <500 KB recommended
MDT Equivalent:
Copy-Item "C:\Branding\Company-Wallpaper.jpg" "C:\DeploymentShare\Extra 
Files\Windows\System32\winpe.jpg"
B. Console Branding
Implementation: Profile.ps1 (see section 2A)
Elements:
*	ASCII art logo
*	Version information
*	Branded colors (Cyan on Black)
*	Custom window title
*	Welcome message with commands
 
10. Logging Configuration
A. Log Directory Creation
Directories Created:
Path
Purpose
X:\OSDCloud\Logs\
Main OSDCloud 
logs
X:\Windows\Logs\DISM\
DISM operation logs
X:\Windows\Panther\
Windows Setup logs (post-
apply)
Creation Method:
# In WinPE startup
New-Item -Path "X:\OSDCloud\Logs" -ItemType Directory -Force
New-Item -Path "X:\Windows\Logs\DISM" -ItemType Directory -Force
B. Logging Functions
Implementation in OSD Module:
function Write-OSDLog {
    param(
        [string]$Message,
        [string]$Component = "OSDCloud",
        [ValidateSet("Info","Warning","Error")]
        [string]$Type = "Info"
    )
    
    $Time = Get-Date -Format "HH:mm:ss.fff"
    $Date = Get-Date -Format "MM-dd-yyyy"
    $TypeCode = switch($Type) {
   
     "Info" {1}
        "Warning" {2}
        "Error" {3}
    }
    
    $LogEntry = "<![LOG[$Message]LOG]!><time=`"$Time+000`" date=`"$Date`" 
component=`"$Component`" context=`"`" type=`"$TypeCode`" thread=`"`" 
file=`"`">"
    Add-Content -Path "X:\OSDCloud\Logs\OSDCloud.log" -Value $LogEntry -ErrorAction 
SilentlyContinue
}

# Usage
Write-OSDLog -Message "Starting OS deployment" -Component "Start-OSDCloud" -
Type Info
Log Format: CMTrace-compatible (readable in Configuration Manager Trace Log Tool)
C. Screenshot Capture
Implementation:
# Capture screenshot at deployment milestones
Add-Type -AssemblyName System.Windows.Forms
$Screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$Bitmap = New-Object System.Drawing.Bitmap $Screen.Width, $Screen.Height
$Graphics = [System.Drawing.Graphics]::FromImage($Bitmap)
$Graphics.CopyFromScreen($Screen.Location, [System.Drawing.Point]::Empty, 
$Screen.Size)
$Bitmap.Save("X:\OSDCloud\Logs\Screenshot-$(Get-Date -Format 'yyyyMMdd-
HHmmss').png")
$Graphics.Dispose()
$Bitmap.Dispose()
Trigger: Enabled via Start-OSDCloudGUI.json "ScreenshotCapture": true
 

11-15. Additional Transformations (Summary)
11. Execution Policy
*	See sections 1B and 2A (startnet.cmd and Profile.ps1)
12. File System Modifications
*	winpeshl.ini, startnet.cmd, Profile.ps1, winpe.jpg (covered above)
13. Service Configuration
*	WlanSvc, Dhcp, Dnscache (covered in sections 3B and 4B)
14. WinPE Optional Components
OSDCloud typically includes:
*	WinPE-WMI
*	WinPE-NetFx
*	WinPE-Scripting
*	WinPE-PowerShell
*	WinPE-DismCmdlets
*	WinPE-SecureBootCmdlets
*	WinPE-StorageWMI
*	WinPE-WinReCfg
Injection:
Dism /Image:"C:\Mount" /Add-Package /PackagePath:"C:\Program Files (x86)\Windows 
Kits\10\Assessment and Deployment Kit\Windows Preinstallation 
Environment\amd64\WinPE_OCs\WinPE-WMI.cab"
Dism /Image:"C:\Mount" /Add-Package /PackagePath:"C:\Program Files (x86)\Windows 
Kits\10\Assessment and Deployment Kit\Windows Preinstallation 
Environment\amd64\WinPE_OCs\en-us\WinPE-WMI_en-us.cab"
# Repeat for all optional components
15. Cleanup and Optimization
# Remove unnecessary language packs
Dism /Image:"C:\Mount" /Remove-Package /PackageName:"WinPE-FontSupport-JA-JP"

# Clean component store
Dism /Image:"C:\Mount" /Cleanup-Image /StartComponentCleanup

# Optimize for size
Dism /Export-Image /SourceImageFile:"boot.wim" /SourceIndex:1 
/DestinationImageFile:"boot-optimized.wim" /Compress:max
 
Complete Transformation Workflow
Step-by-step process Edit-OSDCloudWinPE performs:
1.	Mount boot.wim
2.	Modify winpeshl.ini (add startnet.cmd launch)
3.	Create/modify startnet.cmd (network 
init, PowerShell config, auto-start)
4.	Create Profile.ps1 (branding, module import, help text)
5.	Inject network drivers (Ethernet, Wi-Fi)
6.	Inject storage drivers (NVMe, RAID)
7.	Enable Wi-Fi service (registry: WlanSvc Start = 2)
8.	Enable network services (registry: Dhcp, Dnscache Start = 2)
9.	Set ExecutionPolicy (registry: Bypass)
10.	Configure PSModulePath (registry: add custom paths)
11.	Copy OSD module (to \Program Files\WindowsPowerShell\Modules\OSD)
12.	Replace wallpaper (winpe.jpg)
13.	Add optional components (if not already present)
14.	Apply registry modifications (all HKLM changes)
15.	Create log directories (in WIM for runtime use)
16.	Clean and optimize (remove unused components, compress)
17.	Unmount and commit WIM
Total transformation time: ~5-10 minutes (depending on driver count)
 
MDT Implementation Summary
To replicate ALL Edit-OSDCloudWinPE transformations in MDT:
1.	Create Extra Files directory structure
2.	Create custom startnet.cmd with network 
init and PowerShell launch
3.	Create Profile.ps1 with branding and module import
4.	Add Wi-Fi drivers to Out-of-Box Drivers\WinPE x64\WiFi\
5.	Add network/storage drivers to Out-of-Box Drivers\WinPE x64\
6.	Create registry modification script (.reg or PowerShell)
7.	Copy OSD module to Extra Files\Program Files\WindowsPowerShell\Modules\
8.	Replace winpe.jpg in Extra Files\Windows\System32\
9.	Configure Bootstrap.ini for auto-start (SkipBDDWelcome=YES)
10.	Configure CustomSettings.ini with deployment defaults
11.	Update MDT deployment share (applies all Extra Files and drivers)
12.	Generate boot.wim and ISO
See T04_MDT_Implementation_Mapping_for_OSDCloud_Transformations.md for 
complete PowerShell implementation.