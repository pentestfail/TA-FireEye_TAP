import ta_fireeye_tap_declare

import os
import sys
import time
import datetime

import modinput_wrapper.base_modinput
from solnlib.packages.splunklib import modularinput as smi



import input_module_fireeye_tap_incidents as input_module


'''
    Do not edit this file!!!
    This file is generated by Add-on builder automatically.
    Add your modular input logic to file input_module_fireeye_tap_incidents.py
'''
class ModInputfireeye_tap_incidents(modinput_wrapper.base_modinput.BaseModInput):

    def __init__(self):
        if 'use_single_instance_mode' in dir(input_module):
            use_single_instance = input_module.use_single_instance_mode()
        else:
            use_single_instance = False
        super(ModInputfireeye_tap_incidents, self).__init__("ta_fireeye_tap", "fireeye_tap_incidents", use_single_instance)
        self.global_checkbox_fields = None

    def get_scheme(self):
        """overloaded splunklib modularinput method"""
        scheme = super(ModInputfireeye_tap_incidents, self).get_scheme()
        scheme.title = ("FireEye TAP Incidents")
        scheme.description = ("Incidents generated in FireEye Threat Analytics Platform (TAP).")
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True

        scheme.add_argument(smi.Argument("name", title="Name",
                                         description="",
                                         required_on_create=True))

        """
        For customized inputs, hard code the arguments here to hide argument detail from users.
        For other input types, arguments should be get from input_module. Defining new input types could be easier.
        """
        scheme.add_argument(smi.Argument("instance_id", title="Instance ID",
                                         description="Unique identifier for TAP instance.",
                                         required_on_create=False,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("apikey", title="API Key",
                                         description="API Key created to retrieve alerts from TAP instance (see documentation).",
                                         required_on_create=False,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("api_env", title="Environment",
                                         description="Production should be use unless otherwise directed.",
                                         required_on_create=False,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("api_timeout", title="Timeout",
                                         description="Configurable timeout in seconds (should be less than API request interval).",
                                         required_on_create=False,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("api_limit", title="API Limit",
                                         description="Configurable limit of results to return per API request (higher limits may not complete timeout in short intervals).",
                                         required_on_create=False,
                                         required_on_edit=False))
        return scheme

    def get_app_name(self):
        return "TA-FireEye_TAP"

    def validate_input(self, definition):
        """validate the input stanza"""
        input_module.validate_input(self, definition)

    def collect_events(self, ew):
        """write out the events"""
        input_module.collect_events(self, ew)

    def get_account_fields(self):
        account_fields = []
        return account_fields

    def get_checkbox_fields(self):
        checkbox_fields = []
        return checkbox_fields

    def get_global_checkbox_fields(self):
        if self.global_checkbox_fields is None:
            checkbox_fields = []
            customized_settings = {}.get('global_settings', {}).get('customized_settings', [])
            for global_var in customized_settings:
                if global_var.get('type', '') == 'checkbox':
                    checkbox_fields.append(global_var['name'])
            self.global_checkbox_fields = checkbox_fields
        return self.global_checkbox_fields

if __name__ == "__main__":
    exitcode = ModInputfireeye_tap_incidents().run(sys.argv)
    sys.exit(exitcode)
