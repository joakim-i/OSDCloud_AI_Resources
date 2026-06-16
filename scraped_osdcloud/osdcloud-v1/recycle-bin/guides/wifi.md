> For the complete documentation index, see [llms.txt](https://www.osdcloud.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://www.osdcloud.com/osdcloud-v1/recycle-bin/guides/wifi.md).

# WiFi

{% embed url="<https://www.recastsoftware.com/>" %}
OSDeploy is proudly sponsored by Recast Software
{% endembed %}

This guide will show you how to enable WiFi support in OSDCloud.  Currently WPA2 Personal is working and there are plans to enable other connection methods

## Development

WiFi support required a few people to test and code to get where we are today.  They deserve some recognition for their work.  Very special thanks to Ondrej Sebela for his excellent contribution

{% content-ref url="/pages/-MXzAbmEj6j\_TbVCYgBK" %}
[Broken mention](broken://pages/-MXzAbmEj6j_TbVCYgBK)
{% endcontent-ref %}

## New-OSDCloud.template -WinRE

WiFi doesn't work natively in WinPE, but there is minimal support in WinRE.  This means that your OSDCloud WinPE will have to be built using WinRE.  Follow the instructions to rebuild your Template at this link

{% content-ref url="/pages/-MXzI6I3IBeKzTTxxEBH" %}
[Broken mention](broken://pages/-MXzI6I3IBeKzTTxxEBH)
{% endcontent-ref %}

## New-OSDCloud.workspace

Any time you make changes to your Template, you will need to rebuild your Workspace.  Simply use this command to overwrite your existing Workspace

{% content-ref url="/pages/-MVzK\_o-xGl49jwx5-Vn" %}
[OSDCloud Workspace](/osdcloud-v1/osdcloud/setup/osdcloud-workspace.md)
{% endcontent-ref %}

## Edit-OSDCloud.winpe

Yes you will need to run your WinPE through an Edit pass.  If you have an Intel Wireless Network Adapter, then you are in luck as there is a CloudDriver which will add the drivers you need.  For other Wireless Network Adapters, you are going to have to experiment by adding the Driver.  Finally, this pass is needed to modify Startnet.cmd

{% content-ref url="/pages/-MY8O8lyguXpxfvF2I22" %}
[Broken mention](broken://pages/-MY8O8lyguXpxfvF2I22)
{% endcontent-ref %}

## WinPE (actually WinRE)

If you are lucky enough to have an Intel Wireless Network Adapter, then you will be presented with this PowerShell Window.  If you are connecting over Ethernet, just close this out.  You will also notice a minimized PowerShell Window, this is to do anything you want.  In my case, I used it to start taking Screenshots using Get-ScreenPNG

![](/files/-MY9-LSq_1n2psaY3hHC)

To start a Wireless WPA2 connection, simply enter the Index number of your SSID.  These are sorted by Signal and not SSID incase you couldn't tell

![](/files/-MY90-4Jw6jNgKQkgapD)

Once you make a selection, you will be prompted for credentials.  Simply enter the password for your SSID and press OK

![](/files/-MY90Bzw7At_jEzSi3lG)

Give it about 20 - 30 seconds and it should connect

![](/files/-MY90PeOEEpobPxOQWNV)

Once you are connected, the PowerShell Window for your WiFi connection should close, and a new PowerShell Window will open so you can **`Start-OSDCloud`**

![](/files/-MY90iXyWdOHVGn3F-8C)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://www.osdcloud.com/osdcloud-v1/recycle-bin/guides/wifi.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
