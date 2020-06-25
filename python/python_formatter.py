import vim
from abstract_formatter import AbstractFormatter


class PythonFormatter(AbstractFormatter):

    def __init__(self):
        super(self.__class__, self).__init__()
        self._yapf = self._getAbsPath(self._getRootDir(), "build/venv/bin/yapf")
        self._isort = self._getAbsPath(self._getRootDir(),
                                       "build/venv/bin/isort")

    def _getGuideFilename(self):
        # return vim.eval("s:VimFormatterPythonStyle")
        return None

    def _getFormatCommand(self, formattedFilename, guideFilename):
        guideFilename = vim.eval("g:VimFormatterPythonStyle")
        cmd = '{} --stdout "{}" | {} --style="{}"'.format(
            self._isort, formattedFilename, self._yapf, guideFilename)
        return cmd
