> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deep-dive/connect-azure-in-winpe.md).

# Connect Azure in WinPE

## Connect-AzOSDCloud

This is an OSDCloud function that is used in WinPE to authenticate to Azure using Device Code flow.  I'll explain in detail how this works

{% hint style="info" %}
**I sorted all this out while at the MMSMOA 2022 Conference on Day 2, essentially making the OSDCloud Azure session on Day 1 obsolete as SAS Tokens and Key Vault are no longer needed**
{% endhint %}

## Required PowerShell Modules

The following Modules are installed or updated when executing this function.  This may cause an execution delay depending on the internet connection to the PSGallery Repository

* [ ] **AzureAD**
* [ ] **Az.Accounts**
* [ ] **Az.KeyVault**
* [ ] **Az.Resources**
* [ ] **Az.Storage**
* [ ] **Microsoft.Graph.DeviceManagement**

## Connect-AzAccount (Az.Accounts)

This is the function used to authenticate to Azure from WinPE

```powershell
Connect-AzAccount -UseDeviceAuthentication -AuthScope Storage -ErrorAction Stop
```

![](/files/uXqpQHtEucvA3V4AEpf7)

### -UseDeviceAuthentication

This parameter forces the authentication to occur on a separate device. This can be another computer, a smartphone, or even by a third party by providing them with the code (think Help Desk). The reason this is done is that the standard authentication does not work in WinPE

{% embed url="<https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-authentication-flows#device-code>" %}

### -Authscope Storage

If this parameter is left out, another Authentication may be required later, so since we know that we must access Azure Storage, we might as well do this now

![](/files/6ssyNk39inR4tkNZbaub)

{% embed url="<https://docs.microsoft.com/en-us/powershell/module/az.accounts/connect-azaccount?view=azps-7.5.0>" %}

## Subscription

Once you have been authenticated to Azure AD, this Azure Subscription routine is run. By default, Azure will pretty much randomly select the Azure Subscription that is used, which may not be the one you need to use for OSDCloud. This routine will determine if you have more than one Subscription and then prompt you to select the proper Subscription

```powershell
$Global:AzSubscription = Get-AzSubscription

if (($Global:AzSubscription).Count -ge 2) {
    $i = $null
    $Results = foreach ($Item in $Global:AzSubscription) {
        $i++

        $ObjectProperties = @{
            Number  = $i
            Name    = $Item.Name
            Id      = $Item.Id
        }
        New-Object -TypeName PSObject -Property $ObjectProperties
    }

    $Results | Select-Object -Property Number, Name, Id | Format-Table | Out-Host

    do {
        $SelectReadHost = Read-Host -Prompt "Select an Azure Subscription by Number"
    }
    until (((($SelectReadHost -ge 0) -and ($SelectReadHost -in $Results.Number))))

    $Results = $Results | Where-Object {$_.Number -eq $SelectReadHost}

    $Global:AzContext = Set-AzContext -Subscription $Results.Id
}
else {
    $Global:AzContext = Get-AzContext
}
```

![](/files/gHDwWAQqI5mG0SfJfHVj)

Additionally the following Global Variables are created for this PowerShell session

```powershell
$Global:AzSubscription = Get-AzSubscription
$Global:AzContext = Get-AzContext
```

## Connected to Azure (Subscription)

Once you have successfully connected to Azure (by way of having an Azure Context), the following informational routine will take place.  This will primarily set some more Global Variables so you can easily access them

If there is a failure in this routine, it is because the value for your Azure Subscription will be empty. This typically means that you do not have access to any Azure Resources. Go back to OSDCloud Azure Setup and give your user access to Azure Storage and this will sort itself out.  If you ping me and ask about this error, I will simply ignore it.  It's documented here, and in the Warning message.  there is no need for a third opinion.

