# ☀️ SolaX X1 Boost → Home Assistant, with a €6 Wi-Fi board

See what your solar panels are doing, live, in [Home Assistant](https://www.home-assistant.io/):
power, voltage, today's and lifetime production, and any fault the inverter reports.
**No cloud account and no SolaX Wi-Fi dongle needed:** a small board reads the data
straight from the inverter's communication port and sends it over your own Wi-Fi.

![Wiring diagram: inverter cable, RS485 module and Wemos D1 mini](images/wiring.svg)

**Never built anything like this before? Good, this guide is written for you.** You'll
connect a handful of wires between two small boards and a network cable, copy one
configuration file, and click *Install*. Every step tells you what you should see when it
worked.

| | |
|---|---|
| 🎓 **Difficulty** | Beginner. Soldering is optional. |
| ⏱️ **Time** | About 1–2 hours the first time. |
| 💶 **Cost** | About €6–10 in parts, plus a network cable and a USB phone charger you may already have. |
| ✅ **Works with** | SolaX **X1 Boost, generation 3 (G3)**. The X1 Mini G3 and X1 Air G3 are expected to work too; see [Will it work with my inverter?](#will-it-work-with-my-inverter) |

## 📊 What you'll get in Home Assistant

| Sensor | Example | Notes |
|---|--:|---|
| **Inverter Power** | 1,626 W | What goes into your house right now. |
| **Production Today** | 2.7 kWh | Resets every morning. |
| **Production Total** | 13,275.6 kWh | Lifetime total, ready for the Energy dashboard. |
| **Power DC1 / DC2**, **Total DC Power** | 234 W / 1,423 W | Per panel string, and both together. |
| **PV1/PV2 Input Voltage and Current** | 223.5 V, 6.3 A | Per panel string. |
| **Grid Voltage**, **Grid Frequency**, **Output Current** | 235.6 V, 50.03 Hz | |
| **Temperature** | 37 °C | Inside the inverter. |
| **Run Mode** | Normal | *Waiting*, *Checking*, *Normal*, *Fault*… or *Offline* at night. |
| **Fault** | None | Names any fault the inverter reports, e.g. `GridVolt`. |

## 🛒 What you need

| Part | Price¹ | Notes |
|---|--:|---|
| **Wemos D1 mini** (or a clone) | €3–5 | A small Wi-Fi computer board. Any *D1 mini* with an ESP8266 chip works. |
| **RS485-to-TTL module** | €1–3 | Translates between the inverter's cable and the D1 mini. A **MAX3485** module is ideal; the common blue **MAX485** module works too ([which one?](docs/build.md#which-rs485-module)). |
| **6–7 jumper wires** (female–female) | €1 | Or solder wires directly. |
| **Network cable** (Ethernet, RJ45 plug) | €0–3 | An old one is fine. You'll cut one plug off. |
| **USB phone charger** and **micro-USB cable** | €0 | Probably already in a drawer. The cable must carry data for the first install. |
| A computer with **Chrome or Edge** | | For the first install over USB. |
| **Home Assistant** with the **ESPHome Device Builder** add-on | | [How to install the add-on](https://esphome.io/guides/getting_started_hassio/). |

¹ Approximate, 2026.

🧰 **Tools:** wire strippers or a sharp knife, and a small screwdriver for the module's
screw terminal.

## 🧭 Steps

| Step | What you'll do | Time |
|:-:|---|---|
| 1 | [🔧 **Build the circuit**](docs/build.md): connect the module to the D1 mini. | 15–30 min |
| 2 | [🔆 **Prepare the inverter and cable**](docs/inverter.md): switch on Modbus and make the cable. | 20–40 min |
| 3 | [💾 **Install the software**](docs/install.md): put ESPHome on the D1 mini and add it to Home Assistant. | 20–30 min |
| 4 | [🏠 **Use the data**](docs/home-assistant.md): the Energy dashboard and automation ideas. | 10 min |

**Stuck?** [🩺 Troubleshooting](docs/troubleshooting.md) is organised by what you see.
**Curious?** [🧠 How it works](docs/how-it-works.md) explains Modbus, registers and the
choices in the configuration, [📑 Register reference](docs/registers.md) lists every
address, and the [📖 Glossary](docs/glossary.md) explains every technical word.

<a name="will-it-work-with-my-inverter"></a>

## 🔌 Will it work with my inverter?

| | Inverters | Notes |
|---|---|---|
| ✅ **Tested** | **X1 Boost G3** | Serial number usually starts with `XB3`, `XAU`, `XBE` or `XBU`. Tested on an `XB33…` with ESPHome 2026.9.1 and Home Assistant 2026.9. |
| 🤞 **Expected to work** | **X1 Mini G3** (serial `XM3…`), **X1 Air G3** | Not tested yet. The [SolaX Modbus integration](https://github.com/wills106/homeassistant-solax-modbus) reads all three with the same *register map* (the list of addresses where each value lives). Tried it? Please [tell us](https://github.com/benjaminvdb/esphome-solax-x1-boost/issues/new/choose) whether it worked, so this list can grow. |
| ❌ **No** | **Generation 4** (`XB4…` and similar), hybrid (battery) inverters, the X3 three-phase range | These use different addresses. Also not covered: inverters whose firmware doesn't offer Modbus and only speaks SolaX's own protocol. See the [SolaX Modbus integration](https://github.com/wills106/homeassistant-solax-modbus) or [syssi/esphome-solax-x1-mini](https://github.com/syssi/esphome-solax-x1-mini) instead. |

## 🦺 Safety, in short

> [!CAUTION]
> **Never open the inverter.** It contains high voltages, even after you switch it off.

You only plug a network cable into the inverter's **communication port**, the port meant
for meters and monitoring equipment. Is it behind a cover you aren't sure you may open?
Ask your installer. More in [Prepare the inverter and cable](docs/inverter.md#safety).

## 📜 History

I ([@benjaminvdb](https://github.com/benjaminvdb)) wrote the first version of this
configuration in **December 2022**, for my own X1 Boost. I couldn't find an ESPHome
configuration for this inverter using standard Modbus, so I worked out the addresses by
combining SolaX's documents for related inverters with reading out the inverter's registers
until the values made sense. I also
[asked about it](https://github.com/syssi/esphome-solax-x1-mini/issues/31) in the SolaX
RS485 community. I then contributed the configuration to
[aiolos/ESPHome-config](https://github.com/aiolos/ESPHome-config), the repository that
belongs to the Modbus shield I used ([pull request #2](https://github.com/aiolos/ESPHome-config/pull/2),
merged 21 December 2022), where it still lives as
[`modbus-solax.yaml`](https://github.com/aiolos/ESPHome-config/blob/main/modbus-solax.yaml).
In February 2023, syssi based the
[X1 Boost Modbus example](https://github.com/syssi/esphome-solax-x1-mini/blob/main/modbus-examples/esp32-solax-x1-boost.yaml)
in his project on it.

This repository is the next version: with the official SolaX register document, it fixes
the lifetime total (which fell back to 0 after 6,553.5 kWh) and adds fault reporting,
safer readings and a guide for beginners. See the [changelog](CHANGELOG.md).

## 🙏 Credits

- **aiolos / [enri.nl](https://enri.nl/pcb/?page=modbus)** for the Modbus shield PCB this
  project started on, and for hosting the first version of the configuration.
- **[syssi](https://github.com/syssi/esphome-solax-x1-mini)** for the SolaX RS485 work and
  the RJ45 pinout.
- **[wills106](https://github.com/wills106/homeassistant-solax-modbus)** and contributors
  for the register research and for sharing the official SolaX protocol document.

## 📄 License

The configuration and scripts are [MIT](LICENSE). The documentation and images are
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): share and adapt them, with
credit.

**Questions, ideas or improvements are welcome!** See [CONTRIBUTING.md](CONTRIBUTING.md).
