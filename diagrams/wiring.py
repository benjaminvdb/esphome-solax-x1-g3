"""Draw images/wiring.svg: the inverter cable, RS485 module and Wemos D1 mini.

Run with `python diagrams/wiring.py` from the repository root. No dependencies.
Colours come from the Okabe-Ito palette, which stays distinguishable for
people with colour-vision deficiency; every wire also carries a text label,
so the diagram still works printed in black and white.
"""

from pathlib import Path

W, H = 1240, 800
FONT = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"

POWER = "#D55E00"  # vermillion
GROUND = "#1a1a1a"
SEND = "#0072B2"  # blue: D1 mini -> module
RECEIVE = "#009E73"  # green: module -> D1 mini
SWITCH = "#CC79A7"  # purple: send/receive switch
CABLE_BLUE = "#1f5fbf"
CABLE_BROWN = "#7a4a22"
CABLE_GREEN = "#2e8b3a"
MUTED = "#9a9a9a"

out: list[str] = []


def add(s: str) -> None:
    out.append(s)


def text(x, y, s, size=15, weight="normal", anchor="start", fill="#1a1a1a", italic=False):
    style = ' font-style="italic"' if italic else ""
    add(
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}"{style}>{s}</text>'
    )


def wire(points, color, width=5, dash=None, arrow_at=None):
    d = "M " + " L ".join(f"{x} {y}" for x, y in points)
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    add(
        f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" '
        f'stroke-linecap="round" stroke-linejoin="round"{dash_attr}/>'
    )
    if arrow_at:
        (x, y), direction = arrow_at
        s = 9
        pts = {
            "left": f"{x - s},{y} {x + s},{y - s} {x + s},{y + s}",
            "right": f"{x + s},{y} {x - s},{y - s} {x - s},{y + s}",
        }[direction]
        add(f'<polygon points="{pts}" fill="{color}"/>')


def striped_wire(points, color):
    """A white wire with a coloured stripe, like the 'blue-white' cable pair."""
    wire(points, "#555555", width=9)
    wire(points, "#ffffff", width=6)
    add(f'<path d="M ' + " L ".join(f"{x} {y}" for x, y in points) + f'" fill="none" stroke="{color}" stroke-width="6" stroke-dasharray="12 8"/>')


