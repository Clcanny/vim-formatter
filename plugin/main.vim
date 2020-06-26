" reference: http://candidtim.github.io/vim/2017/08/11/write-vim-plugin-in-python.html
" ready to import python files in python directory
let s:pluginRootDir = fnamemodify(resolve(expand('<sfile>:p')), ':h')
python3 << EOF
import sys
from os.path import normpath, join
import vim
pluginRootDir = vim.eval('s:pluginRootDir')
python_root_dir = normpath(join(pluginRootDir, '..', 'python'))
sys.path.insert(0, python_root_dir)
EOF

python3 << EOF
import main
EOF

" Refer to davidhalter/jedi-vim.
" Settings initialization.
let g:VimFormatterJsonIndent = 2
let g:VimFormatterXmlIndent = 2
exec 'let g:VimFormatterPythonStyle = "'.s:pluginRootDir.'/../config/yapf.cfg"'
let g:VimFormatterBashIndent = 4
" See beautysh documentation.
let g:VimFormatterBashFuncStyle = "fnpar"
let g:VimFormatterCppStyle = {
    \ "IndentWidth": 4,
    \ "TabWidth": 4,
    \ "AccessModifierOffset": -3,
    \ "SpacesBeforeTrailingComments": 2,
    \ "PointerAlignment": "Left",
    \ "AlwaysBreakTemplateDeclarations": "true",
    \ "SortUsingDeclarations": "true",
    \ "FixNamespaceComments": "true",
    \ "AllowShortFunctionsOnASingleLine": "false",
    \ "BinPackArguments": "false",
    \ "BinPackParameters": "false",
    \ "AlignAfterOpenBracket": "true"
    \ }
let g:VimFormatterCMakeStyle = {
    \ "enable-sort": "True",
    \ "autosort": "True",
    \ "max-pargs-hwrap": 2
    \ }

function! Main()
    python3 main.main()
endfunction

command! -nargs=0 Format call Main()
