import json
import os

# User realpath to reliably use the file in the same directory as the script
# Source: https://stackoverflow.com/a/4060259
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# JSON object load
jsonfile = open(os.path.join(__location__, 'sample.json'), 'r')

jsonstr = jsonfile.read()

jsonobj = json.loads(jsonstr)

print(jsonobj)