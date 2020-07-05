---
layout: plugin

id: ArduCamFocus
title: ArduCamFocus
description: Plugin to control ArduCam with motorized focus control on octopi
author: moof, jneilliii
license: AGPLv3

date: 2020-06-08

homepage: https://github.com/moof-src/ArduCamFocus
source: https://github.com/moof-src/ArduCamFocus
archive: https://github.com/moof-src/ArduCamFocus/archive/master.zip

tags:
- ArduCam
- camera
- focus

featuredimage: /assets/img/plugins/ArduCamFocus/ControlScreenShot.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  python: ">=2.7,<4"

---

# ArduCamFocus

Here is a simple plugin to control an ArduCam motorized focus camera using the OctoPrint Control tab. It uses I2C and it is expected the user followed the Pre-Installation requirements below.

![screenshot](/assets/img/plugins/ArduCamFocus/ControlScreenShot.png)

It utilizes these custom commands from your slicer to adjust focus while printing:
  `@ARDUCAMFOCUS <RELATIVE-FOCUS>` to adjust focus 
  `@ARDUCAMFOCUSSET <ABS-FOCUS>` to specify an absolute focus. This command is handy to reset the focus when starting a new print after a power failure.

Example: `@ARDUCAMFOCUSSET 100` will move the focus to 100.

## Pre-Installation Requirements

Please follow the manufacturer's instructions:

This plugin uses I2C to communicate with the camera.  That is not enabled by default.  The ArduCamFocus plugin will not function until
you enable I2C.
  ssh to your octopi and enter this commands (this only needs to be done once):
```bash
if ! grep -Fxq "^#ArduCamFocus$" /boot/config.txt; then
sudo cat << end_of_file > /boot/config.txt
#ArduCamFocus
dtparam=i2c_vc=on
dtparam=i2c_arm=on
end_of_file
fi
```
After executing the above command, the file /boot/config.txt should now have the commands to enable I2C.  In addition, you have to enable the I2C
kernel module using raspi-config.  Again, ssh to your octopi, and then enter this command:
```bash
sudo raspi-config
```

1. select "5 Interfacing Options"
2. select "P5 I2C"
3. raspi-config will ask, "Would you like the ARM I2C interface to be enabled?"
4. select "Yes"
5. you should see, "The ARM I2C interface is enabled"
6. select "Finish"

After you reboot, the camera should become operational in OctoPrint.

## Settings

This plugin has no configurable settings.

### Disclaimer

Although I use this plugin and it works for me without issues, I take no resposiblity for any damage caused by using this plugin. Your camera version, i2c address, or system configuration may be different from mine.  Please make sure to do your reseach and understand the dangers and please be careful.

