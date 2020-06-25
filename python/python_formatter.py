import vim

from abstract_formatter import AbstractFormatter


class PythonFormatter(AbstractFormatter):
    def __init__(self):
        super(self.__class__, self).__init__()
        yapfDir = self._getAbsPath(self._getRootDir(), "thirdparty", "yapf")
        self._yapf = "PYTHONPATH={}/build/lib/python {}/build/bin/yapf".format(
            yapfDir, yapfDir)

    def _getGuideFilename(self):
        # return self._getAbsPath(self._getConfigDir(), "yapf.cfg")
        return None

    def _getFormatCommand(self, formattedFilename, guideFilename):
        # cmd = '{} --style="{}" {}"'.format(self._yapf, guideFilename, formattedFilename)
        cmd = '{} {}'.format(self._yapf, formattedFilename)
        return cmd
