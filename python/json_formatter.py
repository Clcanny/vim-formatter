from abstract_formatter import AbstractFormatter


class JsonFormatter(AbstractFormatter):

    def __init__(self):
        super(self.__class__, self).__init__()

    def _getGuideFilename(self):
        return None

    def _getFormatCommand(self, formattedFilename, guideFilename):
        return "python2.7 {} {}".format("{}/format_json.py".format(self._getCurrentDir()), formattedFilename)
        # pycode = " ".join([
        #     "import collections;"
        #     "import json;",
        #     "jsonDecoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict);",
        #     "infile = open(\"{}\", \"r\");".format(formattedFilename),
        #     "content = infile.read();",
        #     "infile.close();",
        #     "jsonDict = jsonDecoder.decode(content);",
        #     "content = json.dumps(jsonDict, indent=2);",
        #     "print(content);"
        # ])
        # pycode = pycode.replace("\"", "\\\"")
        # pycode = "\"{}\"".format(pycode)
        # return "python2.7 -c {}".format(pycode)
