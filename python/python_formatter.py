import vim
from abstract_formatter import AbstractFormatter


class PythonFormatter(AbstractFormatter):

    def __init__(self):
        super(self.__class__, self).__init__()
        yapfDir = self._getAbsPath(self._getRootDir(), "thirdparty", "yapf")
        self._yapf = "PYTHONPATH={}/build/lib/python {}/build/bin/yapf".format(
            yapfDir, yapfDir)

    def _getGuideFilename(self):
        # return vim.eval("s:VimFormatterPythonStyle")
        return None

    def _getFormatCommand(self, formattedFilename, guideFilename):
        guideFilename = vim.eval("g:VimFormatterPythonStyle")
        isort = "{}/build/venv/bin/isort".format(self._getRootDir())
        cmd = '{} --stdout "{}" | {} --style="{}"'.format(
            isort, formattedFilename, self._yapf, guideFilename)
        return cmd
