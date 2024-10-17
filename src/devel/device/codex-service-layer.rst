===================
Codex-Service-Layer
===================

Command line tool available on the reMarkable Paper Pro in :doc:`../../tech/developer-mode` that allows users to get various information about the device and change
certain parameters.


Available Commands
==================
.. code-block:: shell

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

    $ csl serialnumbers

Lists the serial numbers of the devices and various parts. This includes:

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

Lets the user control the frontlight and keyboard backlight.

.. code-block:: shell

    $ csl help light

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

    $ csl help marker

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

.. code-block:: shell
    
    $ csl marker -c
    NOT_CHARGING

Battery Level
_____________

.. code-block:: shell    

    $ csl marker -b
    81

UI Reported Battery Level
_________________________


.. code-block:: shell

    $ csl marker -x
    100

Marker Serial Number
____________________

.. code-block:: shell

    $ csl marker -s  
    RM04C00XXXXXXME

Marker UID
__________


.. code-block:: shell

    $ csl marker -i
    04 XX XX XX XX XX XX

Marker Docking State
____________________


.. code-block:: shell

    $ csl marker -d
    DOCKED

`power`
-------

Lets the user modify various power states and timeouts. 

.. code-block:: shell

    $ csl help power 

    Display power/battery state
        csl power
    
    Display power/battery state in follow mode, print changes interactively. Exit with Ctrl-C.
        csl power -f
    
    Request power state transition
        csl power -s run
        csl power -s suspend
        csl power -s suspend-then-hibernate
        csl power -s hibernate
        csl power -s poweroff
        csl power -s reboot
    
    Grab and release wakelocks. Text after a ':' is attempted to be parsed as a number to be used as the wakelock timeout, in milliseconds.
        csl power -w wakelock_name        # grab a wakelock
        csl power -w wakelock_name:300000 # grab a wakelock with a 5 minute timeout
        csl power -u wakelock_name        # release a wakelock
    
    Display real battery percentage in raw format.
        csl power -b
    
    Get real battery percentage in memfault's battery-monitor format: ChargerState:realBatteryPercentage.
        csl power -m
    
    Display charger connection status in raw format.
    1: Connected
    0: Not connected
    -1: Unknown
        csl power -c


`devicelock`
------------

`wifi`
------

`network`
---------

`ota`
-----


`deviceinfo`
------------

Lists version information of various parts of the Codex OS.


trace
--------