```powershell
Write-Host -ForegroundColor Green 'Connected to Azure'
Write-Host -ForegroundColor DarkGray "========================================================================="
$Global:AzAccount = $Global:AzContext.Account
$Global:AzEnvironment = $Global:AzContext.Environment
$Global:AzTenantId = $Global:AzContext.Tenant
$Global:AzSubscription = $Global:AzContext.Subscription

Write-Host -ForegroundColor Cyan        '$Global:AzAccount:        ' $Global:AzAccount
Write-Host -ForegroundColor Cyan        '$Global:AzEnvironment:    ' $Global:AzEnvironment
Write-Host -ForegroundColor Cyan        '$Global:AzTenantId:       ' $Global:AzTenantId
Write-Host -ForegroundColor Cyan        '$Global:AzSubscription:   ' $Global:AzSubscription
if ($null -eq $Global:AzContext.Subscription) {
    Write-Warning 'You do not have access to an Azure Subscriptions'
    Write-Warning 'This is likely due to not having rights to Azure Resources or Azure Storage'
    Write-Warning 'Contact your Azure administrator to resolve this issue'
    Break
}
Write-Host -ForegroundColor DarkGray    'Azure Context:             $Global:AzContext'
```

![](/files/ImwMDzugxyQR0aINQUy3)

## Access Tokens and Headers

This is probably the most fun you will see while reading this.  Since we are authenticated to Azure, this routine will automatically get the Azure Access Tokens and create Headers automatically as Global Variables.  These can be used for HTTP RestMethod requests (which will be released later)

* [ ] **AadGraph**
* [ ] **KeyVault**
* [ ] **MSGraph**
* [ ] **Storage**

```powershell
Write-Host -ForegroundColor DarkGray    'Access Tokens:             $Global:Az*AccessToken'
Write-Host -ForegroundColor DarkGray    'Headers:                   $Global:Az*Headers'
Write-Host ''
#=================================================
#	AAD Graph
#=================================================
$Global:AzAadGraphAccessToken = Get-AzAccessToken -ResourceTypeName AadGraph
$Global:AzAadGraphHeaders = @{
    'Authorization' = 'Bearer ' + $Global:AzAadGraphAccessToken.Token
    'Content-Type'  = 'application/json'
    'ExpiresOn'     = $Global:AzAadGraphAccessToken.ExpiresOn
}
#=================================================
#	Azure KeyVault
#=================================================
$Global:AzKeyVaultAccessToken = Get-AzAccessToken -ResourceTypeName KeyVault
$Global:AzKeyVaultHeaders = @{
    'Authorization' = 'Bearer ' + $Global:AzKeyVaultAccessToken.Token
    'Content-Type'  = 'application/json'
    'ExpiresOn'     = $Global:AzKeyVaultAccessToken.ExpiresOn
}
#=================================================
#	Azure MSGraph
#=================================================
$Global:AzMSGraphAccessToken = Get-AzAccessToken -ResourceTypeName MSGraph
$Global:AzMSGraphHeaders = @{
    'Authorization' = 'Bearer ' + $Global:AzMSGraphAccessToken.Token
    'Content-Type'  = 'application/json'
    'ExpiresOn'     = $Global:AzMSGraphHeaders.ExpiresOn
}
#=================================================
#	Azure Storage
#=================================================
$Global:AzStorageAccessToken = Get-AzAccessToken -ResourceTypeName Storage
$Global:AzStorageHeaders = @{
    'Authorization' = 'Bearer ' + $Global:AzStorageAccessToken.Token
    'Content-Type'  = 'application/json'
    'ExpiresOn'     = $Global:AzStorageHeaders.ExpiresOn
}
```

## AzureAD

Finally, AzureAD will be connected using the AAD Access Token

```powershell
#=================================================
#	AzureAD
#=================================================
$Global:AzureAD = Connect-AzureAD -AadAccessToken $Global:AzAadGraphAccessToken.Token -AccountId $Global:AzContext.Account.Id
```

## Summary

Hopefully this gives you some insight on how the connection to Azure is done in WinPE.  There are lots of moving parts, but it should support connecting to more than just Azure Storage

## Sponsor

{% embed url="<https://www.recastsoftware.com/?utm_source=osdeploy&utm_medium=ad&utm_campaign=web>" %}
OSDeploy is sponsored by Recast Software
{% endembed %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/osdcloud-azure/deep-dive/connect-azure-in-winpe.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
