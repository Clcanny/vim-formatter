import vim
from bash_formatter import BashFormatter
from cmake_formatter import CMakeFormatter
from cpp_formatter import CppFormatter
from json_formatter import JsonFormatter
from python_formatter import PythonFormatter
from xml_formatter import XmlFormatter


def main():
    # TODO(junbin.rjb) Get filetype.
    name = vim.current.buffer.name
    if name.endswith(".json"):
        JsonFormatter().run()
    elif name.endswith(".xml"):
        XmlFormatter().run()
    elif name.endswith(".sh"):
        BashFormatter().run()
    elif name.endswith(".py"):
        PythonFormatter().run()
    elif name.endswith(".h") or name.endswith(".cpp"):
        CppFormatter().run()
    elif name.endswith("CMakeLists.txt"):
        CMakeFormatter().run()
    else:
        raise RuntimeError("Unknown filetype.")
