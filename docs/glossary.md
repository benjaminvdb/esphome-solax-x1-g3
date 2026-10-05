# Glossary

Every technical word used in this project, in plain language.

**3V3 / 3.3 V** — The voltage the D1 mini works with. The pin labelled *3V3* supplies it.

**A and B** — The two RS485 wires. Data travels as the difference between them.

**API encryption key** — A long random password that protects the connection between the
D1 mini and Home Assistant. Each device should have its own.

**Baud rate** — How fast data travels over the cable, in bits per second. This inverter uses 9600.

**D1 mini (Wemos D1 mini)** — A small, cheap board with a Wi-Fi chip (the ESP8266) that
runs ESPHome. Its pins are labelled D0–D8, 3V3, 5V and GND.

**DE / RE** — "Driver enable" and "receiver enable" on the RS485 module: they decide
whether the module talks or listens. Here they're joined and connected to pin D5.

**DI / RO** — "Driver input" (data going *into* the module, to be sent to the inverter)
and "receiver output" (data coming *out* of the module, received from the inverter).

**ESP8266** — The Wi-Fi chip on the D1 mini.

**ESPHome** — Free software that turns a small board like the D1 mini into a device for
Home Assistant, using a configuration file instead of programming.

**ESPHome Device Builder** — The Home Assistant add-on where you edit ESPHome
configurations and install them onto boards.

**Firmware** — The software that runs on a device like the D1 mini.

**GND (ground)** — The 0-volt reference that all parts share. Every circuit needs one.

**Hexadecimal** — Counting in base 16, written with `0x` in front. `0x400` is 1024.

**Home Assistant** — Free software for home automation that collects data from devices
and lets you build dashboards and automations.

**Inverter** — The box that turns the panels' direct current (DC) into the alternating
current (AC) your house and the grid use.

**kWh (kilowatt-hour)** — An amount of energy: 1,000 watts for one hour.

**MAX485 / MAX3485** — Common chips (and the small modules built around them) that
translate between RS485 and the D1 mini.

**Modbus** — A simple way for a controller to ask a device for numbers stored in registers.

**OTA (over the air)** — Installing new firmware over Wi-Fi instead of a USB cable.

**Register** — A numbered slot in the inverter that holds one measurement as a whole
number between 0 and 65,535.

**RJ45** — The plug on a network (Ethernet) cable, with 8 pins.

**RS485** — A way to send data over two wires that works well over long cables.

**Secrets (`secrets.yaml`)** — A file in ESPHome Builder that stores private values like
your Wi-Fi password, so configuration files can refer to them by name.

**Solder** — Melting a small amount of metal to join wires or pins permanently.

**String** — A group of solar panels wired in a row. This inverter has two inputs, DC1
and DC2, one per string.

**T-568B / T-568A** — The two standard colour orders for the wires in a network cable.

**TTL** — Here: the simple 3.3-volt signals the D1 mini uses, as opposed to RS485.

**YAML** — The text format of ESPHome configuration files. Indentation (spaces at the
start of a line) matters.
