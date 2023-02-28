#!/usr/bin/env python3

import json
import sys
from string import Template
from urllib.parse import urljoin, urlparse


def exit_message(more=""):
    """
    Exit printing default message, appending the contents of the
    more parameter if provided.
    :param more:
    """
    sys.exit(
        f"Usage: {sys.argv[0]} lang (en|nl) base_url \n"
        + "This will create (overwrite!) a file called slack_manifest.yml\n\n"
        + more
    )


try:
    lang = sys.argv[1]
    base_url = sys.argv[2]
except IndexError:
    exit_message("Have you forgotten arguments?")

if not urlparse(base_url).scheme:
    exit_message("Have you swapped the parameters?")

event_url = urljoin(base_url, "/slack/events")

with open(lang + "_man.json") as json_input:
    command_data = json.loads(json_input.read())

manifest_command_template = Template(
    """    - command: $command
      url: $event_url
      description: "$description"
      usage_hint: "$example"
      should_escape: true
"""
)

manifest_command_data = ""
for command in command_data:
    command["event_url"] = event_url
    manifest_command_item = manifest_command_template.substitute(command)
    manifest_command_data += manifest_command_item

with open("slack_manifest.tpl") as tpl_file:
    manifest_template = Template(tpl_file.read())

manifest_keys = {"event_url": event_url, "slash_commands": manifest_command_data}
manifest_output_data = manifest_template.substitute(manifest_keys)

# slack does not like empty usage hints.
manifest_output_data = manifest_output_data.replace('      usage_hint: ""\n', "")

with open("slack_manifest.yml", "w") as manifest_file:
    manifest_file.write(manifest_output_data)
