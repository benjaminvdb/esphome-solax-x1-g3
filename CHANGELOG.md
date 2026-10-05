# 📝 Changelog

## 1.0.0 (2026-10-05)

First release of this repository. It builds on the configuration I wrote in 2022, which
lives in [aiolos/ESPHome-config](https://github.com/aiolos/ESPHome-config/blob/main/modbus-solax.yaml).

### Fixed

- Production Total and Production Today are read as 32-bit values (`U_DWORD_R`). The
  total used to fall back to 0 after 6,553.5 kWh.
- Production Total is ignored while the inverter starts up and is never reported as 0,
  so the Energy dashboard no longer gets false spikes.

### Added

- A Fault sensor that names the faults the inverter reports.
- Run Mode shows Offline at night, and the D1 mini then checks only once a minute.

### Changed

- All registers are read in one Modbus request, with the timings from SolaX's protocol
  document.
- The API and firmware updates are encrypted. This needs ESPHome 2026.9.0 or newer.
- Total DC Power uses ESPHome's built-in `combination` sensor.
