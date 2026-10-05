# 🔧 Step 1: Build the circuit

In this step you connect the RS485 module to the Wemos D1 mini. The inverter cable comes
later, in [step 2](inverter.md), so you can do this at your desk.

| | |
|---|---|
| ⏱️ **Time** | 15–30 minutes |
| 🧰 **You'll need** | the D1 mini, the RS485 module and six jumper wires |
| 🎯 **Result** | two boards connected with six wires, ready for the inverter cable |

> [!IMPORTANT]
> **Unplug the D1 mini from USB while you connect wires.** Nothing here is dangerous
> (everything runs on 3.3 volts), but a wire touching the wrong pin while powered can
> damage a board.

## 💡 Why two boards?

- The **D1 mini** talks in short pulses of 3.3 volts: one wire for sending, one for
  receiving.
- The **inverter** talks **RS485**: it sends data over a *pair* of wires, as the
  difference between them. That keeps the signal clean, even over long cables.
- The **RS485 module** translates between the two. The inverter uses its pair of wires
  for both directions, so the module also needs to know when to listen and when to talk.
  That's the job of the *send/receive switch* wire.

<a name="which-rs485-module"></a>

## 🛒 Which RS485 module?

You'll find two kinds. Both are a small board with a chip, a row of pins on each side and
a screw terminal marked **A** and **B**. They have the same pin names, so the wiring is
identical.

| Module | Made for | Verdict |
|---|---|---|
| **MAX3485** or **SP3485** | 3.3 volts, like the D1 mini | ✅ **Recommended.** Fits without any compromise. |
| Blue **MAX485** (very common) | 5 volts, officially | 👍 **Works.** Many people, including the author, run it at 3.3 volts without problems: a short cable at 9600 bits per second asks very little of it. |

**Don't power any module from 5 V.** Its data output would then send 5 volts into the
D1 mini, which is built for 3.3.

**The tiny parts already on the module:** the blue module carries a few resistors of its
own. Four keep its pins at a defined level when nothing drives them, two keep A and B in a
known state while nobody is sending, and one of 120 Ω between A and B (often labelled
*R7*) stops signals echoing at the end of the cable. **Leave them all in place.** R7
belongs at each *end* of an RS485 cable, and with only the inverter and your module on
the cable, your module is an end.

## 🔌 Connect the wires

Find the pin names printed on both boards. Hold the D1 mini with the Wi-Fi chip at the
top and the USB socket at the bottom: its pins are then in the same order as in the
picture.

![Wiring diagram](../images/wiring.svg)

| # | RS485 module | D1 mini | What it does |
|:-:|---|---|---|
| 1 | **VCC** | **3V3** | Power for the module (3.3 volts). |
| 2 | **GND** | **GND** | Ground: the shared 0-volt reference. Every part needs this. |
| 3 | **DI** | **D7** | Data *in* to the module: what the D1 mini sends. |
| 4 | **RO** | **D6** | Data *out* of the module: what the D1 mini receives. |
| 5 | **DE** | **D5** | *Driver enable*: talk. |
| 6 | **RE** | **D5** | *Receiver enable*: listen. DE and RE share one D1 mini pin. |

### Joining DE and RE

Both go to **D5**. With jumper wires:

1. Connect **DE** to **RE** on the module itself, with a short wire or a tiny bridge of
   solder.
2. Run one wire from either of them to **D5**.

When D5 is high, the module talks; when it's low, the module listens. ESPHome switches
it for you.

### ✅ Check your work

- [ ] On the D1 mini, exactly five pins are used: **D5, D6, D7, 3V3** and **GND**.
- [ ] On the module: **VCC, GND, DI, RO, DE** and **RE**, with DE and RE joined.
- [ ] The screw terminal (**A**, **B**) is still empty. It's for the inverter cable.

### Common mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| **D6 and D7 swapped** | Later, the inverter never answers. | Follow the table: **DI ← D7**, **RO → D6**. Swapping them back can't damage anything. |
| **5V instead of 3V3** | The power wire sits next to **GND** on the right-hand side. | Move it to **3V3**, on the left-hand side. |

## 🪛 Solder or not?

Jumper wires are fine for testing. For something that will hang on a wall for years,
soldering is more reliable, because jumper wires can work loose.

| Option | Soldering | Notes |
|---|---|---|
| **Pin headers + jumper wires** | Only the headers, if they aren't attached yet | Quickest to start with. |
| **Perfboard** (a board with holes) | Yes | Both boards and short wires on one board; tidy and sturdy. |
| **[enri.nl Modbus Shield](https://enri.nl/pcb/?page=modbus)** | Headers only | A printed board with sockets for the D1 mini and a MAX485 module, with exactly this wiring (3.3 V, D5, D6, D7). This project started on it. Tidy, but not required. |

<details>
<summary><b>Optional: two protective resistors</b> (the dashed boxes in the diagram)</summary>

<br>

The enri.nl shield adds a 1 kΩ resistor (bands: brown, black, red) in the **DI** wire and
another in the **RO** wire. You can do the same: put the resistor in the middle of the
wire, *in series*, so the signal passes through it.

**What they do:**

- **While everything is right, nothing.** At 9600 bits per second the signal doesn't
  notice them.
- **When two sides send on the same wire at once, they limit the current** to a few
  thousandths of an ampere, which can't damage anything. That can happen if D6 and D7
  are swapped in the configuration, or for a moment while the D1 mini starts up.

**What they don't do:**

- **They don't make a 5-volt module safe.** Powered from 5 V, a MAX485 module's RO pin
  sends 5 volts towards the D1 mini. The ESP8266 datasheet allows at most 3.6 V on a pin,
  and a resistor doesn't change that. Power the module from **3V3**, as shown.
- **They don't protect the cable side** against static or lightning surges. For a short
  indoor cable that's rarely a concern; for long or outdoor cables, use an isolated RS485
  module (see [Safety](inverter.md#safety)).

</details>

## 📦 Put it in a box

Keep the boards dry and out of direct sun, for example in a small plastic project box
next to the inverter, with the network cable and USB cable entering through a hole. Is
the inverter outside? Then put the D1 mini indoors and run a longer network cable to it.

---

**Next:** [🔆 Step 2: Prepare the inverter and cable](inverter.md) →
