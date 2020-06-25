import sys
import collections
import json

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise RuntimeError("Please call format_json.py with arugments: indent and filename.")
    indent = int(sys.argv[1])
    filename = sys.argv[2]

    jsonDecoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
    infile = open(filename, "r")
    content = infile.read()
    infile.close()
    jsonDict = jsonDecoder.decode(content)
    content = json.dumps(jsonDict, indent=indent)
    print(content)
