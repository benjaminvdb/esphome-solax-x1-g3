# 📝 Changelog

## 🚀 1.0.0 — 2026-10-05

First release in this repository. Compared to the
[2022 configuration](https://github.com/aiolos/ESPHome-config/blob/main/modbus-solax.yaml),
which @benjaminvdb wrote and contributed to aiolos/ESPHome-config
([pull request #2](https://github.com/aiolos/ESPHome-config/pull/2)):

- **Fixed:** Production Total and Production Today are read as 32-bit values
  (`U_DWORD_R`). Before, the total fell back to 0 after 6,553.5 kWh.
- **Fixed:** Production Total is ignored while the inverter starts up (Run Mode not
  *Normal*) and never reports 0, so the Energy dashboard gets no false spikes.
- **New:** *Fault* sensor that names active inverter faults.
- **New:** Run Mode shows *Offline* at night, and the D1 mini then checks only once a minute.
- **Changed:** all registers are read in one Modbus request, with the timings from
  SolaX's protocol document.
- **Changed:** encrypted API and encrypted firmware updates. Needs ESPHome 2026.9.0 or newer.
- **Changed:** Total DC Power uses ESPHome's built-in `combination` sensor.
