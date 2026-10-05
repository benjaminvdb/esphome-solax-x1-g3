# 🔆 Step 2: Prepare the inverter and cable

In this step you switch on Modbus in the inverter's menu, make a cable with one network
plug, and connect two (or three) of its wires to the RS485 module.

| | |
|---|---|
| ⏱️ **Time** | 20–40 minutes |
| 🧰 **You'll need** | a network cable, wire strippers or a knife, a small screwdriver |
| 🎯 **Result** | Modbus switched on, and a cable from the inverter to the RS485 module |

<a name="safety"></a>

## 🦺 Safety

> [!CAUTION]
> **Never open the inverter.** It contains high voltages, even after you switch it off.
> Everything in this guide happens through the communication port on the outside.

- **Use only the communication port.** It's labelled **RS485/Meter** (on some models
  **RS485/Meter/CT/DRM**) and is meant for meters and monitoring equipment. Is it behind
  a cover or cable gland you aren't sure you may open? Ask your installer first.
- **Keep it simple and dry.** The documentation doesn't say whether the port is
  electrically isolated from the rest of the inverter. So keep the cable reasonably short
  (a few metres is fine), indoors or somewhere dry, and don't connect the D1 mini to
  anything mains-powered apart from its own USB charger.
- **Long or outdoor cable?** Then an *isolated* RS485 module is the safer choice.

<a name="1-switch-on-modbus-in-the-inverter"></a>

## 📟 1. Switch on Modbus in the inverter

The inverter can speak Modbus, but on some units it has to be enabled first. Users report
that this needs **ARM firmware 1.37 or newer** (shown in the inverter's *About* menu);
older firmware only speaks SolaX's own protocol.

1. On the inverter's display, open the **Settings** menu.
2. Enter the password. Installers commonly report **6868** (advanced settings) or
   **2014**; your installer may have changed it.
3. Find the RS485 or Modbus setting and select **Modbus**.
4. Check that the **Modbus address** is **1** and the speed (*baud rate*) is **9600**.

Menu names differ slightly between models and firmware versions. Your inverter's manual
shows the exact path.

**✅ You should now see** Modbus selected, with address 1. Using another address? Change
`modbus_address` at the top of `solax-x1.yaml` to match.

## 🪢 2. Make the cable

You need a network cable with a plug on one end and bare wires on the other.

1. **Cut one plug off** the cable. Keep enough length to reach from the inverter to where
   the D1 mini will hang.
2. **Strip about 3 cm of the outer jacket.** You'll see eight thin wires in four twisted
   pairs.
3. **Find the wires in the table below** and strip about 5 mm of each.
4. **Cut the other wires short** so they can't touch anything.

| Plug pin | Wire colour | Inverter signal | Goes to module pin |
|:-:|---|---|---|
| **4** | 🔵 blue | 485 A | **A** |
| **5** | ⚪ white with blue stripe | 485 B | **B** |
| **3** | ⚪ white with green stripe¹ | GND_COM (ground) | **GND**, *optional* |

¹ In the rarer T-568A cable, pin 3 is *white with orange stripe*. Pins 4 and 5 are the
same in both kinds of cable.

![Wiring diagram](../images/wiring.svg)

<details>
<summary><b>Which kind of cable do I have?</b></summary>

<br>

Hold the plug with the clip underneath, the copper contacts facing you and the cable
pointing down. Pin 1 is on the left.

| Cable type | Pin 1 | Pin 2 | Pin 3 |
|---|---|---|---|
| **T-568B** (most common) | white-orange | orange | white-green |
| **T-568A** | white-green | green | white-orange |

</details>

## 🔗 3. Connect the cable to the module

1. **Put the blue wire into screw terminal A** and the **white-blue wire into B**.
   Tighten the screws and tug gently: the wires should stay put.
2. **Optional: connect the pin 3 wire** (GND_COM) to the module's **GND** pin, the same
   pin that already goes to the D1 mini's GND.
   - RS485 only strictly needs A and B; the author's setup uses only those two.
   - A shared ground gives both sides the same 0-volt reference, which can help when
     communication is unreliable.
   - Pin 3 is the ground pin named in SolaX's X1 Boost G3 manual.

> [!TIP]
> **A and B swapped?** Nothing breaks; it just won't read any data. Swapping A and B is a
> normal troubleshooting step.

## 🔌 4. Plug in

Plug the network plug into the inverter's **RS485/Meter** port. Leave the D1 mini
unpowered for now: it doesn't have any software yet.

---

**Next:** [💾 Step 3: Install the software](install.md) →
