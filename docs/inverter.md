# Step 2: Prepare the inverter and cable

In this step you switch on Modbus in the inverter's menu, make a cable with one network
plug, and connect two (or three) of its wires to the RS485 module.

**Time:** 20–40 minutes. **You'll need:** a network cable, wire strippers or a knife, and a
small screwdriver.

## Safety

- **Never open the inverter.** It contains high voltages, even after you switch it off.
  Everything in this guide happens through the communication port on the outside.
- The port you'll use, labelled **RS485/Meter** (on some models **RS485/Meter/CT/DRM**), is
  meant for meters and monitoring equipment. If it sits behind a cover or cable gland you
  aren't sure you may open, ask your installer first.
- The port's documentation doesn't say whether it's electrically isolated from the rest of
  the inverter. Keep the cable reasonably short (a few metres is fine), indoors or in a
  dry place, and don't connect the D1 mini to anything mains-powered apart from its own USB
  charger. For long cables or outdoor runs, an *isolated* RS485 module is the safer choice.

## 1. Switch on Modbus in the inverter

The inverter can speak Modbus, but on some units it has to be enabled first. Users report
that this needs **ARM firmware 1.37 or newer** (shown in the inverter's *About* menu);
older firmware only speaks SolaX's own protocol.

1. On the inverter's display, open the **Settings** menu.
2. Enter the password. Installers commonly report **6868** (advanced settings) or
   **2014**; your installer may have changed it.
3. Find the RS485 or Modbus setting and select **Modbus**.
4. Check the **Modbus address** is **1** and the speed (baud rate) is **9600**.

Menu names differ slightly between models and firmware versions. Your inverter's manual
shows the exact path.

> **You should now see** Modbus selected and address 1. If you use another address, change
> `modbus_address` at the top of `solax-x1.yaml` to match.

## 2. Make the cable

You need a network cable with a plug on one end and bare wires on the other.

1. Cut one plug off the cable. Keep enough length to reach from the inverter to where the
   D1 mini will hang.
2. Strip about 3 cm of the outer jacket. You'll see eight thin wires in four twisted pairs.
3. Find these three and strip about 5 mm of each:

| Plug pin | Wire colour (T-568B, most common) | Inverter signal | RS485 module |
|---|---|---|---|
| **4** | blue | 485 A | **A** |
| **5** | white with blue stripe | 485 B | **B** |
| **3** | white with green stripe (T-568A: white with orange stripe) | GND_COM (ground), optional | **GND** |

4. Cut the other wires short so they can't touch anything.

![Wiring diagram](../images/wiring.svg)

**Is my cable T-568B?** Hold the plug with the clip underneath and the copper contacts
facing you, cable pointing down; pin 1 is on the left. In a T-568B cable, pin 1 is white-orange and
pin 2 orange. In the rarer T-568A cable, those are white-green and green. **Pins 4 and 5
are blue and white-blue in both**; only pin 3 differs, as shown in the table.

## 3. Connect the cable to the module

1. Put the **blue** wire into screw terminal **A** and the **white-blue** wire into **B**.
   Tighten the screws and tug gently: the wires should stay put.
2. **Optional:** connect the pin 3 wire (GND_COM) to the module's **GND** pin, the same
   pin that already goes to the D1 mini's GND. RS485 only strictly needs A and B, and the
   author's setup uses only those two. A shared ground gives both sides the same 0-volt
   reference, which can help when communication is unreliable. Pin 3 is the ground pin
   named in SolaX's X1 Boost G3 manual.

> **A and B swapped?** Nothing breaks, it just won't read any data. Swapping A and B is a
> normal troubleshooting step.

## 4. Plug in

Plug the network plug into the inverter's **RS485/Meter** port. Leave the D1 mini
unpowered for now: it doesn't have any software yet.

**Next:** [Step 3: Install the software](install.md)
