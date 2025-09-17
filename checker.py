#!/usr/bin/env python3

import base64
import fileinput
import json
import subprocess
import sys
import webbrowser
import zlib

RECIPES = [
    "https://asp-chef.alviano.net/#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%21",
]


def compress_object_for_url(obj: object, *, suffix: str = '%21'):
    json_dump = json.dumps(obj, separators=(',', ':')).encode()
    json_dump = base64.b64encode(json_dump)
    return base64.b64encode(zlib.compress(json_dump)).decode() + suffix


args = [arg for arg in sys.argv if arg != "--no-browser"]
no_browser = bool([arg for arg in sys.argv if arg == "--no-browser"])

if len(args) != 2:
    sys.exit("ERROR: missing problem-ID in command parameters")

try:
    problem = int(sys.argv[1])
except ValueError:
    sys.exit("ERROR: problem-ID must be integer")

if problem < 0 or problem >= len(RECIPES):
    sys.exit("ERROR: invalid problem-ID")


the_input = ''.join(fileinput.input("-"))

if no_browser:
    proc = subprocess.Popen(f"""
sudo docker run -i malvi/asp-chef-cli --headless run-with -u {RECIPES[problem]}
    """.strip().split(' '), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate(the_input.encode())
    print(o.decode())
    print(e.decode())
else:
    webbrowser.open(
        RECIPES[problem].replace("/#", "/open#" + compress_object_for_url({"input": the_input}, suffix="") + ";", 1)
    )




