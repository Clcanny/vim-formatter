import vim
from bash_formatter import BashFormatter
from cmake_formatter import CMakeFormatter
from cpp_formatter import CppFormatter
from json_formatter import JsonFormatter
from python_formatter import PythonFormatter
from xml_formatter import XmlFormatter


def main():
    filetype = vim.eval("&filetype")
    if filetype == "json":
        JsonFormatter().run()
    elif filetype == "xml":
        XmlFormatter().run()
    elif filetype == "sh":
        BashFormatter().run()
    elif filetype == "python":
        PythonFormatter().run()
    elif filetype == "c" or filetype == "cpp":
        CppFormatter().run()
    elif filetype == "cmake":
        CMakeFormatter().run()
    else:
        raise RuntimeError("Unknown filetype.")
