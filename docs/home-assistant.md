# 🏠 Step 4: Use the data in Home Assistant

Your inverter is now in Home Assistant. This page shows how to put it on the Energy
dashboard, what each sensor means, and some ideas for automations.

## ⚡ The Energy dashboard

1. Go to **Settings → Dashboards → Energy** (or open **Energy** in the sidebar and follow
   the setup).
2. Under **Solar panels**, add **Solax Production Total** as the solar production sensor.

**Use *Production Total*, not *Production Today*.** The total only ever goes up, which is
exactly what the Energy dashboard expects; it works out the daily, weekly and monthly
amounts by itself.

**✅ You should now see** solar production in the Energy dashboard within an hour or so.
Home Assistant collects energy statistics once per hour.

## 📊 What the sensors mean

| Sensor | What it tells you |
|---|---|
| **Inverter Power** | What the inverter delivers to your home and the grid (AC). |
| **Total DC Power** | What comes in from the panels. The difference with *Inverter Power*, usually 2–4%, is the inverter's own loss. |
| **Power DC1 / DC2**, **PV1 / PV2** voltage and current | The two panel *strings* (groups of panels wired together). Comparing them is a quick way to spot a shaded or dirty string. |
| **Production Today** / **Production Total** | Energy produced today, and in the inverter's whole life. |
| **Grid Voltage**, **Grid Frequency**, **Output Current** | The electricity grid as the inverter sees it. |
| **Temperature** | Inside the inverter. |
| **Run Mode** | *Waiting* and *Checking* in the morning, *Normal* while producing, *Fault* when something is wrong, and *Offline* at night, when the inverter switches itself off. |
| **Fault** | *None*, or the name of each fault the inverter reports. For example, `GridVolt` means the grid voltage was out of range, and `Isolation` a possible wiring or moisture problem on the panel side. You'll find it under the device's *diagnostic* entities. |

## 🤖 Ideas for automations

- **Get a notification on a fault:** trigger when *Solax Fault* changes to anything other
  than `None`.
- **Use surplus solar power:** start the dishwasher or charge the car when *Inverter
  Power* stays above a threshold for 10 minutes.
- **Keep an eye on the panels:** notify when *Power DC1* and *Power DC2* differ a lot at
  midday on a sunny day.

## 🔢 A note on the totals

The lifetime total is stored in the inverter in tenths of a kWh, as a 32-bit number
spread over two Modbus registers. Older configurations read only the first of those
registers, so their total jumped back to 0 after 6,553.5 kWh. This configuration reads
both, and also ignores readings taken while the inverter is starting up, which can briefly
be 0.

Coming from an older configuration? See
[How it works](how-it-works.md#the-lifetime-total) for details, including how to clean up
Home Assistant's statistics.
