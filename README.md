# ArduCamFocus

This plugin controls the focus on an ArduCam Motorized Focus Camera.  https://www.arducam.com/docs/cameras-for-raspberry-pi/motorized-focus-camera/

It uses a custom `@ARDUCAMFOCUSSET FOCUS` command that can be incorporated within your slicer to automatically adjust focus while printing. 
You can also send relative adjustments with `@ARDUCAMFOCUS 50` or `@ARDUCAMFOCUS -50`

Example: `@ARDUCAMFOCUSSET 300` will set the focus to 300.   

## Pre-Installation Requirements

Please follow the manufacturer's instructions:

https://www.arducam.com/docs/cameras-for-raspberry-pi/motorized-focus-camera/

### Disclaimer

Although I have used this plugin and it has worked for me without issues, I take no resposiblity for any damage caused by using this plugin. Please make sure to do your reseach and understand the dangers and please be careful.

