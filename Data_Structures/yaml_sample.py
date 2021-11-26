import os, yaml
from yaml import load, load_all

# User realpath to reliably use the file in the same directory as the script
# Source: https://stackoverflow.com/a/4060259
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

