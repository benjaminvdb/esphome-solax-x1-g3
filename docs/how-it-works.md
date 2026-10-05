# 🧠 How it works

You don't need this page to build the project. It's for when you're curious, or want to
change something in the configuration.

## 📨 Modbus in one minute

Modbus is a simple, decades-old way for one device to ask another for numbers. The
inverter keeps its measurements in numbered slots called registers, and each register
holds a whole number between 0 and 65,535. The D1 mini sends a request along the lines
of "device 1, please send me registers 0x400 to 0x428", and the inverter replies with
those numbers.

Register numbers are usually written in hexadecimal (base 16), with `0x` in front:
`0x400` is 1024 in everyday numbers. SolaX publishes which register holds what in a
protocol document; the [register reference](registers.md) has the table.

Most values need a small conversion. The inverter stores 230.5 volts as `2305`, for
example, so the configuration multiplies by 0.1. That's what the `multiply: 0.1` lines
do.

## 📡 RS485

The Modbus messages travel over RS485, which uses two wires, A and B, and sends each bit
as the difference in voltage between them. Interference tends to affect both wires
equally, so the difference survives, and that's why RS485 copes well with long cables.
Only one side can talk at a time, which is why the D1 mini uses pin D5 to tell the
module whether to talk or listen.

<a name="the-lifetime-total"></a>

## 🔢 The lifetime total

The lifetime production can grow past 65,535 tenths of a kWh, so SolaX spreads it over
two registers: `0x423` holds the low part and `0x424` the high part. The full value is
high × 65,536 + low. ESPHome calls this format `U_DWORD_R`, an unsigned 32-bit number
from two registers with the low part first.

My first version of this config, from 2022, read only `0x423`. That works until the total
passes 6,553.5 kWh, and then it falls back to 0. Home Assistant sees the lower number,
assumes a new meter was installed and keeps counting, so the Energy dashboard still looks
right, but the total on its own is wrong. When you switch to this configuration, the total
jumps up to the real value once and Home Assistant counts that jump as production. The
[troubleshooting page](troubleshooting.md#the-energy-dashboard-shows-a-huge-spike) shows
how to remove that spike.

### Why the total is ignored while the inverter starts up

While the inverter is waking up it can answer with 0 for a moment. Home Assistant would
treat a drop to 0 as a new meter, and the return to the real value as a huge burst of
production. So the configuration only passes the total on when Run Mode is Normal, and
never passes on exactly 0. The
[SolaX Modbus integration](https://github.com/wills106/homeassistant-solax-modbus) uses a
similar rule.

<a name="one-request-instead-of-six"></a>

## 📦 One request instead of six

There are gaps of unused registers between the ones this configuration reads. By default,
ESPHome sends a separate request for each group, six per update. The setting
`reuse_previous_range: true` makes it read straight across the gaps, so a single request
fetches everything from `0x400` to `0x428`. That's quicker, and all values come from the
same moment, so Run Mode and Production Total always belong together. The protocol
document marks the registers in the gaps as reserved, and the inverter answers them
without complaint.

## ⏳ Timing

SolaX's protocol document says to wait at most 1 second for an answer and to leave at
least 1 second between two requests. The `send_wait_time` and `turnaround_time` settings
in the `modbus:` section do exactly that. The D1 mini asks for new values every 15
seconds (`update_interval`).

## 🌙 At night

When the panels stop producing, the inverter switches off and stops answering. After a
few attempts ESPHome marks it as offline, sets Run Mode to Offline, and from then on only
checks once a minute (`offline_skip_updates: 3`). The other sensors keep their last value
until the inverter wakes up again.

That's when the D1 mini runs on a phone charger. Powered from the inverter's USB port, it
switches off along with the inverter, and Home Assistant shows its sensors as unavailable
overnight. Home Assistant leaves unavailable values out of its statistics, so the Energy
dashboard isn't affected.

## 🚨 Faults

Registers `0x427` and `0x428` together hold 32 on/off flags, one for each type of fault.
The Fault sensor turns the flags that are on into the names from SolaX's document, such
as `GridVolt, Isolation`, or shows None.

## 🔒 Security

The connection between the D1 mini and Home Assistant is encrypted with your
`api_encryption_key`. Firmware updates over Wi-Fi use the same key (`ota: encryption:`),
so nobody else on your network can read your Wi-Fi password from an update. And when the
D1 mini can't reach your Wi-Fi, the fallback network it opens is protected with your
`fallback_password`.
