#!/usr/bin/python

import os, ConfigParser
import json

config = ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/Library/Application Support/Firefox/profiles.ini'))

profiles = []

# Loop over all the sections in the config file
for name in config.sections():
    try:
        # Get the Name from each firefox profile
        profile_names = config.get(name, "Name")
        # Append the profile name to the appropriate json keys
        config_dict = {"uid": profile_names, "type": "default", "title": profile_names,
                       "subtitle": name + " : " + profile_names,
                       "autocomplete": profile_names, "arg": profile_names}
        # Append each config_dict the the profiles list
        profiles.append(config_dict)
        # In the event there is a profile with no Name, skip over it
    except ConfigParser.NoOptionError:
        config_dict = {"type": "default", "title": "Invalid profile",
                       "subtitle": name + " : " + "This is an invalid profile",
                       "autocomplete": "-ProfileManager", "arg": "-ProfileManager"}
        # Append each config_dict the the profiles list
        profiles.append(config_dict)
        continue

# Convert the profiles list to a json object
json_convert = json.dumps(profiles, sort_keys=True, indent=2)
# Append the items to the json object then print it
print '{{"items" :  {profile} }}'.format(profile=json_convert)
