```markdown
---
title: WinPE Boot Flow Before and After OSDCloud
source_url: https://www.osdcloud.com/osdcloud-v1
version: OSD 23.5.21.1+
last_updated: May 21, 2023
category: Transformation
section_path: OSDCloud v1 > Transformations > Boot Flow Analysis
doc_type: comparison_analysis
---

# WinPE Boot Flow Before and After OSDCloud

## Overview

This document provides a detailed, stage-by-stage comparison of the Windows 
Preinstallation Environment (WinPE) boot sequence before and after OSDCloud 
transformations are applied.
Understanding these differences is critical for replicating 
OSDCloud behavior in MDT or troubleshooting boot issues.

## Boot Sequence Comparison Table

|
Stage | Standard ADK WinPE | OSDCloud-Modified WinPE | Time Difference |
|-------|-------------------|------------------------|-----------------|
| **1. UEFI/BIOS Firmware** |
Initialize hardware, load boot manager | Identical | 0s |
| **2. Boot Manager Load** |
bootmgr.efi (UEFI) or bootmgr (BIOS) reads BCD | Identical 
| 0s |
| **3. BCD Reading** |
Boot Configuration Database points to boot.wim | Identical | 0s |
| **4. boot.wim Load** |
Load WIM into RAM disk (ramdisk) | boot.wim larger due to 
drivers/modules (+150-200 MB) | +2-3s |
| **5.
Kernel Init** | ntoskrnl.exe starts, initialize kernel | Identical | 0s |
| **6. Driver Loading** |
Load default inbox drivers only | Load default + Wi-Fi + NVMe + 
additional network drivers | +3-5s |
|
**7. winpeshl.ini** | Launch wpeinit.exe only | Launch wpeinit.exe **then** startnet.cmd | +1s |
| **8. wpeinit Execution** |
Hardware detection, PnP, load matched drivers | Identical 
(but more drivers available from step 6) | +2s |
| **9.
Network Init** | **NONE (manual required)** | **wpeutil InitializeNetwork 
(automatic)** | +8s |
| **10. Network Wait** | N/A |
5-second stabilization delay (ping localhost) | +5s |
| **11. Shell Launch** | cmd.exe prompt (black screen) |
**PowerShell with profile** (branded console) | +3s |
| **12. Module Loading** | None | **Import OSD module** |
+3s |
| **13. User Interface** | cmd.exe prompt, no guidance |
PowerShell console with 
banner, network status, command help **OR** Start-OSDCloudGUI (if autostart) | +2s |
| **14. Deployment Readiness** |
User must navigate to deployment tools manually | 
**Ready immediately** (single command or auto-start) | -30s (faster UX) |
|
**TOTAL BOOT-TO-READY** | **~90 seconds** | **~30 seconds to deployment-ready 
state** | **66% faster** |
---

## Detailed Stage-by-Stage Analysis

### Stage 1: UEFI/BIOS Firmware Initialization

**Standard ADK:**
- Firmware performs Power-On Self-Test (POST)
- Initializes CPU, RAM, storage controllers
- Searches for boot devices in configured order
- Loads UEFI bootloader (bootx64.efi) or BIOS bootloader (bootmgr)

**OSDCloud:**
- Identical (no modifications at firmware level)

**Timing:** ~3-5 seconds (hardware-dependent)

---

### Stage 2: Boot Manager Load

**Standard ADK:**
- **UEFI:** Loads `\EFI\Boot\bootx64.efi` ?
`\EFI\Microsoft\Boot\bootmgfw.efi`
- **BIOS:** Loads Master Boot Record (MBR) ? `bootmgr`

**OSDCloud:**
- Identical (boot manager files unchanged)

**Timing:** ~1-2 seconds

---

### Stage 3: Boot Configuration Database (BCD) Reading

**Standard ADK:**
- Boot manager reads BCD store
- Locates boot entry pointing to `\sources\boot.wim`
- Configures ramdisk parameters

**BCD Entry (Standard):**
identifier {default} device ramdisk=[boot]\sources\boot.wim,{ramdiskoptions} path 
\windows\system32\boot\winload.efi description Windows Setup locale en-US inherit 
{bootloadersettings} osdevice ramdisk=[boot]\sources\boot.wim,{ramdiskoptions} 
systemroot \windows detecthal Yes winpe Yes

**OSDCloud:**
- Identical BCD configuration
- **Difference:** boot.wim is larger (400-600 MB vs 250-300 MB standard)
- Larger WIM = longer load time in next stage

**Timing:** ~0.5 seconds

---

### Stage 4: boot.wim Load into RAM

**Standard ADK:**
- Ramdisk driver (ramdisk.sys) mounts boot.wim as X:\
- Typical size: 
250-300 MB
- Load time: ~5-7 seconds on modern hardware

**OSDCloud:**
- Same ramdisk mounting process
- Larger size: 400-600 MB (due to injected drivers, OSD module, additional components)
- Load time: ~8-10 seconds

**Size Breakdown:**

|
Component | Standard ADK | OSDCloud | Difference |
|-----------|-------------|----------|------------|
| Base WinPE | 220 MB | 220 MB |
0 MB |
| Inbox drivers | 30 MB | 30 MB | 0 MB |
| **Wi-Fi drivers** |
0 MB | 50 MB | +50 MB |
| **NVMe/storage drivers** | 0 MB | 30 MB |
+30 MB |
| **Additional network drivers** | 0 MB | 20 MB | +20 MB |
|
**OSD PowerShell module** | 0 MB | 40 MB | +40 MB |
| **WinPE optional components** |
0 MB | 30 MB | +30 MB |
| **Total** | **250 MB** | **420 MB** |
**+170 MB** |

**Timing Difference:** +2-3 seconds

---

### Stage 5: Windows Kernel Initialization

**Standard ADK:**
- ntoskrnl.exe (Windows kernel) starts
- Initialize kernel subsystems (memory management, process management, etc.)
- Load boot-critical drivers (disk, file system, ramdisk)

**OSDCloud:**
- Identical (no kernel modifications)

**Timing:** ~2-3 seconds

---

### Stage 6: Driver Loading (PnP Enumeration)

**Standard ADK:**
- Plug and Play (PnP) manager enumerates hardware
- Loads drivers from `\Windows\System32\drivers\` and driver store
- **Default drivers only:** Basic network (limited adapters), basic storage, USB

**OSDCloud:**
- Same PnP process
- **More drivers available:** Wi-Fi, modern NVMe, additional NICs
- **Result:** More hardware detected and functional immediately

**Driver Count Comparison:**

|
Driver Type | Standard ADK | OSDCloud |
|------------|-------------|----------|
| Network (Ethernet) | ~20 adapters | ~50 adapters |
|
Wi-Fi | 0 adapters | ~30 adapters |
| NVMe Storage | ~5 controllers | ~15 controllers |
|
USB 3.x | Default | Default |

**Timing Difference:** +3-5 seconds (more drivers to process)

---

### Stage 7: winpeshl.ini Execution

**Standard ADK (winpeshl.ini):**
```ini
[LaunchApps]
%SYSTEMDRIVE%\Windows\System32\wpeinit.exe
Result: Launches wpeinit.exe only, then stops (no further automation)
OSDCloud (winpeshl.ini):
[LaunchApps]
%SYSTEMDRIVE%\Windows\System32\wpeinit.exe
%SYSTEMDRIVE%\Windows\System32\startnet.cmd
Result: Launches wpeinit.exe, waits for completion, then launches startnet.cmd
Timing Difference: +1 second (script launch overhead)
 
