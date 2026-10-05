# 💾 Step 3: Install the software

Here you put ESPHome on the D1 mini, using the configuration from this project, and add
the result to Home Assistant. It takes 20 to 30 minutes.

You need Home Assistant with the
[ESPHome Device Builder add-on](https://esphome.io/guides/getting_started_hassio/),
version 2026.9.0 or newer, plus the D1 mini, a micro-USB cable that carries data, and
Chrome or Edge. The first install goes over USB. After that, updates go over Wi-Fi and you
won't need the cable again.

## 🔑 1. Add your secrets

The configuration refers to your Wi-Fi password and a few other private values by name,
so the file itself contains nothing private. You enter the real values once, in a file
called `secrets.yaml`.

1. Open ESPHome Builder in the Home Assistant sidebar.
2. Open Secrets from the menu at the top right.
3. Add these four lines with your own values:

```yaml
wifi_ssid: "Your Wi-Fi network name"
wifi_password: "Your Wi-Fi password"
fallback_password: "choose-a-password"   # 8 characters or more
api_encryption_key: "..."                # see below
```

`fallback_password` protects the emergency Wi-Fi network the D1 mini opens when it can't
reach yours (see [Troubleshooting](troubleshooting.md)). `api_encryption_key` encrypts the
connection to Home Assistant and the firmware updates. It has to be 32 random bytes
written in base64. The [ESPHome API page](https://esphome.io/components/api/#configuration-variables)
generates a fresh one every time you open it. Use a new key for each device rather than
copying one from another device.

You should now see the four secrets saved. A red error usually means a value is
missing its quotes.

## 🆕 2. Create the device

1. In ESPHome Builder, click **Create device** (called **+ New device** in some versions)
   and name it `solax`.
2. When it asks for the board type, choose ESP8266, or Wemos D1 Mini if it's listed.
3. Open the new device with **Edit**, select everything in the editor and delete it.
4. Paste the contents of [`solax-x1.yaml`](../solax-x1.yaml) and click **Save**.
5. Click **Validate**, if your version has that button.

You should now see "Configuration is valid". If it complains about a secret that isn't
defined, compare the spelling of `api_encryption_key` and `fallback_password` with what you
entered in step 1.

## 🔌 3. First install, over USB

1. Plug the D1 mini into your computer.
2. Click **Install** and choose **Plug into this computer**. The wording varies a little
   between versions.
3. Your browser asks which serial port to use. Pick the one that appeared when you
   plugged in the D1 mini; it's often called CH340 or USB Serial.
4. Wait. Building takes a few minutes the first time, and installing about one more.

You should now see "Installation complete" or the device's log. Modbus timeouts in the
log are expected at this point, because the D1 mini isn't connected to the inverter yet.

<details>
<summary>If the browser can't see the board</summary>

<br>

Try another USB cable first: plenty of cables only charge. On Windows, cheap D1 mini
clones may need the CH340 driver. You can also choose **Manual download**, open
[web.esphome.io](https://web.esphome.io/) in Chrome or Edge, click **Connect** and install
the downloaded file from there.

</details>

## 🌞 4. Connect it to the inverter

Unplug the D1 mini from the computer and put it where it's going to live. Plug the
inverter cable into the inverter (see [step 2](inverter.md)). Do this during the day: the
inverter switches itself off at night.

For power, the inverter has a USB port of its own, and that's what I use: a short USB
cable from the inverter to the D1 mini, and no extra charger. The D1 mini then switches
off at night together with the inverter, so its sensors show as unavailable in Home
Assistant until the morning. That doesn't affect the Energy dashboard. If you'd rather
keep the D1 mini on around the clock, use a USB phone charger instead.

You should now see the device marked Online in ESPHome Builder within a minute. Open
its **Logs**. After about 15 seconds values start coming in, without `Modbus error`
lines.

## 🏠 5. Add it to Home Assistant

Home Assistant usually finds the new device by itself. Go to **Settings → Devices &
services**, where a "Discovered: solax" card should show up. Click **Configure** and
confirm. If it asks for an encryption key, paste the `api_encryption_key` from your
secrets.

You should now see a device called solax with about 25 entities. During the day, Run
Mode shows Normal and Inverter Power shows a number of watts.

From now on you can update over Wi-Fi: change the configuration, click **Install** and
choose **Wirelessly**.

Next: [Step 4: Use the data](home-assistant.md). Not working? See
[Troubleshooting](troubleshooting.md).
