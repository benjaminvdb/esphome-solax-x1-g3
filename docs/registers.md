# Register reference

Source: *SolaX Power X1-BOOST Single phase inverter Modbus-RTU comms protocol V1.0
(public version)*, shared by the community in
[wills106/homeassistant-solax-modbus#327](https://github.com/wills106/homeassistant-solax-modbus/discussions/327).
The document covers the X1 Boost (generation 3). The SolaX Modbus integration uses the
same map for the X1 Mini G3 and X1 Air G3.

Communication: Modbus RTU over RS485, 9600 baud, 8 data bits, no parity, 1 stop bit,
device address 1 by default. Response timeout 1 s; at least 1 s between requests.

## Input registers (function code 0x04), used by this project

| Register | Name | Unit | Type | Sensor |
|---|---|---|---|---|
| 0x400 | Vdc1 | 0.1 V | uint16 | PV1 Input Voltage |
| 0x401 | Vdc2 | 0.1 V | uint16 | PV2 Input Voltage |
| 0x402 | Idc1 | 0.1 A | uint16 | PV1 Input Current |
| 0x403 | Idc2 | 0.1 A | uint16 | PV2 Input Current |
| 0x404 | Vac | 0.1 V | uint16 | Grid Voltage |
| 0x407 | Fac | 0.01 Hz | uint16 | Grid Frequency |
| 0x40A | Iac | 0.1 A | uint16 | Output Current |
| 0x40D | INVTemperatureDeg | 1 °C | uint16 | Temperature |
| 0x40E | Pac | 1 W | uint16 | Inverter Power |
| 0x40F | RunMode | – | uint16 | Run Mode |
| 0x414 | Pdc1 | 1 W | uint16 | Power DC1 |
| 0x415 | Pdc2 | 1 W | uint16 | Power DC2 |
| 0x423 / 0x424 | YieldTotal (low / high) | 0.1 kWh | uint32, low word first | Production Total |
| 0x425 / 0x426 | YieldToday (low / high) | 0.1 kWh | uint32, low word first | Production Today |
| 0x427 / 0x428 | Inverter_FaultMessage (low / high) | bit flags | uint32, low word first | Fault |

## Other documented input registers

| Register | Name | Unit |
|---|---|---|
| 0x416 | GridVoltFaultValue | 0.1 V |
| 0x419 | GridFreqFaultValue | 0.01 Hz |
| 0x41C | DciFaultValue | 1 mA |
| 0x41F / 0x420 | Pv1VoltFaultValue / Pv2VoltFaultValue | 0.1 V |
| 0x421 | INVTemperatureDegFaultValue | 1 °C |
| 0x422 | GfciFaultValue | 1 mA |
| 0x42C | ENVTemperatureDeg (control board) | 1 °C |
| 0x42D | ENVTemperatureDegFaultValue | 1 °C |
| 0x42F | Manager_FaultMessage | bit flags |

All other registers between 0x400 and 0x434 are marked *reserved*.

## Holding registers (function code 0x03)

| Register | Name | Type |
|---|---|---|
| 0x300–0x306 | SeriesNumber | 14 characters |
| 0x307–0x30D | FactoryName | 14 characters |
| 0x30E–0x314 | ModuleName | 14 characters |

## Run Mode values

| Value | Mode |
|---|---|
| 0 | Wait |
| 1 | Check |
| 2 | Normal |
| 3 | Fault |
| 4 | Permanent Fault |

The configuration also names values 5–10 (from SolaX's hybrid inverters) in case newer
firmware uses them.

## Fault bits (0x427 = bits 0–15, 0x428 = bits 16–31)

| Bit | Fault | Bit | Fault |
|---|---|---|---|
| 0 | TzProtectFault | 16 | SpiCommsFault |
| 1 | MainsLostFault | 17 | SciCommsFault |
| 2 | GridVoltFault | 18 | *reserved* |
| 3 | GridFreqFault | 19 | InputConfigFault |
| 4 | PLLLostFault | 20 | EepromFault |
| 5 | BusVoltFault | 21 | RelayFault |
| 6 | ExportHardLimitFault | 22 | SampleConsistenceFault |
| 7 | Inv_OCP_Fault | 23 | ResidualCurrent_DeviceFault |
| 8 | Dci_OCP_Fault | 24 | GeneralHardLimitFault |
| 9 | ResidualCurrentFault | 25–28 | *reserved* |
| 10 | PvVoltFault | 29 | DCI_DeviceFault |
| 11 | Ac10Mins_Voltage_Fault | 30 | Other_DeviceFault |
| 12 | IsolationFault | 31 | *reserved* |
| 13 | TemperatureOverFault | | |
| 14 | *reserved* | | |
| 15 | EarthFault | | |

## RS485/Meter port (RJ45)

| Pin | Signal |
|---|---|
| 3 | GND_COM |
| 4 | 485_A |
| 5 | 485_B |

The other pins carry DRM, reference and emergency-stop signals; leave them unconnected.
The X1 Mini table in [syssi/esphome-solax-x1-mini](https://github.com/syssi/esphome-solax-x1-mini#x1-mini-rj45-connector)
also lists pin 7 as GND_COM, but the X1 Boost G3 manual doesn't, so this project uses pin 3.
