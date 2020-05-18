# NOIAPP micropython apps & tools for EPS32

This project contains micropython implementations to interact with BLE with contact tracing devices.

## Getting Started

These instructions will get you a copy of the project up and running on your eps32 board for development and testing purposes.

### Prerequisites

To play with this software you neeed:

* An Expressif [ESP32](https://www.espressif.com/en/products/socs/esp32/overview "Expressif ESP32") board;
  
* to fullfill [requirements](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html "Expressif ESP32") for micropython for esp32:
  
  * [Micropython](https://micropython.org/download/esp32/ "Microypython") on the board, see [here](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#deploying-the-firmware)
  * [esptool](https://github.com/espressif/esptool/ "esptool")
  * Adafruit MicroPython Tool ([ampy](https://github.com/scientifichackers/ampy))

## NoiApp for esp32

TBD

## Installing

Prerequisites: you need python3 with pyserial and a bash shell (Linux/Mac/Windows with Git Bash)

Run:

`./setup.sh <serial>`

where `<serial>` is the name of your serial device.

## Run

You can now run the tools by name (currently only bleSniffer) with:

`./run bleSniffer`

## Tools

### BLE sniffer

This simple tool scan for [BLE advertising](https://www.argenox.com/library/bluetooth-low-energy/ble-advertising-primer/) and output some information to help beacon analysis.

## Contributing

Please read (_italian_) [help us](https://www.protetti.app/helpus) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning.
