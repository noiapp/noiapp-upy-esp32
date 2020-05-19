# NOIAPP micropython apps & tools for ESP32

This project contains micropython implementations to interact with BLE with contact tracing devices.

## Getting Started

These instructions will get you a copy of the project up and running on your eps32 board for development and testing purposes.

### Prerequisites

To play with this software you neeed:

* An Expressif [ESP32](https://www.espressif.com/en/products/socs/esp32/overview "Expressif ESP32") board;
  
* to fullfill [requirements](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html "Expressif ESP32") for micropython for esp32:
  
  * [Micropython](https://micropython.org/download/esp32/ "Microypython") on the board, see [here](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#deploying-the-firmware)
  * [esptool](https://github.com/espressif/esptool/ "esptool")
  * A local version of Python3 with pyserial library
  * A bash shell (Linux/Mac/Windows with Git Bash)


### Installing

`./setup.sh <serial>`

where `<serial>` is the name of your serial device.

### Executing

You can now run the tools by name with:

`./run.sh <tool> [-f] args...`

where 
- `<tool>` is the name of the script in `tools` without `.py`
- `-f` follow the output indefinitely (press ^C to interrupt)
- you can pass multiple args as strings (but do not put single quotes in it!)

args are then available inside the script in the array `args` as strings, and args[0] is the script name.

## Tools

### BLE sniffer

This simple tool scan for [BLE advertising](https://www.argenox.com/library/bluetooth-low-energy/ble-advertising-primer/) and output some information to help beacon analysis.

usage: `./run.sh bleSniffer -f 2000`

the `2000` is the number of milliseconds it must be listening.

## Contributing

Please read (_italian_) [help us](https://www.protetti.app/helpus) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning.