Stage 8: wpeinit.exe Hardware Detection
Standard ADK:
*	wpeinit.exe performs final hardware detection
*	Applies registry settings
*	Starts plug-and-play services
*	Does NOT initialize network stack
*	Ends with cmd.exe prompt
OSDCloud:
*	Identical wpeinit.exe behavior
*	After completion, startnet.cmd continues execution
Timing: ~10-15 seconds (identical for both)
 
Stage 9: Network Stack Initialization
Standard ADK:
*	Network NOT initialized automatically
*	User must manually run: wpeutil InitializeNetwork
*	DHCP client: Stopped
*	DNS client: Stopped
*	Result: No IP address, no network connectivity
OSDCloud 
(startnet.cmd):
wpeutil InitializeNetwork
ping 127.0.0.1 -n 6 > nul
What wpeutil InitializeNetwork Does:
1.	Starts DHCP Client service
2.	Starts DNS Client service
3.	Initializes network interfaces
4.	Sends DHCP DISCOVER broadcast
5.	Receives DHCP OFFER from server
6.	Configures IP address, subnet mask, gateway, DNS servers
Timing:
*	Standard ADK: Never (manual intervention required, ~60-90 seconds after boot 
when user runs command)
*	OSDCloud: Automatic at ~20 seconds after boot, completes by ~28 seconds
Timing Difference: +8 seconds for OSDCloud, but -60 seconds in user workflow (no 
manual step)
 
