#!/usr/bin/env python

import json
import sys

lang = sys.argv[1]
base_url = sys.argv[2]

event_url += "/slack/events"

with open(lang+".json") as jsinput:
    data = json.loads(jsinput.read())

commands_keys = [kk for kk in data.keys() if kk.startswith("COMMAND")]

manifest_command_template = f"""    - command: {command}
      url: {event_url}
      description: {description}
      usage_hint: {usage hint}
      should_escape: false"""

for command_key in commands_keys:
    print(manifest_command_template.format(event_url = event_url)
