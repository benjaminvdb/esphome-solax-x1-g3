# 🏠 Step 4: Use the data in Home Assistant

## ⚡ The Energy dashboard

Go to **Settings → Dashboards → Energy** (or open Energy in the sidebar and follow the
setup). Under Solar panels, add **Solax Production Total** as the solar production sensor.

Pick Production Total rather than Production Today. The Energy dashboard wants a number
that only ever goes up, and it works out the daily, weekly and monthly amounts by itself.

You should now see solar production in the Energy dashboard within an hour or so. Home
Assistant collects energy statistics once an hour.

## 📊 What the sensors mean

Inverter Power is what the inverter delivers to your house and the grid. Total DC Power
is what comes in from the panels. The difference between the two, usually 2 to 4
percent, is lost as heat in the inverter.

Power DC1 and DC2, and the PV1 and PV2 voltages and currents, belong to the two panel
strings (groups of panels wired in a row). On a sunny day you can compare them to spot a
string that's shaded or dirty.

Run Mode shows what the inverter is up to: Waiting and Checking in the morning, Normal
while it's producing, Fault when something is wrong, and Offline at night when it has
switched itself off.

Fault shows None, or the name of each fault the inverter reports. `GridVolt`, for
example, means the grid voltage was out of range, and `Isolation` points to a possible
wiring or moisture problem on the panel side. You'll find it among the device's
diagnostic entities.

## 🤖 Automation ideas

- Send yourself a notification when Solax Fault changes to anything other than `None`.
- Start the dishwasher, or charge the car, when Inverter Power has been above a certain
  level for 10 minutes.
- Get a warning when Power DC1 and DC2 differ a lot around midday on a sunny day.

## 🔢 About the totals

The inverter keeps its lifetime total in tenths of a kWh, as a 32-bit number spread over
two Modbus registers. Older configurations read only one of the two, so their total went
back to 0 after 6,553.5 kWh. This configuration reads both. It also ignores readings
taken while the inverter is starting up, because those can briefly be 0.

If you're switching over from an older configuration, [How it works](how-it-works.md#the-lifetime-total)
explains what happens to your history and how to clean it up.