Stage 10: Network Stabilization Wait
Standard ADK:
*	N/A (network not initialized)
OSDCloud (startnet.cmd):
ping 127.0.0.1 -n 6 > nul
Purpose:
*	Wait 5 seconds for network stack to stabilize
*	Ensure DHCP lease is fully acquired
*	Allow DNS registration to complete
Timing: 
+5 seconds
 
Stage 11: Shell Launch
Standard ADK:
*	wpeinit.exe completes
*	winpeshl.ini has no further entries
*	Falls back to cmd.exe (command prompt)
*	Black screen with X:\Windows\System32> prompt
*	No branding, no guidance
OSDCloud (startnet.cmd continues):
powershell.exe -NoExit -ExecutionPolicy Bypass
Triggers:
*	PowerShell launches
*	Reads Profile.ps1 automatically
*	Profile.ps1 executes (branding, module import, help text)
User Experience:
*	Branded blue/cyan console
*	OSDCloud ASCII art banner
*	Version information
*	Network status displayed
*	Available commands listed
*	Helpful prompts
Timing Difference: +3 seconds (PowerShell startup + profile execution)
 
Stage 12: Module Loading
Standard ADK:
*	No modules loaded
*	User must manually import any needed PowerShell modules
OSDCloud (Profile.ps1):
Import-Module OSD -Force -Global -ErrorAction SilentlyContinue
Result:
*	OSD module loaded automatically
*	70+ cmdlets available immediately
*	Start-OSDCloudGUI, Start-OSDCloud, Get-OSDCloudOS, etc. ready to use
Timing: +3 seconds
 
Stage 13: User Interface Presentation
Standard ADK:
*	cmd.exe prompt
*	User must: 

1.	Know deployment tools exist
2.	Navigate to tool location
3.	Launch manually
*	Typical user action time: 30-60 seconds
OSDCloud:
Option A: PowerShell Console (no autostart)
*	Branded console with instructions
*	User types Start-OSDCloudGUI and presses Enter
*	GUI launches in 2-3 seconds
Option B: Auto-Start GUI (if configured)
*	startnet.cmd detects X:\OSDCloud\Config\Start-OSDCloudGUI-Auto.ps1
*	Launches automatically
*	GUI appears without user interaction
Timing Difference: +2 seconds (GUI launch if autostart), -30 seconds user time (no 
navigation needed)
 
Stage 14: Deployment Readiness
Standard ADK:
*	User at cmd.exe prompt
*	Must navigate to deployment tools (e.g., wscript \\server\share\LiteTouch.wsf)
*	Typical time from boot to deployment start: 90-120 seconds
OSDCloud:
*	User at PowerShell with OSD module loaded OR
*	Start-OSDCloudGUI already running
*	Typical time from boot to deployment start: 30 seconds
Total Time Savings: 60-90 seconds
 

Network Initialization Timing Critical Path
Standard ADK (Manual Network Init)
Boot ? wpeinit (15s) ? cmd.exe prompt (0s) ?
User types wpeutil InitializeNetwork (30s) 
? 
Network initializes (10s) ?
User can proceed (total: ~55s + manual intervention)
OSDCloud (Automatic Network Init)
Boot ? wpeinit (15s) ? startnet.cmd launches (1s) ?
wpeutil InitializeNetwork (8s) ? 
Wait 5s (5s) ? PowerShell ready with network (total: ~29s, fully automatic)
Critical Difference:
*	Standard ADK: Network ready at ~55+ seconds IF user knows to run command
*	OSDCloud: Network ready at ~29 seconds automatically, no user action
 
Wi-Fi Availability Timing
Standard ADK
Wi-Fi Status: Not available
*	No Wi-Fi drivers injected by default
*	Even if manually injected, WlanSvc service not enabled
*	User must manually: 
1.	Inject drivers (before deployment)
2.	Enable WlanSvc service (via registry or sc command)
3.	Run netsh wlan show networks
4.	Run netsh wlan connect name=<SSID>
*	Wi-Fi UI: Never appears automatically
Time to Wi-Fi connectivity: Not achievable without pre-deployment customization
OSDCloud
Wi-Fi Status: Fully available and automatic
*	Wi-Fi drivers injected during Edit-OSDCloudWinPE
*	WlanSvc set 
to Automatic start
*	Service starts during wpeinit phase
Boot Sequence:
Boot (0s) ? wpeinit (15s) ? WlanSvc starts (16s) ?
Network init (25s) ? 
Wi-Fi UI available in system tray (28s)
User Experience:
1.	WinPE boots to PowerShell console
2.	Wi-Fi icon visible in taskbar/system tray
3.	User clicks icon
4.	Windows Wi-Fi selection UI appears
5.	User selects network and enters password
6.	Connected in 10-15 seconds
Time to Wi-Fi connectivity: ~40-45 seconds from boot (including user selection time)
 
