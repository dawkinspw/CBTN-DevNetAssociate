import xmltodict
import os

# User realpath to reliably use the file in the same directory as the script
# Source: https://stackoverflow.com/a/4060259
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Get the XML file data
stream = open(os.path.join(__location__, 'sample.xml'), 'r')

# Parse the XML file into an 'OrderedDic'
xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    print(e)