from json_formatter import JsonFormatter

import vim


def main():
    # TODO(junbin.rjb) Get filetype.
    name = vim.current.buffer.name
    if name.endswith(".json"):
        JsonFormatter().run()
    else:
        raise RuntimeError("Unknown filetype.")
