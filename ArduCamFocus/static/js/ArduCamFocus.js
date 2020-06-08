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

		self.onStartup = function() {
			$('#control-focus').insertAfter('#control-jog-general');
		}

		self.onBeforeBinding = function() {
		    self.controlViewModel.right = ko.observable('@ARDUCAMFOCUS 50');
		    self.controlViewModel.left = ko.observable('@ARDUCAMFOCUS -50');
		    self.controlViewModel.focus = ko.observable('@ARDUCAMFOCUSSET ' + self.settingsViewModel.settings.plugins.ArduCamFocus.FOCUS());
		}

		self.onEventSettingsUpdated = function (payload) {            
			self.controlViewModel.right('@ARDUCAMFOCUS 50');
			self.controlViewModel.left('@ARDUCAMFOCUS -50');
		        self.controlViewModel.focus('@ARDUCAMFOCUSSET ' + self.settingsViewModel.settings.plugins.ArduCamFocus.FOCUS());
		};
	}

	OCTOPRINT_VIEWMODELS.push({
		construct: ArduCamFocusViewModel,
		dependencies: [ "controlViewModel", "settingsViewModel" ],
		elements: [ "settings_plugin_ArduCamFocus_form", "control-focus" ]
	});
});