Boot-to-Ready Performance Summary
Milestone
Standard ADK
OSDCloud
Improvement
Hardware initialized
5s
5s
0s
boot.wim loaded
12s
15s
-3s
Kernel started
15s
18s
-3s
Drivers loaded
20s
25s
-5s
wpeinit complete
30s
35s
-5s
Network initialized
Never (manual)
43s
N/A
Shell ready
35s (cmd.exe)
48s (PowerShell)
-13s
Deployment tool ready
90s+ (user navigation)
30s (auto-available)
+60s faster
Key Insight:
*	OSDCloud boot sequence is longer by 13 seconds due to larger WIM and more 
drivers
*	But deployment readiness is 60+ seconds faster due to automation eliminating 
user navigation time
*	Net result: 66% faster time-to-deployment
 
Critical Paths 
Comparison
Standard ADK Critical Path
Firmware (5s) ? Boot Manager (2s) ? BCD (0.5s) ? Load WIM (7s) ? 
Kernel (3s) ?
Drivers (5s) ? wpeinit (15s) ? cmd.exe (0s) ? 
User navigates (30s) ? User initializes network (40s) ?
Deployment starts
TOTAL: ~107 seconds
OSDCloud Critical Path
Firmware (5s) ? Boot Manager (2s) ? BCD (0.5s) ? Load WIM (10s) ?
Kernel (3s) ? Drivers (8s) ? wpeinit (15s) ? startnet.cmd (1s) ? 
Network init (8s) ? Wait (5s) ?
PowerShell (3s) ? Module load (3s) ? 
Ready (OR autostart GUI launches)
TOTAL: ~63 seconds to deployment-ready state (OR ~30s if GUI autostarts)
Improvement: 44-77 seconds faster (41-72% reduction in time-to-deploy)
 
Implications for MDT Implementation
To achieve OSDCloud boot speed in MDT:
1.	Inject drivers into WinPE:
o	Add Wi-Fi, modern NVMe, additional network drivers to Out-of-Box 
Drivers\WinPE x64\
2.	Modify startnet.cmd:
o	Add wpeutil InitializeNetwork
o	Add network stabilization wait
o	Launch PowerShell automatically
3.	Create PowerShell profile:
o	Add branding and help text
o	Import necessary modules
4.	Configure Bootstrap.ini:
o	Set SkipBDDWelcome=YES for auto-start
5.	Pre-configure CustomSettings.ini:
o	Set deployment defaults to minimize prompts
Expected Result:
*	Boot-to-deployment time: ~40-50 seconds (similar to OSDCloud)
*	Network initialized automatically
*	Deployment starts with minimal user interaction
Remaining MDT Limitation:
*	Wi-Fi UI does not appear automatically (requires 
manual PowerShell command: 
Start-Process "ms-availablenetworks:")
 
Troubleshooting Boot Issues
Slow Network Initialization
Symptoms:
*	wpeutil InitializeNetwork takes >20 seconds
*	DHCP lease acquisition fails
Causes:
*	Missing network drivers
*	DHCP server unreachable
*	Network interface not detected
OSDCloud Mitigation:
*	Extensive network driver injection (50+ adapters)
*	Automatic retry logic in OSD module
MDT Solution:
*	Add more network drivers to WinPE
*	Increase wait time after wpeutil InitializeNetwork
*	Add ipconfig /renew retry loop
PowerShell Not Launching
Symptoms:
*	startnet.cmd runs but PowerShell doesn't appear
Causes:
*	PowerShell optional components not included
*	Profile.ps1 syntax error
OSDCloud Prevention:
*	WinPE-PowerShell component always included
*	Profile.ps1 tested and validated
MDT Solution:
*	Verify WinPE-PowerShell optional component is added
*	Test Profile.ps1 syntax before deployment
Wi-Fi UI Not Appearing
Symptoms:
*	Wi-Fi drivers present but no Wi-Fi icon in system tray
Causes:
*	WlanSvc service not enabled
*	Service startup delayed
OSDCloud Prevention:
*	WlanSvc Start = 
2 (Automatic) in registry
*	DelayedAutoStart = 0 (immediate)
MDT Solution:
*	Set WlanSvc registry during boot.wim customization
*	Manually start service in startnet.cmd: net start WlanSvc