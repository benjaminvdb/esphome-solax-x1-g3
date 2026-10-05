# 💾 Step 3: Install the software

In this step you put ESPHome (the software that runs on the D1 mini) on the board, using
the configuration file from this project, and add the result to Home Assistant.

| | |
|---|---|
| ⏱️ **Time** | 20–30 minutes |
| 🧰 **You'll need** | Home Assistant with the **ESPHome Device Builder** add-on, version **2026.9.0 or newer** ([installation guide](https://esphome.io/guides/getting_started_hassio/)); the D1 mini; a micro-USB data cable; Chrome or Edge |
| 🎯 **Result** | a *solax* device in Home Assistant, showing live values |

The **first** install goes over a USB cable. After that, every update goes over Wi-Fi and
you won't need the cable again.

## 🔑 1. Add your secrets

The configuration refers to private values by name, so the file itself contains nothing
private. You store the real values once, in a file called `secrets.yaml`.

1. Open **ESPHome Builder** in the Home Assistant sidebar.
2. Open **Secrets** (in the menu at the top right).
3. Add these four lines, with your own values:

```yaml
wifi_ssid: "Your Wi-Fi network name"
wifi_password: "Your Wi-Fi password"
fallback_password: "choose-a-password"   # 8 characters or more
api_encryption_key: "..."                # see below
```

| Secret | What it's for |
|---|---|
| `wifi_ssid`, `wifi_password` | Your home Wi-Fi. |
| `fallback_password` | Protects the D1 mini's own emergency Wi-Fi network (see [Troubleshooting](troubleshooting.md)). |
| `api_encryption_key` | Encrypts the connection to Home Assistant and firmware updates. |

**Getting an API encryption key:** it must be 32 random bytes written as *base64*. The
[ESPHome API page](https://esphome.io/components/api/#configuration-variables) has a box
that generates a fresh one each time you open the page. **Use a new key for every
device**; don't copy one from another device.

**✅ You should now see** your four secrets saved. A red error usually means a missing
quote around a value.

## 🆕 2. Create the device

1. In ESPHome Builder, click **Create device** (or **+ New device**) and name it `solax`.
2. When asked for the board type, choose **ESP8266** (or *Wemos D1 Mini*).
3. Open the new device with **Edit**, select everything in the editor and delete it.
4. Paste the full contents of [`solax-x1.yaml`](../solax-x1.yaml) and click **Save**.
5. Click **Validate**, if your version shows it.

**✅ You should now see** *Configuration is valid*. An error about a secret that isn't
defined means a spelling difference: check `api_encryption_key` and `fallback_password`
in step 1.

## 🔌 3. First install, over USB

1. **Plug the D1 mini into your computer** with a micro-USB cable.
2. Click **Install** and choose **Plug into this computer** (the wording differs slightly
   between versions).
3. **Pick the serial port** your browser offers: the one that appeared when you plugged in
   the D1 mini, often called *CH340* or *USB Serial*.
4. **Wait.** Building takes a few minutes the first time; installing about a minute.

**✅ You should now see** *Installation complete* or the device's log. Modbus timeouts in
the log are fine for now: the D1 mini isn't connected to the inverter yet.

<details>
<summary><b>The browser can't see the board, or there's no "Plug into this computer"</b></summary>

<br>

- Try another USB cable. Many cables only charge and can't carry data.
- On Windows, clone D1 minis may need the *CH340* driver.
- Or choose **Manual download** instead, open [web.esphome.io](https://web.esphome.io/)
  in Chrome or Edge, click **Connect**, and install the downloaded file from there.

</details>

## 🌞 4. Connect it to the inverter

1. **Unplug the D1 mini** from the computer.
2. **Put it in its final place**, plug the inverter cable into the inverter (see
   [step 2](inverter.md)), and power the D1 mini from a USB phone charger.
3. **Do this in daylight.** The inverter switches itself off at night.

**✅ You should now see** the device marked **Online** in ESPHome Builder within a minute.
Open its **Logs**: after about 15 seconds, values arrive without `Modbus error` lines.

## 🏠 5. Add it to Home Assistant

Home Assistant usually finds the new device by itself.

1. Go to **Settings → Devices & services**. A **Discovered: solax** card should appear.
2. Click **Configure** and confirm. Asked for an encryption key? Paste the
   `api_encryption_key` value from your secrets.

**✅ You should now see** a device called *solax* with about 25 entities. During the day,
*Run Mode* shows **Normal** and *Inverter Power* shows a number of watts.

> [!TIP]
> **That's the hardware done! 🎉** Later updates go over Wi-Fi: change the
> configuration, click **Install** and choose **Wirelessly**.

---

**Next:** [🏠 Step 4: Use the data](home-assistant.md) → · Not working? [🩺 Troubleshooting](troubleshooting.md)
