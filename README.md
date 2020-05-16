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

## Tools

### BLE sniffer

This simple tool scan for [BLE advertising](https://www.argenox.com/library/bluetooth-low-energy/ble-advertising-primer/) and output some information to help beacon analysis.

#### Upload on board

Using esptool you can upload on yor esp32 module with

```
ampy -p <your_serial_device> put tools
```

on Linux is something like

```
ampy -p /dev/ttyUSBx put tools
```

You can use [webrepl](http://docs.micropython.org/en/latest/esp32/quickref.html?highlight=webrepl#webrepl-web-browser-interactive-prompt) to upload the file and get results.

#### Running the sniffer

Once uploaded the sniffer can be run with

```
ampy -p /dev/ttyUSBx run tools/bleSniffer.py
```

or importing on micropython REPL

```
>>> uos.chdir('tools')
>>> import bleSniffer.py
```

## Contributing

Please read (_italian_) [help us](https://www.protetti.app/helpus) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning.
