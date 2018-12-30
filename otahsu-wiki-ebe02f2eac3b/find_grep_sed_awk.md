## URL link ##
[http://content.hccfl.edu/pollock/unix/findcmd.htm](http://content.hccfl.edu/pollock/unix/findcmd.htm)
[http://www.openfoundry.org/tw/foss-programs/8628--linux-](http://www.openfoundry.org/tw/foss-programs/8628--linux-)
* VBird - [http://linux.vbird.org/linux_basic/0330regularex.php]
## find ##
* Note that it support glob syntax(* wildcard) like 'ls', not regrex!!
* find the filename "*.py" in the current dict recursively
```
//find [PATH] [option] [action] 
$ find ./ -name ".py" 
```
* find files for certain time : atime = access time, ctime = chmod time, mtime = modify time when content has been modified 
```
//find files are modified between 1~2 * 24hr by now.
$ find ./ -mtime 1 
//find files are modified before 5 * 24hr by now. 
$ find ./ -mtime +4 
//find files are modified by 4 * 24hr before to now.
$ find ./ -mtime -4 
```
* find some dictionary then remove it. 
```
//type can be d(dict), f(file), l(link) 
$ find ./ -type d -name "sub" -exec rm -r '{}' + 
```
* find some file exclusively then remove it. '!' is the exclusive operator preceding -xxx option opertator. Note that the dir hierachy need to be kept in this case. 
```
$ find ./ -type f '!' -name "*.txt" -exec rm '{}' +
```
* Find xxx.log and cat all of them.
```
$ find ./ -name "*.log" -exec cat '{}' +
```
* Find all nulll file in PWD then mv them to etc/. -maxdepth = search depth of dir, where 1 is to the PWD. 
```
$ find ./ -maxdepth 1 -type f -size 0 -exec mv -t etc/ '{}' +
```

## grep ##
* grep support RE, not glob wildcard.
* Find files that contain a string. -l = switch outputs only the names of files in which the text occurs. -i = switch ignores the case, -r = into recursive subfolder, -n = show line number, -I = ignore the binary files.
```
$ grep -lirn "string" ./filename
```
* Pipe command -  receive the stdout of the last command as input.`grep` is a pipe command. 
```
The syntax is like: 
cmd | pipe-cmd | pipe-cmd2 
```
* An example -  
```
//show only the result line number that have "abc" in .c files 
$ find ./ -name "*.c" | grep -irn "abc" | more
```
* grep the "function name" in .h files, it's fast!!
```
$ find ./ -name "*.h" | xargs grep -irn "GetTopCellByIndex"
./HOPE/db/toDB.h:64:               Cell_C*  GetTopCellByIndex(unsigned int p_nIdx);
```

## sed ##
* sed support RE
* delete blank line in a file. -i = directly modfify file. '^' is at line start, '$' is at line end, 'd' is delete.
```
$ sed -i '/^$/d' file
```
* in RE, '.' is one char that can be any, '*' is not wildchar but repeat previous char for any times including 0 time.
```
$ sed -i '/^.*$/d' file
```
* Search and replace - like vim 
```
$ sed -i `s/old/new/g` file
```

## awk ##
* parse for 1st augment of a line text, splitted by ' '
```
$ cat xx | awk '{print $1}'
```
* split by '.'
```
$ awk -F\.
```

/** 140425 cleaned **/

# vim: set ft=markdown ai ts=4 et sw=4 sts=4:
