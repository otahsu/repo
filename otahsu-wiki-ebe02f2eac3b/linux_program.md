[markdown syntax](http://markdown.tw/)

## CodeBeamer ##
* task should be submmitted by a submiter
* task can be assgined to a worker.
* task should have a owner.

## GVIM ##
* ~/.gvimrc config the gvim, execute automatically when you run gvim 

* set the gvim enviroment in a .py file
```
# vim: set ft=python ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=79:
//ft is "file type", ff is "file format", fenc is "file encode", ai is "auto indent"
//et is "expand tab"(instead 'tab' with numbers of 'space')
//nu is "number"(show line number)
//ts is "tab stop"(numbers of 'space')
//tw is "text width"
```
* folding indenting lines
```
:set foldmethod=indent
zi      "啟用/關閉折疊

zo      "打開折疊
zc      "關閉折疊
zO      "打開所有折疊
zC      "關閉所有折疊

zx      "更新折壘，即除了游標所在折疊不關，其他都關掉
```

* jump to TCSH, use it's cmd, ex. ls. ```:!ls```

* split the window ``` 'ctrl + w' then 'ctrl + s' ```

* Get into 'insert' mode ```i```
* Get into 'replace' mode ``` 'shift + r' ```

* open a vi window. ```$ gvim main.c```

* open all .py files in PWD ```$ gvim *.py -p```

* see the PWD (present working dictionary) ```:pwd```

* Get help information for vi cmd ```:help cmd```

* open a file in a horizontal split ```:sp filename```

* open a file in a new tab(tab edit) ```:tabe x.c```

* open *.c files in new tabs ```:tabe *.c -p```

* move the tabe to nth tab(start from 0) ,without n it moves to the lase.
```
:tabm n
```

* go to the next tab, it will wrap around.
>in visual-mode
```
gt
```

* edit the file
```
:e filename
```

* reload the file
```
:e
```

* format the highlighted line in visual-mode
```
gw
```

* copy and paste in clipboard(it can cross app, even OS)
>"+y for copy.
>"+p for paste on the next line of current cusor.

* copy and paste in visual mode(?the buffer is?) 
>select the region, and then click 'middle'

* yank copy # lines after cusor(include cusor line)
```
#yy
```

* delete # lines after cusor
```
#dd
```

* delete line1 ~ line3
```
:1,3d
```

* copy line1 ~ line3 to the next line of line5
```
:1,3co 5
```

* move select chop
```
:1,3mo 5
```

* delete character on cusor
```
x
```

* Move curusor to the next/last word by direction key
>'ctrl'+'LEFT' //move to last word
>'ctrl'+'RIGHT' //move to next word
>'UP' //move to last line with the same column
>'DOWN' //move to next line with the same column

* Move to the start of a line.
>0

* Move to the end of a line.
>$

* next word
>w

* last word
>b

* last word escape blanks.
>1B

* change case of a character
>~

* Next 2 word that escape blanks. note that 'norm' is in normal mode.
>2W
```
:norm 2W
```

* Move cursor to the #num of colummn
>2|
```
:norm 2|
```

* Move cursor to line 2 and coulum 20
```
:norm 2G20|
```

* Move cursor to line 2 and word 2
```
:norm 2G3W
```

* yank Paste on the next of cusor line
>p

* yank Paste on cusor line
>P

* find "context"
>press '/', and 'n' for next place, 'shift'+'n' for previous place
>press '?', and 'n' for previous place, 'shift'+'n' for next place
>press 'shift'+'3' to wrapped the word and fing it in the previous place

* find the same 'word' where the cursor is on
>'*' to search forward 
>'#' to searchbackward

* replace string, e.g., replace "s1" to "s2" between line1~20
>$ reprsent end line of file
>^ reppresent start of a line
>ctrl+'i' represent tab 
```
:1,20s/s1/s2/gc
```  
>or you can find and replace in the whole file
```  
:%s/s1/s2/gc
```

* undo, redo
>in visual-mode,
>'u' undo last change (can be repeated to undo preceding commands) 
>'Ctrl'+'r': Redo changes which were undone (undo the undos). 

*　select visual block
>in visual-mode,
>'click'+'Ctrl+V'+'drag' 

* block insert, note that the insert point is one left grid before insert cusor
>'shift'+'i'

* epscape from visual block
>'esc'

* Move cursor to the number(num) of line
num + 'G'
  ```
  :num
  ```

* go to the 1st line
>'gg'

* go to the last line
> 'G'

* visual selection
>'v' at the start line then 
>'nG' go to the line n for the selection

* use visual selection to copy/paste in clippboard
>'v'
>'nG' move cursor to nth line; or '}' go to next paragraph; or up/down button
>"+y
>"+p

* identation fowoard or backwoard
>'shift+>>' or 'shift+<<'

* marks that can live in the scope of an instance that has many tabs
>mark in the current tab as lowercase a-z
>ma

* mark int the current instanse as uppercase A-Z
>mA

* show all mark list
> marks

* delete mark a
> delm a

* jump to previous context mark
>'

* move to mark a
>'a

* move cursore(go) to certain line in normal|visual mode
  ```
  'gg' go to the start of a file
  'G' go to end of file
  'nG go to line n
  '{' go backward a 'paragraph'
  '}' go forward one 'paragraph'
  '[' go to next 'block'
  ']' go to last 'block'
  ```

* folding
  ```
  //folding the same indentation.
  #vim: set foldmethod=indent#
  //default hot-key
  za: toggle the current fold
  zc: close folding
  zo: open folding
  ```
  
* move cursor
  ```
  'h' left
  'l' right
  'j' down
  'k' up
  ```

* split-window
  ```
  'ctrl+w'+'j' down split
  'ctrl+w'+'k' up split
  ```
  
* open the selected split wnd in a new tab.
  ```
  <Ctrl-w>,'T'
  ```

* enable/disable to show '\tab' EOL..
  ```
  :set list
  :set nolist
  ```

## Ctags and Cscope ##
* build tag recursive
```
$ctags -R
```
* Vi will, by default, expect a tag file by the name "tags" in the current directory. To use 'tags' builded in the top repository level, need to open .cpp in the top level.

* jump into the function definition
```
'ctrl' + 'Left-Mouse'
'ctrl' + ]
```

* back to the previous state
```
'ctrl' + 'Right-Mouse'
'ctrl' + t
```

* open tag in a split window
```
<Ctrl-w>, <Ctrl-]>, choose tag
```
* open tag in a new tab
```
<Ctrl-w>, <Ctrl-]>, choose tag, <Ctrl-w>,'T'
nnoremap <silent><Leader><C-]> <C-w><C-]><C-w>T
```

* c72xx has installed it. It's a code project parser that can enhance vim.
```
$cscope -h
//build library
$cscope -Rbkq
//add '.cpp' into cscope visibilty.
find ./ -name "*.h" -o -name "*.cpp" -o -name "*.c" >> cscope.files
//put key-map file 'cscope_maps.vim' into ~/.vim/plugin
//nmap <C-@> is map 'Ctrl'+'2' to ':csc'
```
```
add library with its location.
:cs add cscope.out /ban/chhsuzt/griffey/src 
```



//TODO: add 140430
## SCons ##
* See scons dependency tree 
```
$ scons -u --no-exec --tree=all,status // '-n' is don't build.
$ scons -u --no-exec --tree=derived //skip .h and .cpp, view .o only
```
* See scons log
```
$ scons -u --debug=explain
```
* ? what's .sconsign.dblite
```
The .sconsign.dblite file is a temporary database used by SCons to keep file signatures to speed up future builds. If you delete it, SCons will recreate it.
```
* dump .sconsign.dblite ('t' is timestamp, 'i' is implicit info, 'r' is read timestamps)
```
$ sconsign -atir .sconsign.dblite
```
# vim: set ft=markdown ai ts=4 et sw=4 sts=4:
