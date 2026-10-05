# Troubleshooting

Find what you see in the headings below. To read the device's log, open **ESPHome
Builder**, find the *solax* device and click **Logs**.

Most problems are one of three things: the inverter isn't on (it's night), Modbus isn't
enabled in the inverter, or two wires are swapped. Swapping wires on this project can't
damage anything, so it's safe to try.

## Nothing appears in Home Assistant at all

- **Is the D1 mini on Wi-Fi?** In ESPHome Builder, is the device marked *Online*? If not,
  look for a Wi-Fi network called **solax-fallback** on your phone. If you see it, the
  D1 mini can't reach your Wi-Fi: connect to *solax-fallback* (password: your
  `fallback_password`), and a page opens where you can enter the right Wi-Fi details.
- **Is your Wi-Fi 2.4 GHz?** The D1 mini can't use 5 GHz networks. Most routers offer
  both, sometimes under one name.
- **Did Home Assistant discover it?** Check **Settings → Devices & services** for a
  *Discovered* card, or add it manually: **Add integration → ESPHome**, host `solax.local`.

## The log shows `Stop waiting for response` or `set offline`

The D1 mini asks the inverter for data but gets no answer.

1. **Is it daytime?** The inverter switches off when the panels don't produce. At night
   these messages are normal and the device only checks once a minute.
2. **Is Modbus enabled** in the inverter, with address **1** and speed **9600**? See
   [step 2](inverter.md#1-switch-on-modbus-in-the-inverter).
3. **Swap A and B** on the RS485 module's screw terminal.
4. **Swap the wires on D6 and D7.**
5. **Check the cable:** is the plug in the **RS485/Meter** port, and are you using
   pins 4 and 5 (blue and white-blue)?
6. **Check DE and RE:** both must connect to D5.

## The log shows `Modbus error … exception: 2`

The inverter answers but refuses one of the requests ("illegal data address"). Your
inverter may have different firmware or be a different model. Check
[Will it work with my inverter?](../README.md#will-it-work-with-my-inverter). If it's a
G3 model, open an issue with the full log line; the
[configuration reads several registers in one go](how-it-works.md#one-request-instead-of-six),
and removing `reuse_previous_range: true` from the sensor just after the address in the
message usually fixes it.

## Values appear, but they look wrong

- **Production Total far too low, or it dropped to 0 once:** you're probably using an old
  configuration that reads the total as a 16-bit number. Use the current
  `solax-x1.yaml`; see [How it works](how-it-works.md#the-lifetime-total).
- **Production Total doesn't update in the morning:** that's on purpose. It only updates
  when Run Mode is *Normal*, because the inverter can report 0 while starting up.
- **Temperature, voltage or power seem a bit off:** compare with the inverter's own
  display. The values come straight from the inverter, so small differences with other
  meters are normal.

## The Energy dashboard shows a huge spike

Home Assistant counts every increase of *Production Total* as production. A spike happens
when the total jumps, for example when you switch from an old configuration, or when
an old configuration briefly reported 0. To fix the history:

1. Go to **Settings → Tools → Statistics** (called *Developer tools → Statistics* in older
   versions).
2. Find *Solax Production Total* and click the adjust icon on its row.
3. Pick the date and time of the spike, select the entry with the huge value, and enter
   the real production for that period (a fraction of a kWh, or 0).

## Installing over USB doesn't work

- Use **Chrome or Edge**; other browsers can't talk to USB serial devices.
- Try another USB cable: many cables only charge.
- On Windows, you may need the CH340 driver for clone D1 minis.
- Use **Manual download** and [web.esphome.io](https://web.esphome.io/) instead.

## Still stuck?

Open an [issue](https://github.com/benjaminvdb/solax-esphome/issues/new/choose) and include: your inverter model and serial
number prefix (the first three characters, e.g. `XB3`), the inverter's firmware version,
which RS485 module you used, and the device log from about one minute after it starts.
