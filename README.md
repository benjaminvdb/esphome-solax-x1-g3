# SolaX inverter → Home Assistant, with a €6 Wi-Fi board

See what your solar panels are doing, live, in [Home Assistant](https://www.home-assistant.io/):
power, voltage, today's and lifetime production, and any fault the inverter reports.
No cloud account and no SolaX Wi-Fi dongle needed: a small board reads the data straight
from the inverter's communication port and sends it over your own Wi-Fi.

![Wiring diagram: inverter cable, RS485 module and Wemos D1 mini](images/wiring.svg)

**Never built anything like this before?** Good, this guide is written for you. You'll
connect a handful of wires between two small boards and a network cable, copy one configuration
file, and click *Install*. Every step tells you what you should see when it worked.

| | |
|---|---|
| **Difficulty** | Beginner. Soldering is optional (see [Build the circuit](docs/build.md)). |
| **Time** | About 1–2 hours the first time. |
| **Cost** | About €6–10 in parts, plus a network cable and a USB phone charger you may already have. |
| **Works with** | SolaX **X1 Boost, X1 Mini and X1 Air, generation 3 (G3)**. See [Will it work with my inverter?](#will-it-work-with-my-inverter) |

## What you'll get in Home Assistant

| Sensor | Example | Notes |
|---|---|---|
| Inverter Power | 1,626 W | What goes into your house right now. |
| Production Today | 2.7 kWh | Resets every morning. |
| Production Total | 13,275.6 kWh | Lifetime total, ready for the Energy dashboard. |
| Power DC1 / DC2, Total DC Power | 234 W / 1,423 W | Per panel string, and both together. |
| PV1/PV2 Input Voltage and Current | 223.5 V, 6.3 A | Per panel string. |
| Grid Voltage, Grid Frequency, Output Current | 235.6 V, 50.03 Hz | |
| Temperature | 37 °C | Inside the inverter. |
| Run Mode | Normal | Waiting, Checking, Normal, Fault… or Offline at night. |
| Fault | None | Names any fault the inverter reports, e.g. `GridVolt`. |

## What you need

| Part | Price (approx., 2026) | Notes |
|---|---|---|
| Wemos D1 mini (or a clone) | €3–5 | A small Wi-Fi computer board. Any "D1 mini" with an ESP8266 chip works. |
| RS485-to-TTL module | €1–3 | Translates between the inverter's cable and the D1 mini. A **MAX3485** (3.3 V) module is ideal; the common blue **MAX485** module works too (see [Build the circuit](docs/build.md#which-rs485-module)). |
| 8 jumper wires (female–female) | €1 | Or solder wires directly. |
| A network cable (Ethernet, RJ45 plug) | €0–3 | An old one is fine. You'll cut one plug off. |
| USB phone charger and micro-USB cable | €0 | Most likely already in a drawer. The cable must carry data for the first install. |
| A computer with Chrome or Edge | | For the first install over USB. |
| Home Assistant with the ESPHome Device Builder add-on | | [How to install the add-on](https://esphome.io/guides/getting_started_hassio/). |

Tools: wire strippers or a sharp knife, and a small screwdriver for the module's screw terminal.

## Steps

1. [Build the circuit](docs/build.md): connect the module to the D1 mini.
2. [Prepare the inverter and cable](docs/inverter.md): switch on Modbus in the inverter menu and make the cable.
3. [Install the software](docs/install.md): put ESPHome on the D1 mini and add it to Home Assistant.
4. [Use the data](docs/home-assistant.md): the Energy dashboard and useful automations.

Stuck? [Troubleshooting](docs/troubleshooting.md) is organised by what you see.

Curious how it works? [How it works](docs/how-it-works.md) explains Modbus, registers and the
choices in the configuration, and [Glossary](docs/glossary.md) explains every technical word.

## Will it work with my inverter?

- **Yes:** SolaX X1 Boost G3, X1 Mini G3 and X1 Air G3. These share one register map (the
  list of addresses where each value lives). The serial number of an X1 Boost G3 usually
  starts with `XB3`, `XAU`, `XBE` or `XBU`, and an X1 Mini G3 with `XM3`.
- **Tested on:** X1 Boost G3 (`XB33…`), ESPHome 2026.9.1, Home Assistant 2026.9.
- **No:** generation 4 inverters (`XB4…` and similar) use different addresses. Hybrid
  (battery) inverters, the X3 three-phase range, and the X1 Mini **G2** with the older
  SolaX protocol aren't covered either. For those, see the
  [SolaX Modbus integration](https://github.com/wills106/homeassistant-solax-modbus) or
  [syssi/esphome-solax-x1-mini](https://github.com/syssi/esphome-solax-x1-mini).

## Safety, in short

You only plug a network cable into the inverter's **communication port**, the port meant
for meters and monitoring equipment. **Never open the inverter**: it contains high
voltages, even after you switch it off. If the port sits behind a cover you aren't sure you
may open, ask your installer. More in [Prepare the inverter and cable](docs/inverter.md#safety).

## Credits

- **aiolos / [enri.nl](https://enri.nl/pcb/?page=modbus)** made the Modbus shield PCB this
  project started on, and hosts the [first version of this config](https://github.com/aiolos/ESPHome-config/blob/main/modbus-solax.yaml) (December 2022).
- **[syssi](https://github.com/syssi/esphome-solax-x1-mini)** for the SolaX RS485 work and
  the RJ45 pinout, and **[wills106](https://github.com/wills106/homeassistant-solax-modbus)**
  and contributors for the register research and the official SolaX protocol document.

## License

The configuration and scripts are [MIT](LICENSE). The documentation and images are
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): share and adapt them, with credit.

Contributions and questions are welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).
