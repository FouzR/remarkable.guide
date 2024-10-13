===================
Codex-Service-Layer
===================

Command line tool available on the reMarkable Paper Pro in :doc:`../../tech/developer-mode` that allows users to get various information about the device and change
certain parameters


Available Commands
==================
.. code-block:: shell
    root@imx8mm-ferrari:~# csl help
    usage: csl <command> [<args>]
    build: 2024-09-12T05:45:25Z 

    These are common csl commands used in various situations:

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

    Use 'csl <command> [...]' to enable additional output.
    Use 'csl help <command> to get additional help.


`serialnumbers`
---------------

.. code-block:: shell
    csl serialnumbers

Lists the serial numbers of the devices and various parts. This includes
1. battery
2. device
3. epd
4. front_panel
5. pcba
6. touch
7. wlc

You can enter `csl serialnumbers <key>` to get the serial number of a specific part.


`light`
-------

Lets you control the frontlight and keyboard backlight.

.. code-block:: shell
    root@imx8mm-ferrari:~# csl help light

    Print current state of the light (frontlight by default)
        csl light [--source <frontlight | keyboard | funkey>]

    Turn light on/off
        csl light [--source ...] -p on  | --power on
        csl light [--source ...] -p off | --power off

    Set light brightness
        csl light [--source ...] -b <0..100> | --brightness <0..100>

    The -p and -b options can be combined. E.g.:
        csl light --source frontlight -p on -b 50

`marker`
--------

.. code-block:: shell
    root@imx8mm-ferrari:~# csl help marker

    Flags to print various pieces of information
        csl marker -c       Charging state
        csl marker -b       Battery level
        csl marker -x       User battery level
        csl marker -s       Marker serial
        csl marker -i       Marker UID
        csl marker -d       Docking state

    Follow mode, print state changes as they happen
        csl marker -f
        csl marker --version                Display ASIC+MCU FW versions
        csl marker --version-shipped-asic   Display ASIC FW version shipped on device
        csl marker --version-shipped-mcu    Display MCU FW version shipped on device

    Flags to alter Marker

        csl marker --update-mcu         Update MCU FW
        csl marker --update-asic        Update ASIC FW

**Example:** 

Charging state
______________

`csl marker -c`
.. code-block:: shell
    NOT_CHARGING

Battery Level
_____________

`csl marker -b`
.. code-block:: shell    
    81

UI Reported Battery Level
_________________________

`csl marker -x`
.. code-block:: shell
   100

Marker Serial Number
____________________

`csl marker -s`
.. code-block:: shell
    RM04C00XXXXXXME

Marker UID
__________

`csl marker -i`
.. code-block:: shell
    04 XX XX XX XX XX XX

Marker Docking State
____________________

`csl marker -d`
.. code-block:: shell
    DOCKED