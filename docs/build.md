# 🔧 Step 1: Build the circuit

Here you connect the RS485 module to the Wemos D1 mini. The inverter cable comes later,
in [step 2](inverter.md), so you can do this at your desk. It takes 15 to 30 minutes and
you need the D1 mini, the RS485 module and six jumper wires.

> [!IMPORTANT]
> Keep the D1 mini unplugged from USB while you connect wires. Everything runs on 3.3
> volts, so it isn't dangerous, but a loose wire on the wrong pin can damage a board.

## 💡 Why two boards?

The D1 mini sends and receives data as 3.3-volt pulses, with one wire for each direction.
The inverter speaks RS485 instead: it sends data over a pair of wires as the difference
between them, which keeps the signal clean over long cables. The RS485 module translates
between the two.

The inverter uses the same pair of wires for talking and listening, so the module also
needs to know which of the two it should do. A third wire from the D1 mini, which I'll
call the send/receive switch, takes care of that.

<a name="which-rs485-module"></a>

## 🛒 Which RS485 module?

You'll come across two kinds. Both are a small board with a chip, a row of pins on each
side and a screw terminal marked A and B, and both have the same pin names, so the wiring
is the same.

A MAX3485 or SP3485 module is the best fit. It's made for 3.3 volts, like the D1 mini.

The blue MAX485 module is easier to find. Its chip is officially specified for 5 volts,
but I run mine at 3.3 V without problems, and so do many others: a short cable at 9600
bits per second doesn't ask much of it.

Whichever you buy, power it from the D1 mini's 3V3 pin and not from 5V. At 5 volts the
module would send 5-volt signals back into the D1 mini, which is built for 3.3.

The blue module already has a handful of tiny resistors on it. Four keep its pins at a
defined level when nothing drives them, two hold A and B in a known state while nobody
is talking, and one 120 Ω resistor between A and B (often labelled R7) stops signals
from echoing at the end of the cable. Leave them all where they are. R7 belongs at each
end of an RS485 cable, and with only the inverter and your module on it, your module is
one of the ends.

## 🔌 Connect the wires

Hold the D1 mini with the Wi-Fi chip at the top and the USB socket at the bottom. Its
pins are then in the same order as in the diagram.

![Wiring diagram](../images/wiring.svg)

| RS485 module | D1 mini | What the wire does |
|---|---|---|
| VCC | 3V3 | Powers the module with 3.3 volts. |
| GND | GND | Ground, the shared 0-volt reference. |
| DI | D7 | Carries data from the D1 mini into the module (DI stands for *driver input*). |
| RO | D6 | Carries data from the module to the D1 mini (*receiver output*). |
| DE | D5 | Tells the module to talk (*driver enable*). |
| RE | D5 | Tells the module to listen (*receiver enable*). |

DE and RE both go to D5. The easiest way is to connect DE to RE on the module with a
short wire or a small blob of solder, then run one wire from either of them to D5. When
ESPHome sets D5 high, the module talks; when it sets it low, the module listens.

### ✅ Check your work

- [ ] Five pins on the D1 mini are in use: D5, D6, D7, 3V3 and GND.
- [ ] On the module, VCC, GND, DI, RO, DE and RE are connected, with DE and RE joined.
- [ ] The screw terminal is still empty. That's where the inverter cable goes.

Two mistakes are easy to make. D6 and D7 get swapped because the names look so alike;
if the inverter never answers later, swap them back, which can't damage anything. And
the 5V pin sits next to GND on the right-hand side, while 3V3 is at the bottom left. The
module's VCC wire belongs on 3V3.

## 🪛 Solder or not?

Jumper wires are fine for trying things out, but they can work loose over the years, so
for something that will hang on a wall soldering is more reliable. Most D1 minis come
with pin headers you solder on yourself; if yours already has them, you can start with
jumper wires and no soldering at all. For a sturdier build, solder both boards onto a
small piece of perfboard (board with holes) with short wires.

I started on the [enri.nl Modbus Shield](https://enri.nl/pcb/?page=modbus), a printed
board with sockets for the D1 mini and a MAX485 module. It uses exactly this wiring, at
3.3 V, on D5, D6 and D7. It makes for a tidy build, but you don't need it.

<details>
<summary>Optional: two protective resistors (the dashed boxes in the diagram)</summary>

<br>

The enri.nl shield has a 1 kΩ resistor (bands: brown, black, red) in the DI wire and
another in the RO wire. You can add them too: cut the wire and put the resistor in
between, so the signal passes through it.

While everything is wired and configured correctly, they do nothing; at 9600 bits per
second the signal doesn't notice them. They come into play when both sides send on the
same wire at once, which happens if D6 and D7 are swapped in the configuration or for a
moment while the D1 mini starts up. The resistors then limit the current to a few
milliamps, which can't damage anything.

They won't make a module powered from 5 V safe. Its RO pin would still put 5 volts on the
D1 mini, and the ESP8266 datasheet allows at most 3.6 V on a pin. They also don't protect
the cable side against static or lightning surges. For a short cable indoors that's
rarely a concern; for a long or outdoor cable, use an isolated RS485 module (see
[Safety](inverter.md#safety)).

</details>

## 📦 Put it in a box

A small plastic project box next to the inverter works well, with the network cable and
a short USB cable from the inverter's USB port coming in through a hole. Keep it dry and out of direct sun. If the
inverter is outside, put the D1 mini indoors and run a longer network cable to it.

Next: [Step 2: Prepare the inverter and cable](inverter.md)
