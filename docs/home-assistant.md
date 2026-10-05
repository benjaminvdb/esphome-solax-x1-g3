# Step 4: Use the data in Home Assistant

## The Energy dashboard

1. Go to **Settings → Dashboards → Energy** (or open **Energy** in the sidebar and follow
   the setup).
2. Under **Solar panels**, add **Solax Production Total** as the solar production sensor.

Use *Production Total*, not *Production Today*. The total only ever goes up, which is
exactly what the Energy dashboard expects; it works out the daily, weekly and monthly
amounts by itself.

> **You should now see** solar production appear in the Energy dashboard after an hour or
> so: Home Assistant collects energy statistics once per hour.

## What the sensors mean

- **Inverter Power** is what the inverter delivers to your home and the grid (AC).
  **Total DC Power** is what comes in from the panels. The difference, usually 2–4%, is
  the inverter's own loss.
- **Power DC1 / DC2** and the **PV1 / PV2** voltages and currents are the two panel
  *strings* (groups of panels wired together). Comparing them is a quick way to spot a
  shaded or dirty string.
- **Run Mode** is what the inverter is doing: *Waiting* and *Checking* in the morning,
  *Normal* while producing, *Fault* when something is wrong, and *Offline* at night, when
  the inverter switches itself off.
- **Fault** shows *None*, or the name of each fault the inverter reports, such as
  `GridVolt` (grid voltage out of range) or `Isolation` (a possible wiring or moisture
  problem on the panel side). The names come from SolaX's protocol document. It's under
  the device's diagnostic entities.

## Ideas for automations

- **Get a notification on a fault:** trigger when *Solax Fault* changes to anything other
  than `None`.
- **Use surplus solar power:** start the dishwasher or charge the car when *Inverter
  Power* stays above a threshold for 10 minutes.
- **Check the panels:** notify when *Power DC1* and *Power DC2* differ a lot at midday on
  a sunny day.

## A note on the totals

The lifetime total is stored in the inverter in tenths of a kWh, as a 32-bit number
(two Modbus registers). Older configurations read only the first of those registers, so
their total jumped back to 0 after 6,553.5 kWh. This configuration reads both, and also
ignores readings taken while the inverter is starting up, which can briefly be 0. See
[How it works](how-it-works.md#the-lifetime-total) for details, including how to clean up
Home Assistant's statistics if you're coming from an older configuration.
