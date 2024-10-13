===================
Codex-Service-Layer
===================

Command line tool available on the reMarkable Paper Pro in :doc:`../../tech/developer-mode` that allows users to get various information about the device and change
certain parameters


Available Commands
==================
```
    serialnumbers   Read and write serial numbers
    light           Query and control of light sources
    marker          Query marker status
    power           Query battery and power information
    devicelock      Query and control of the device operating mode
    wifi            Query and control of WiFi
    network         Get a list of all IP address
    ota             Perform OTA update operations
    deviceinfo      Get information of the device.
    trace           Generate a trace file
```

`csl serialnumbers`
-------------------

Lists the serial numbers of the devices and various parts. This includes
1 battery
2 device
3 epd
4 front_panel
5 pcba
6 touch
7 wlc

You can enter `csl serialnumbers <key>` to get the serial number of a specific part.



`csl light`
-----------

Lets you control the frontlight and keyboard backlight.

`csl light -p on`
_________________
 