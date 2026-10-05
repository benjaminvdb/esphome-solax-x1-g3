# Step 1: Build the circuit

In this step you connect the RS485 module to the Wemos D1 mini with six wires. The
inverter cable comes later, in [step 2](inverter.md). You don't need the inverter yet, so
you can do this at your desk.

**Time:** 15–30 minutes. **You'll need:** the D1 mini, the RS485 module and six jumper wires.

> **Before you start:** unplug the D1 mini from USB while you connect wires. Nothing here
> is dangerous (everything runs on 3.3 volts), but a wire touching the wrong pin while
> powered can damage a board.

## Why two boards?

The D1 mini talks in short pulses of 3.3 volts, one wire for sending and one for
receiving. The inverter talks **RS485**: it sends the same data over a *pair* of wires,
as the difference between them, which keeps the signal clean over long cables. The RS485
module translates between the two. Because the inverter's pair is used for both
directions, the module needs to know when to listen and when to talk; that's what the
"send/receive switch" wire is for.

## Which RS485 module?

You'll find two kinds. Both look like a small board with a chip, a row of pins on each
side, and a screw terminal marked A and B.

- **MAX3485 or SP3485 module (recommended):** made for 3.3 volts, the same as the
  D1 mini. It fits without any compromise.
- **Blue MAX485 module (very common):** its chip is officially designed for 5 volts. Many
  people, including the author, run it at 3.3 volts without problems, because receiving a
  short cable at 9600 bits per second asks very little of it. **Don't power it from 5 V**:
  its data output would then send 5 volts into the D1 mini, which is designed for 3.3.

Both modules have the same pin names, so the wiring below is identical.

## Connect the wires

Find the pin names printed on both boards. The D1 mini's pins are in the same order as in
the picture when you hold it with the Wi-Fi chip at the top and the USB socket at the
bottom.

![Wiring diagram](../images/wiring.svg)

| # | RS485 module | D1 mini | What it does |
|---|---|---|---|
| 1 | **VCC** | **3V3** | Power for the module (3.3 volts). |
| 2 | **GND** | **GND** | Ground, the shared 0-volt reference. Every part needs this. |
| 3 | **DI** | **D7** | Data *in* to the module: what the D1 mini sends. |
| 4 | **RO** | **D6** | Data *out* of the module: what the D1 mini receives. |
| 5 | **DE** | **D5** | "Driver enable": talk. |
| 6 | **RE** | **D5** | "Receiver enable": listen. DE and RE share one D1 mini pin. |

**Joining DE and RE:** both go to D5. With jumper wires, use a short wire from DE to RE on
the module itself (many people bend one wire's end to touch both pins, but a tiny bridge
of solder is more reliable), then one wire from either of them to D5. When D5 is high, the
module talks; when it's low, the module listens. ESPHome switches it for you.

> **Check:** count the wires on the D1 mini side: D5, D6, D7, 3V3 and GND, five pins in
> total. On the module: VCC, GND, DI, RO, DE and RE, with DE and RE joined. The screw
> terminal (A, B) stays empty for now.

### Common mistakes

- **D6 and D7 swapped.** The names are confusingly similar to the "TX/RX" on some
  modules. Follow the table: **DI ← D7** and **RO → D6**. If it doesn't work later,
  swapping these two is the first thing to try; it can't damage anything.
- **5V instead of 3V3.** The D1 mini also has a 5V pin, right next to GND on the other
  side. Use **3V3**.

## Solder or not?

Jumper wires are fine to test. For something that will hang on a wall for years,
soldering is more reliable: jumper wires can work loose. Some options:

- **Pin headers and jumper wires:** most D1 minis come with headers that need soldering
  on. If yours came with headers already attached, you need no soldering at all.
- **A small piece of perfboard** (board with holes) with both boards and short wires.
- **A ready-made shield:** the [enri.nl Modbus Shield](https://enri.nl/pcb/?page=modbus)
  this project started on is a printed board with sockets for the D1 mini and a MAX485
  module, using exactly these pins (D5, D6 and D7). It adds two 1 kΩ resistors on the data
  lines. It makes tidy connections, but it isn't required: the wiring above does the same
  job.

## Put it in a box

Keep the boards dry and out of direct sun, for example in a small plastic project box
next to the inverter, with the network cable and USB cable entering through a hole. If the
inverter is outside, put the D1 mini indoors and run a longer network cable to it.

**Next:** [Step 2: Prepare the inverter and cable](inverter.md)
