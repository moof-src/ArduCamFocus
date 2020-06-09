# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import smbus

class ArduCamFocusPlugin(octoprint.plugin.SettingsPlugin, 
                         octoprint.plugin.AssetPlugin,
                         octoprint.plugin.TemplatePlugin,
                         octoprint.plugin.StartupPlugin):

	def __init__(self):
		self.bus = None

	def on_after_startup(self):
		self.current_focus = self._settings.get_int(["FOCUS"])

	##~~ SettingsPlugin mixin
	def get_settings_defaults(self):
		return dict(
			FOCUS="100"
		)

	def on_settings_save(self, data):
		oldFOCUS = self._settings.get_int(["FOCUS"])

		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

		newFOCUS = self._settings.get_int(["FOCUS"])

		if oldFOCUS != newFOCUS:
			self._logger.info("FOCUS changed, initilizing to %d." % (int(FOCUS)))
			self.current_focus = newFOCUS


	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/ArduCamFocus.js"],
		)

	##-- Template hooks

	def get_template_configs(self):
		return [dict(type="generic",custom_bindings=False)]

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			ArduCamFocus=dict(
				displayName="ArduCamFocus",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="moof-src",
				repo="ArduCamFocus",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/moof-src/ArduCamFocus/archive/{target_version}.zip"
			)
		)

	##~~ Utility functions

	def focus (self, f): 
		if f < 100:
			f = 100
		elif f > 1000:
			f = 1000
		value = (f << 4) & 0x3ff0
		data1 = (value >> 8) & 0x3f
		data2 = value & 0xf0
		try: 
			if self.bus == None:
				self.bus = smbus.SMBus(0)
			self._logger.info("setting FOCUS to %d" % (f))
			self.bus.write_byte_data(0xc, data1, data2)
			self.current_focus = f
			self._settings.set_int(["FOCUS"], f, min=100, max=1000)
			self._settings.save()
			self._plugin_manager.send_plugin_message(self._identifier, dict(focus_val=self.current_focus))
		except IOError:
			self._plugin_manager.send_plugin_message(self._identifier, dict(error="Unable to open SMBUS"))
			return
		except:
			self._logger.info("Error writing to BUS")
			self._plugin_manager.send_plugin_message(self._identifier, dict(error="Error Writing to BUS"))
			return

	##~~ atcommand hook

	def processAtCommand(self, comm_instance, phase, command, parameters, tags=None, *args, **kwargs):
		if command == 'ARDUCAMFOCUS':
			try:
				self.focus(self.current_focus + int(parameters))
			except ValueError:
				self._logger.info("unknown parameter %s" % parameters)
				return
		elif command == 'ARDUCAMFOCUSSET':
			try:
				self.focus(int(parameters))
			except ValueError:
				self._logger.info("unknown parameter %s" % parameters)
				return

__plugin_name__ = "ArduCamFocus"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ArduCamFocusPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
		"octoprint.comm.protocol.atcommand.queuing": __plugin_implementation__.processAtCommand
	}
