# How it works

You don't need this page to build the project. It explains what's going on underneath,
for when you're curious or want to change something.

## Modbus in one minute

**Modbus** is a simple, decades-old way for a controller to ask a device for numbers. The
inverter keeps its measurements in numbered slots called **registers**, each holding one
whole number between 0 and 65,535. The D1 mini sends a request like *"device 1, please
give me registers 0x400 to 0x428"*, and the inverter replies with those numbers.

Register numbers are usually written in **hexadecimal** (base 16), shown with `0x` in
front: `0x400` is 1024 in normal numbers. SolaX publishes which register holds what in a
protocol document; the table is in [Register reference](registers.md).

Most values need a small conversion. The inverter stores 230.5 volts as `2305`, so the
configuration multiplies by 0.1. That's what lines like `multiply: 0.1` do.

## RS485

The Modbus messages travel over **RS485**: two wires, A and B, carrying each bit as the
*difference* between them. Interference usually affects both wires equally, so the
difference survives, which is why RS485 works over long cables. Only one side may talk at
a time; the D5 pin tells the RS485 module whether to talk or listen.

## The lifetime total

The lifetime production can grow larger than 65,535 tenths of a kWh, so SolaX stores it
in **two** registers: `0x423` holds the low part and `0x424` the high part. The full value
is *high × 65,536 + low*. ESPHome calls this `U_DWORD_R`: an unsigned 32-bit number from
two registers, low part first.

The first published configuration for this inverter (from 2022, copied in a few places)
read only `0x423`. That works until the total passes 6,553.5 kWh; then it falls back to 0.
Home Assistant sees a lower number, treats it as a new meter, and keeps counting, so the
Energy dashboard looks fine, but the value on its own is wrong. If you switch to this
configuration, the total jumps up to the real value once, and Home Assistant counts that
jump as production. Remove that spike as described in
[Troubleshooting](troubleshooting.md#the-energy-dashboard-shows-a-huge-spike).

**Why the total is ignored outside *Normal* mode:** while the inverter wakes up, it can
answer with 0 for a moment. Home Assistant would treat a drop to 0 as a new meter, and the
return to the real value as a huge amount of production. So the configuration only passes
the total on when Run Mode is *Normal*, and never passes on exactly 0. The
[SolaX Modbus integration](https://github.com/wills106/homeassistant-solax-modbus) uses the
same rule.

## One request instead of six

The registers the configuration uses have gaps of unused registers between them. By
default, ESPHome would send a separate request for every group, six per update. The
setting `reuse_previous_range: true` tells ESPHome to read across the gaps, so one
request fetches everything from `0x400` to `0x428`. That's faster, and all values come
from the same moment. In particular, *Run Mode* and *Production Total* always belong
together. The protocol document lists the gap registers as *reserved*, and the inverter
answers them without complaint.

## Timing

The protocol document asks for at most 1 second to wait for an answer, and at least
1 second between two requests. The `modbus:` section sets exactly that
(`send_wait_time` and `turnaround_time`). The D1 mini asks for new values every 15
seconds (`update_interval`).

## At night

When the panels stop producing, the inverter switches off and stops answering. After a few
tries, ESPHome marks it offline, sets Run Mode to *Offline*, and from then on checks only
once a minute (`offline_skip_updates: 3`). The other values keep their last reading until
the inverter wakes up in the morning.

## Faults

Registers `0x427` and `0x428` together hold 32 on/off flags, one per fault type. The
*Fault* sensor turns the flags that are on into names from SolaX's document, for example
`GridVolt, Isolation`, or shows *None*.

## Security

- The connection between the D1 mini and Home Assistant is encrypted with your
  `api_encryption_key`.
- Firmware updates over Wi-Fi are encrypted with the same key (`ota: encryption:`), so
  nobody on your network can read your Wi-Fi password out of an update.
- If the D1 mini can't reach your Wi-Fi, it opens a fallback network protected with your
  `fallback_password`.
