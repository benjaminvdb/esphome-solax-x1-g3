# 🩺 Troubleshooting

Look for what you're seeing in the headings below. To read the device's log, open
ESPHome Builder, find the solax device and click **Logs**.

> [!TIP]
> Most problems come down to one of three things: it's night and the inverter is off,
> Modbus isn't switched on in the inverter, or two wires are swapped. Swapping wires in
> this project can't damage anything, so it's safe to try.

## 📵 Nothing shows up in Home Assistant

First check whether the D1 mini is on your Wi-Fi: is it marked Online in ESPHome
Builder? If not, look on your phone for a Wi-Fi network called solax-fallback. If it's
there, the D1 mini can't reach your network. Connect to solax-fallback (the password is
your `fallback_password`) and a page opens where you can enter the right Wi-Fi details.

The D1 mini only works with 2.4 GHz Wi-Fi. Most routers offer 2.4 and 5 GHz, sometimes
under one name, so this is rarely the problem, but it's worth knowing.

If the device is online but missing from Home Assistant, look under **Settings → Devices
& services** for a Discovered card. You can also add it by hand: **Add integration →
ESPHome**, with `solax.local` as the host.

## 🔇 The log says `Stop waiting for response` or `set offline`

The D1 mini asks the inverter for data and gets no answer. Go through these in order:

1. Is it daytime? At night the inverter is off and these messages are normal. The D1 mini
   then only checks once a minute.
2. Is Modbus switched on in the inverter, with address 1 and speed 9600? See
   [step 2](inverter.md#1-switch-on-modbus-in-the-inverter).
3. Swap A and B on the module's screw terminal.
4. Swap the wires on D6 and D7.
5. Check the cable: is the plug in the RS485/Meter port, and are the blue and white-blue
   wires (pins 4 and 5) the ones you connected?
6. Check that DE and RE both connect to D5.

## 🚫 The log says `Modbus error … exception: 2`

The inverter answers, but refuses one of the requests ("illegal data address"). That can
mean different firmware or a different model, so check
[Will it work with my inverter?](../README.md#will-it-work-with-my-inverter) first.

If it is a G3 model, please [open an issue](https://github.com/benjaminvdb/esphome-solax-x1-g3/issues/new/choose)
with the full log line. The configuration
[reads several registers in one go](how-it-works.md#one-request-instead-of-six), and
removing `reuse_previous_range: true` from the sensor right after the address in the
message usually fixes this.

## 🤔 The values look wrong

If Production Total is far too low, or dropped to 0 at some point, you're probably still
running an old configuration that reads the total as a 16-bit number. Switch to the
current `solax-x1.yaml`; [How it works](how-it-works.md#the-lifetime-total) explains why.

Production Total not updating early in the morning is intentional. It only updates once
Run Mode is Normal, because the inverter can report 0 while it starts up.

Small differences in temperature, voltage or power compared to other meters are normal.
The values come straight from the inverter, so compare them with its own display.

<a name="the-energy-dashboard-shows-a-huge-spike"></a>

## 📈 The Energy dashboard shows a huge spike

Home Assistant counts every increase of Production Total as production. When the total
jumps, for example after switching from an old configuration, or when an old
configuration briefly reported 0, you get a spike. To fix the history:

1. Go to **Settings → Tools → Statistics**. In older versions this is under Developer
   tools.
2. Find Solax Production Total and click the adjust icon at the end of its row.
3. Pick the date and time of the spike, select the entry with the huge value, and enter
   the real production for that period: a fraction of a kWh, or 0.

## 🔌 Installing over USB doesn't work

Use Chrome or Edge, because other browsers can't talk to USB serial devices. Try another
USB cable, since many cables only charge. On Windows, cheap D1 mini clones may need the
CH340 driver. If none of that helps, choose **Manual download** and install the file with
[web.esphome.io](https://web.esphome.io/).

## 🙋 Still stuck?

[Open an issue](https://github.com/benjaminvdb/esphome-solax-x1-g3/issues/new/choose).
The form asks for your inverter model, the first three characters of its serial number,
the firmware version, which RS485 module you used, and about a minute of the device log.
That's usually enough for me to help.