def resistor(x, y, color, label="1 kΩ (optional)"):
    """An optional series resistor: a zigzag on the wire, drawn dashed-outlined."""
    add(f'<rect x="{x - 26}" y="{y - 12}" width="52" height="24" rx="4" fill="#ffffff" '
        f'stroke="{color}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    pts = " ".join(f"{x - 20 + i * 5},{y + (0 if i in (0, 8) else (-7 if i % 2 else 7))}" for i in range(9))
    add(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.5" '
        f'stroke-linejoin="round"/>')
    text(x, y - 17, label, size=11, anchor="middle", fill="#555")


def dot(x, y, color):
    add(f'<circle cx="{x}" cy="{y}" r="7" fill="{color}"/>')


def pin(x, y, color="#e8c34a", used=True):
    add(
        f'<circle cx="{x}" cy="{y}" r="8" fill="{color if used else "#cfcfcf"}" '
        f'stroke="#333" stroke-width="1.5"/>'
    )


def label_box(x, y, s, color, anchor="middle"):
    """A small rounded tag on top of a wire, so the label never floats away."""
    width = 9 * len(s) + 16
    x0 = x - width / 2 if anchor == "middle" else x
    add(
        f'<rect x="{x0}" y="{y - 15}" width="{width}" height="24" rx="12" '
        f'fill="#ffffff" stroke="{color}" stroke-width="2"/>'
    )
    text(x0 + width / 2, y + 2, s, size=13, weight="600", anchor="middle", fill=color)


add(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">'
)
add('<title id="title">Wiring diagram: SolaX inverter to RS485 module to Wemos D1 mini</title>')
add(
    '<desc id="desc">Network cable pin 4 (blue) goes to A, pin 5 (blue-white) goes to B '
    "and optionally pin 3 (green-white) goes to GND on the RS485 module. On the module, VCC goes to "
    "3V3, GND to GND, DI to D7, RO to D6, and DE and RE are joined and go to D5 on the "
    "Wemos D1 mini. The D1 mini is powered over USB.</desc>"
)
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

text(40, 50, "How to wire it", size=28, weight="700")
text(
    40, 80,
    "Three parts, eight wires (one optional). Every wire is labelled; the colours only help.",
    size=16, fill="#444",
)

# --- 1. Inverter cable (RJ45 plug, pins listed top to bottom) -------------------
add('<rect x="40" y="130" width="230" height="470" rx="16" fill="#f4f6f8" stroke="#c9d1d9"/>')
text(155, 160, "1 · Inverter cable", size=17, weight="700", anchor="middle")
text(155, 182, "RS485/Meter port, RJ45 plug", size=13, anchor="middle", fill="#555")

T568B = [
    (1, "orange-white", "#e07b00", True),
    (2, "orange", "#e07b00", False),
    (3, "green-white", "#2e8b3a", True),
    (4, "blue", CABLE_BLUE, False),
    (5, "blue-white", CABLE_BLUE, True),
    (6, "green", "#2e8b3a", False),
    (7, "brown-white", CABLE_BROWN, True),
    (8, "brown", CABLE_BROWN, False),
]
USED = {3: "GND", 4: "A", 5: "B"}
cable_y = {}
for i, (n, name, color, striped) in enumerate(T568B):
    y = 220 + i * 46
    cable_y[n] = y
    used = n in USED
    add(
        f'<rect x="62" y="{y - 14}" width="34" height="28" rx="5" '
        f'fill="{"#fff6d6" if used else "#ffffff"}" stroke="#888"/>'
    )
    text(79, y + 5, str(n), size=14, weight="700", anchor="middle")
    text(108, y + 5, name, size=13, fill="#1a1a1a" if used else MUTED)
    if not used:
        wire([(205, y), (245, y)], MUTED, width=3, dash="2 6")
text(155, 585, "Grey pins: not used", size=12, anchor="middle", fill=MUTED, italic=True)

# --- 2. RS485 module --------------------------------------------------------------
MX0, MX1 = 450, 640
add(f'<rect x="{MX0}" y="200" width="{MX1 - MX0}" height="380" rx="14" fill="#1d4f91"/>')
text((MX0 + MX1) / 2, 160, "2 · RS485 module", size=17, weight="700", anchor="middle")
text((MX0 + MX1) / 2, 182, "MAX485 / MAX3485 board", size=13, anchor="middle", fill="#555")
add(f'<rect x="{(MX0 + MX1) / 2 - 38}" y="230" width="76" height="76" rx="6" fill="#111"/>')
text((MX0 + MX1) / 2, 273, "485", size=14, weight="700", anchor="middle", fill="#ddd")

left_pins = {"A": 358, "B": 404}
right_pins = {"DE": 340, "RE": 380, "RO": 420, "DI": 460, "VCC": 500}
for name, y in left_pins.items():
    pin(MX0, y)
    text(MX0 + 18, y + 5, name, size=15, weight="700", fill="#ffffff")
for name, y in right_pins.items():
    pin(MX1, y)
    text(MX1 - 18, y + 5, name, size=15, weight="700", anchor="end", fill="#ffffff")
GND_X = (MX0 + MX1) / 2
pin(GND_X, 580)
text(GND_X, 568, "GND", size=15, weight="700", anchor="middle", fill="#ffffff")

# --- 3. Wemos D1 mini -------------------------------------------------------------
DX0, DX1 = 900, 1120
add(f'<rect x="{DX0}" y="200" width="{DX1 - DX0}" height="400" rx="14" fill="#0b6e6e"/>')
add(f'<rect x="{DX0 + 50}" y="214" width="{DX1 - DX0 - 100}" height="34" rx="4" fill="#d9d9d9"/>')
text((DX0 + DX1) / 2, 236, "Wi-Fi chip", size=12, anchor="middle", fill="#333")
add(f'<rect x="{(DX0 + DX1) / 2 - 26}" y="586" width="52" height="34" rx="5" fill="#bdbdbd" stroke="#555"/>')
text((DX0 + DX1) / 2, 645, "USB: power from a phone charger", size=13, anchor="middle", fill="#555")
text((DX0 + DX1) / 2, 160, "3 · Wemos D1 mini", size=17, weight="700", anchor="middle")
text((DX0 + DX1) / 2, 182, "the small Wi-Fi computer", size=13, anchor="middle", fill="#555")

LEFT_COL = ["RST", "A0", "D0", "D5", "D6", "D7", "D8", "3V3"]
RIGHT_COL = ["TX", "RX", "D1", "D2", "D3", "D4", "GND", "5V"]
d1 = {}
for i, name in enumerate(LEFT_COL):
    y = 260 + i * 40
    d1[name] = (DX0, y)
    used = name in {"D5", "D6", "D7", "3V3"}
    pin(DX0, y, used=used)
    text(DX0 + 18, y + 5, name, size=14, weight="700" if used else "normal",
         fill="#ffffff" if used else "#a8d5d5")
for i, name in enumerate(RIGHT_COL):
    y = 260 + i * 40
    d1[name] = (DX1, y)
    used = name == "GND"
    pin(DX1, y, used=used)
    text(DX1 - 18, y + 5, name, size=14, weight="700" if used else "normal",
         anchor="end", fill="#ffffff" if used else "#a8d5d5")

# --- Wires: module <-> D1 mini (pins are aligned, so these run straight) -------
y_d5, y_d6, y_d7, y_3v3 = d1["D5"][1], d1["D6"][1], d1["D7"][1], d1["3V3"][1]
wire([(MX1, right_pins["DE"]), (690, right_pins["DE"]), (690, y_d5)], SWITCH)
wire([(MX1, right_pins["RE"]), (DX0, y_d5)], SWITCH)
dot(690, y_d5, SWITCH)
label_box(790, y_d5, "D5 → DE + RE", SWITCH)
wire([(MX1, right_pins["RO"]), (DX0, y_d6)], RECEIVE, arrow_at=((870, y_d6), "right"))
label_box(790, y_d6, "RO → D6", RECEIVE)
resistor(700, y_d6, RECEIVE)
wire([(MX1, right_pins["DI"]), (DX0, y_d7)], SEND, arrow_at=((670, y_d7), "left"))
label_box(790, y_d7, "D7 → DI", SEND)
resistor(712, y_d7, SEND, label="")
wire([(MX1, right_pins["VCC"]), (720, right_pins["VCC"]), (720, y_3v3), (DX0, y_3v3)], POWER)
label_box(810, y_3v3, "3V3 → VCC", POWER)

GND_Y = 670
gx, gy = d1["GND"]
wire([(GND_X, 580), (GND_X, GND_Y), (1180, GND_Y), (1180, gy), (gx, gy)], GROUND)
label_box(1000, GND_Y, "GND → GND", GROUND)

# --- Wires: cable <-> module ------------------------------------------------------
wire([(205, cable_y[4]), (MX0, left_pins["A"])], CABLE_BLUE, width=6)
label_box(385, left_pins["A"], "pin 4 → A", CABLE_BLUE)
striped_wire([(205, cable_y[5]), (MX0, left_pins["B"])], CABLE_BLUE)
label_box(385, left_pins["B"], "pin 5 → B", CABLE_BLUE)
striped_wire([(205, cable_y[3]), (245, cable_y[3]), (245, GND_Y), (GND_X, GND_Y)], CABLE_GREEN)
dot(GND_X, GND_Y, GROUND)
label_box(330, GND_Y, "pin 3 → GND (optional)", CABLE_GREEN)

# --- Legend -----------------------------------------------------------------------
legend = [
    (POWER, "power (3.3 volt)"),
    (GROUND, "ground (0 volt), shared by everything"),
    (SEND, "data from the D1 mini to the inverter"),
    (RECEIVE, "data from the inverter to the D1 mini"),
    (SWITCH, "send/receive switch"),
    (CABLE_BLUE, "network cable wire (striped = white with colour)"),
    ("#555555", "dashed box: optional 1 kΩ resistor (see the build guide)"),
]
for i, (color, s) in enumerate(legend):
    col, row = divmod(i, 3)
    x, y = 40 + col * 400, 726 + row * 22
    add(f'<line x1="{x}" y1="{y}" x2="{x + 28}" y2="{y}" stroke="{color}" stroke-width="5" stroke-linecap="round"/>')
    text(x + 38, y + 5, s, size=13, fill="#333")

add("</svg>")

target = Path(__file__).resolve().parent.parent / "images" / "wiring.svg"
target.parent.mkdir(exist_ok=True)
target.write_text("\n".join(out) + "\n")
print(f"wrote {target}")
