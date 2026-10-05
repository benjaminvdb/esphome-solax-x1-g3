# 🔆 Step 2: Prepare the inverter and cable

Here you switch on Modbus in the inverter's menu, make a cable with a network plug on one
end, and connect two or three of its wires to the RS485 module. Plan on 20 to 40 minutes.
You need a network cable, wire strippers or a knife, and a small screwdriver.

<a name="safety"></a>

## 🦺 Safety

> [!CAUTION]
> Never open the inverter. It contains high voltages, even when it's switched off.
> Everything in this guide happens through the communication port on the outside.

The port you'll use is labelled RS485/Meter (on some models RS485/Meter/CT/DRM). It's
meant for meters and monitoring equipment. If it's behind a cover or cable gland and
you're not sure you're allowed to open it, ask your installer first.

SolaX's documentation doesn't say whether this port is electrically isolated from the
rest of the inverter. So keep the cable fairly short (a few metres is fine), run it
indoors or somewhere dry, and power the D1 mini from the inverter's own USB port or a USB
phone charger, not from other equipment. If you need a long or outdoor cable, an
isolated RS485 module is the safer choice.

<a name="1-switch-on-modbus-in-the-inverter"></a>

## 📟 1. Switch on Modbus in the inverter

The inverter speaks Modbus, but on some units you have to switch it on first. According
to other users this needs ARM firmware 1.37 or newer, which you can check in the
inverter's About menu. Older firmware only speaks SolaX's own protocol.

1. Open the Settings menu on the inverter's display.
2. Enter the password. People report 6868 (advanced settings) or 2014, though your
   installer may have changed it.
3. Find the RS485 or Modbus setting and select Modbus.
4. Check that the Modbus address is 1 and the speed (baud rate) is 9600.

The menu names differ a little between models and firmware versions. If you can't find
the setting, the manual for your inverter shows the exact path.

You should now see Modbus selected, with address 1. If you picked a different address,
change `modbus_address` at the top of `solax-x1.yaml` to match.

## 🪢 2. Make the cable

You need a network cable with a plug on one end and bare wires on the other.

1. Cut one plug off. Leave enough cable to reach from the inverter to where the D1 mini
   will go.
2. Strip about 3 cm of the outer jacket. Inside are eight thin wires in four twisted pairs.
3. Find the wires from the table below and strip about 5 mm off each.
4. Cut the remaining wires short so they can't touch anything.

| Plug pin | Wire colour | Inverter signal | Goes to module pin |
|:-:|---|---|---|
| 4 | blue | 485 A | A |
| 5 | white with a blue stripe | 485 B | B |
| 3 | white with a green stripe¹ | ground (GND_COM) | GND (optional) |

¹ Most cables follow the T-568B colour order. In the less common T-568A cables, pin 3 is
white with an orange stripe. Pins 4 and 5 are the same in both.

![Wiring diagram](../images/wiring.svg)

<details>
<summary>How to tell which colour order your cable uses</summary>

<br>

Hold the plug with the clip underneath, the copper contacts facing you and the cable
pointing down. Pin 1 is on the left. In a T-568B cable, pin 1 is white-orange and pin 2
is orange. In a T-568A cable, pin 1 is white-green and pin 2 is green.

</details>

## 🔗 3. Connect the cable to the module

Put the blue wire in screw terminal A and the white-blue wire in B. Tighten the screws
and give each wire a gentle tug to make sure it stays put.

Connecting the pin 3 wire to the module's GND pin (the one that already goes to the
D1 mini) is optional. RS485 only strictly needs A and B, and my own setup uses just those
two. A shared ground gives both sides the same 0-volt reference, though, which can help
if communication turns out to be unreliable. Pin 3 is the ground pin named in SolaX's
X1 Boost G3 manual.

> [!TIP]
> If A and B are the wrong way round, nothing breaks; you just won't get any data.
> Swapping them is a normal thing to try when troubleshooting.

## 🔌 4. Plug in

Plug the network plug into the inverter's RS485/Meter port. Leave the D1 mini unpowered
for now, because it doesn't have any software on it yet.

Next: [Step 3: Install the software](install.md)
