" reference: http://candidtim.github.io/vim/2017/08/11/write-vim-plugin-in-python.html
" ready to import python files in python directory
let s:pluginRootDir = fnamemodify(resolve(expand('<sfile>:p')), ':h')
python << EOF
import sys
from os.path import normpath, join
import vim
pluginRootDir = vim.eval('s:pluginRootDir')
python_root_dir = normpath(join(pluginRootDir, '..', 'python'))
sys.path.insert(0, python_root_dir)
EOF

python << EOF
import main
EOF

let g:VimFormatterJsonIndent = 2
let g:VimFormatterXmlIndent = 2
exec 'let g:VimFormatterPythonStyle = "'.s:pluginRootDir.'/../config/yapf.cfg"'

function! Main()
    python main.main()
endfunction

command! -nargs=0 Format call Main()
