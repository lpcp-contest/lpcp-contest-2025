#!/usr/bin/env python3

import base64
import fileinput
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




