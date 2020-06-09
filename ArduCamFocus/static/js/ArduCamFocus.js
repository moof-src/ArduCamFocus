/*
 * View model for ArduCamFocus
 *
 * Author: Moof
 * License: AGPLv3
 */
$(function() {
	function ArduCamFocusViewModel(parameters) {
		var self = this;

		self.controlViewModel = parameters[0];
		self.settingsViewModel = parameters[1];
		self.focus_val = ko.observable();
		self.error_msg = ko.observable('');

		self.onStartup = function() {
			$('#control_focus_wrapper').insertAfter('#control-jog-general');
		};

		self.onBeforeBinding = function() {
			self.focus_val(self.settingsViewModel.settings.plugins.ArduCamFocus.FOCUS());
		};

		self.onDataUpdaterPluginMessage = function(plugin, data) {
			if (plugin != "ArduCamFocus") {
				return;
			}

			if(data.focus_val) {
				self.focus_val(data.focus_val);
			}

			if(data.error) {
				self.error_msg(data.error);
			}
		}
	}

	OCTOPRINT_VIEWMODELS.push({
		construct: ArduCamFocusViewModel,
		dependencies: [ "controlViewModel", "settingsViewModel" ],
		elements: [ "#control_focus_snippet" ]
	});
});
