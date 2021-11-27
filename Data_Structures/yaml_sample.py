import os, yaml
from yaml import load, load_all

# User realpath to reliably use the file in the same directory as the script
# Source: https://stackoverflow.com/a/4060259
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

stream = open(os.path.join(__location__, 'sample.yaml'))
documents = load_all(stream, Loader=yaml.FullLoader)

print(type(documents))

for doc in documents:
    print(type(doc))
    print(doc['people'][1]['FirstName'])