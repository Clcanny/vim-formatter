import collections
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise RuntimeError(
            "Please call {} with arugments: indent and filename.".format(
                sys.argv[0]))
    indent = int(sys.argv[1])
    filename = sys.argv[2]

    jsonDecoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
    infile = open(filename, "r")
    content = infile.read()
    infile.close()
    jsonDict = jsonDecoder.decode(content)
    content = json.dumps(jsonDict, indent=indent)
    print(content)
