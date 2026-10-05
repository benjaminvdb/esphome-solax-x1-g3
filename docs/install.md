# Step 3: Install the software

In this step you put ESPHome (the software that runs on the D1 mini) on the board, using
the configuration file from this project, and add the result to Home Assistant.

**Time:** 20–30 minutes. **You'll need:** Home Assistant with the **ESPHome Device Builder**
add-on ([installation guide](https://esphome.io/guides/getting_started_hassio/)) version
**2026.9.0 or newer**, the D1 mini, a micro-USB data cable, and Chrome or Edge.

The first install goes over a USB cable. After that, every update goes over Wi-Fi and you
won't need the cable again.

## 1. Add your secrets

The configuration refers to your Wi-Fi password and other private values by name, so the
file itself contains nothing private. You store the real values once, in a file called
`secrets.yaml`.

1. Open **ESPHome Builder** in the Home Assistant sidebar.
2. Open **Secrets** (in the menu at the top right).
3. Add these lines, with your own values. [`secrets.example.yaml`](../secrets.example.yaml)
   has the same lines with explanations.

```yaml
wifi_ssid: "Your Wi-Fi network name"
wifi_password: "Your Wi-Fi password"
fallback_password: "choose-a-password"   # 8 characters or more
api_encryption_key: "..."                # see below
```

**The API encryption key** protects the connection between the D1 mini and Home Assistant.
It must be 32 random bytes written as base64. The easiest way to get one: the
[ESPHome API page](https://esphome.io/components/api/#configuration-variables) has a box
that generates a key for you. Use a new key for every device; don't copy one from another
device.

> **You should now see** your four secrets saved. If the editor shows a red error, check
> that each value is between quotes.

## 2. Create the device

1. In ESPHome Builder, click **Create device** (or **+ New device**) and give it the name
   `solax`.
2. When asked for the board type, choose **ESP8266** (or *Wemos D1 Mini*).
3. Open the new device with **Edit**, select everything in the editor and delete it.
4. Paste the full contents of [`solax-x1.yaml`](../solax-x1.yaml) and click **Save**.
5. Click **Validate** (if your version shows it).

> **You should now see** "Configuration is valid". If you see an error about a secret not
> being defined, check the spelling in step 1: `api_encryption_key` and `fallback_password`
> must match exactly.

## 3. First install, over USB

1. Plug the D1 mini into the computer you're using, with a micro-USB cable. Some cables
   only charge and can't carry data; if nothing happens in step 3, try another cable.
2. Click **Install** and choose **Plug into this computer** (the wording differs slightly
   between versions).
3. Your browser asks which serial port to use. Pick the one that appeared when you plugged
   in the D1 mini (often called *CH340* or *USB Serial*).
4. Wait. Building the software takes a few minutes the first time; installing takes about
   a minute.

> **You should now see** "Installation complete" or the device's log. Don't worry if the
> log mentions Modbus timeouts: the D1 mini isn't connected to the inverter yet.

**No "Plug into this computer" option, or your browser can't see the board?** Choose
**Manual download** instead, then open [web.esphome.io](https://web.esphome.io/) in
Chrome or Edge, click *Connect*, and install the downloaded file from there.

## 4. Connect it to the inverter

1. Unplug the D1 mini from the computer.
2. Put it in its final place, plug the inverter cable into the inverter (see
   [step 2](inverter.md)), and power the D1 mini from a USB phone charger.
3. Do this in daylight: the inverter switches itself off at night.

> **You should now see** the device marked **Online** in ESPHome Builder within a minute.
> Open its **Logs**: after about 15 seconds the values arrive, without
> `Modbus error` lines.

## 5. Add it to Home Assistant

Home Assistant usually finds the new device by itself.

1. Go to **Settings → Devices & services**. A **Discovered: solax** card should appear.
2. Click **Configure** and confirm. If you're asked for the encryption key, paste the
   `api_encryption_key` value from your secrets.

> **You should now see** a device called *solax* with about 25 entities: power, voltages,
> production, Run Mode and so on. During the day, Run Mode shows **Normal** and Inverter
> Power shows a number of watts.

That's it, the hardware part is done. Later updates go over Wi-Fi: change the
configuration, click **Install**, and choose **Wirelessly**.

**Next:** [Step 4: Use the data](home-assistant.md) · Not working? [Troubleshooting](troubleshooting.md)
