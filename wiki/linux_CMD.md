## Hot Keys ##
```
'ctrl' + 'alt' + 'F1' or 'F7'
'F12' //lock screen
```
## File system ##
* Absolute location can be added by'//'
* In Linux, file or dict name is not allowed to ' ', use'_' instead
layoutCan 1871 chhsuzt txt    REG   0,38 6243327 69397883 .nfs000000000422ed7b0000b5ba

* move or rename a dict
```
$ mv ./dict/ /home/newname/
```
* Rename a file name has white-space, '\' is escape character.
```
$ mv file\ with\ space new_path
```
* copy all ./*.pdf files to HOME dir
```
$ cp ./*.pdf ~/
```
* Copy the source to the target darget recursively
```
//'-r' means do recursively from the level of ./srcDir 
cp -r ./srcDir ./newDir // newDir will be created, ./srcDir/* will be copied under ./newDir
cp -r ./srcDir ./newDir/ // if newDir exists, ./srcDir/ will be copied under ./newDir
```
* Copy all files(exclue .hidden) under dict to current location
```
$ cp ./dict/* ./
```
* Copy link by no-dereference
```
$ cp -d links ./target
```
* Change directory to the home dir.
```
$ cd ~
```
* Show the tree structure of dictionarys
```
tree -d 
//show all files in some dict 
ls ./dict
tree ./dict
```
* Create a new directory
```
$ mkdir newdir
```
* Delete a dictinaory recursively
```
//'-r' means do recursively from the level of ./dict
//'f' means by force, never 'prompt' even if the file doesn't exist.
$ rm -rf ./dict/
```

* Permission of a file/direction
```
//For dir, 'r' is to 'ls' the file/dir belong to it,
//'w' is to 'rm/mv' the file/dir belong to it
//'x' is to 'cd' to the dir
//For file, 'r' is to 'cat' it, 'w' is to 'sed' it, 'x' is to excute it. 
//change user permission of a file
//user= u(user), g(group), o(others) ,a(all)
//note that here user is the owner of the shell, i.e., chhsuzt.
//operation= +, - , =
//permission= r, w, x(executable)
$ chmod a+x filepath
//or setting at once user|group|others = rwx|rwx|rwx
$ chmod 744 filepath //means user=(111)can rwx, group=(100)can read only
$ chmod 755 test 
$ ll test
>>-rwxr-xr-x 1 chhsuzt opc  774 Feb 23 09:35 test
//note that the 1st character is '-' or 'd', that means dictionary or not.
// add sticky-bit onto a dir(not file)
// it forces to dis-allow everyone but Owner to mv/rm the dir and file under 1-level of this dir,
$ chmod o+t ./new
$ chmod 1775 xxx
$ ls 
drwxr-xr-t  2 chhsuzt opc 4096 Sep 13 14:44 new
$ chmod o-t ./new
$ chmod 0775 xxx
```

* ls that sort by size
```
ls --sort=size
```

* Open a null file or update an existing file.
```
$ touch x
```
* link 
    * make a soft(symbolic)-link to a file/dictionary
```
$ ln -s file link
-rw-r--r-- 1 chhsuzt opc         0 Dec 26 14:32 dict
lrwxrwxrwx 1 chhsuzt opc         6 Dec 26 14:32 link -> dict
```
* remove the link
```
$ unlink link
$ rm link
```
* copy link
```
//'-d' same as --no-dereference --preserve=link
$cp -d link /new/
```

## Avaliable servers ##
* OPC 2-2 big RAM server - 3cb0402
* To login public server - ALPS_1F is preferable for OPC2 //ALPS_1F_TZ is for OPC2&3(C3246 C4254 i1004)
* Recipe power CPU c7240~7243 7245~6
* IP naming rule: 140.10.4w.xyz = cwxyz 
```
$ rlogin c0105, c205x 
$ rsh c2003 
$ ssh opc_cb@c0105 //Secure Shell protocal, need to key in ID/pass to generate public and private key
$ rlogin c0105 -l opc_cb
```

## Linux apps usage ##
* kpdf
* kdevelop
* tkdiff
* xemacs
* hg(Mercurial)
* thg(GUI Mercurial)
* eog(eye of gnome)
* convert(convert figure files app in ImageMagick)	 	
* gs(powerful image tool in Linux)
* oocalc(excel of open office)
* scrot
    //screen copy from server1 to server2
    1. type 'scrot' on terminal
    2. use white rectangle to quote the region you want to snapshot
    3. your snapshot is in the calliboard, paste it if you want

## TCSH ##
* we use tcsh as our 1st terminal shell for default usage 
* to see the version of Linux
```
$ cat /etc/redhat-release
Red Hat Enterprise Linux WS release 4 (Nahant Update 4)
```
* merge path and set itset
```
$ setenv setpath = {path1 path2 ... $PATH}
path1/path2/$PATH
//PATH is a constant name, $(dollar star)
```
* generate new rsa key for a account
```
$ ssh-keygen -t rsa
$ ll ~/.ssh/
id_rsa.pub
```
* see the ip config in the host
```
$ /sbin/ifconfig
```
* monitor the port status in the host
```
$ netstat
```
* check the connection with a certain server
```
$ ping c0105
```
* logout from remote
```
$ logout
'ctrl' + 'd'
```
* exit the terminal
```
$ exit
'ctrl' + 'd'
```
* echo the return code
```
$ echo $?
```
* show the system time
```
$ date
```
* Load enviroment setting from starup
    * Linux system enviroment default setting is under /etc/, ex. /etc/bashrc
    * When login, Linux execute cshrc(C shell resource control) to configure automatically
    ```	
    $ source ~/.cshrc  // and it calls $ ~/.my
    ```
    * Each setting would overwrite the setting before -
    A login shell begins by executing commands from the system files /etc/csh.cshrc and /etc/csh.login. 
    It then executes commands from files in the user's home directory: first ~/.tcshrc (+) or, if ~/.tcshrc is not found, ~/.cshrc, then ~/.history (or the value of the histfile shell variable), then ~/.login, and finally ~/.cshdirs (or the value of the dirsfile shell variable) (+).
    The shell may read /etc/csh.login before instead of after /etc/csh.cshrc, and ~/.login before instead of after ~/.tcshrc or ~/.cshrc and ~/.history, if so compiled.
    * For using sombody's AP without installing, you can source somebody's .cshrc 
    ```
    $ source /ban/cclinzzp/.cshrc
    ```
* The path of a app
```
$ which gitk
/ban/ylchenzr/usr/local/x86_64/bin/gitk
```
* Look the enviroment setting in the present terminal
```
$ env
```
* Add a variable to the shell enviroment
```
$ setenv new
```
* Unset a variabel to the shell env.
```
$ unsetenv new
```
* Changing the 'DISPLAY' in env
```
$ setenv DISPLAY 10.40.247.105:0
```
* Launch an app in the background
```
$ apName &
```
* Put frontground ap in the background
```
'Ctrl+Z' //pause(Suspended) the current process 
$ bg
$ fg // put bk app to the fg.
```
* Read 'less' mannual of some linux bin
```
$ man grep
```
* Find help massage of some app
```
$ appName -help
```
* List all history of command in a terminal shell
```
$ history
```
* Clear the command in a terminal shell
```
$ clear 
```
* Stream out the output message to a file
```
$ history > file.txt
```
* concatenate, output to standard-out in once
```
$ cat x
```
* merge 2 stream file
```
$ cat file1 file2 >> merge.txt
```
* more, output once a page(only can pagedown by 'space') 
```
$ more x
```
* less, output once a page, can pagedown and pageup
```
$ less x
```
* print out only selected line number
```
$ cat log | sed -n '6118,10938p' > purify.log
```
* print the last lines of xxx file.
```
$ tail -n 50 xxx 
```

* Redirect file descriptor. Note that '0' is stdin, '1' is stdout, '2' is stderr.
    * in BASH,
    ```
    $ echo "redirect stdout to stderr" 1>&2
    ```
    * In TCSH, if we want to echo string correctly, we need BASH's help
    ```
    $ sh -c 'echo "msg" 1>&2'
    ```
    * In TCSH, redirect stderr to stdout then output to a log file
    ```
    $ ap >& err.log
    ```
	* redirect stderr to a file.
	```
    $ sh -c 'scons 2>err.log'
    ```
    * redirect stderr to stdout and to a file.
    ```
    $ sh -c 'scons >err.log 2>&1'
    ```
    * 'tee' is read/write from stdin to stdout and file at the same time.
    ```
    $ sh -c 'scons 2>&1 |tee err.log'
    * redirect stderr to a file by swapping stderr and stdout, keeping display still - create 3 as the same as 1, assign 1 as 2, assign 2 as 3(3=1;1=2;2=3).
    ```
    $ sh -c 'scons 3>&1 1>&2 2>&3 | tee  err.log'
    ```
    * discard stderr and stdout 
    ```
    $ xxx 2>&1 >/dev/null
    $ xxx & >/dev/null
    ```
    * discard stdout
    ```
    $ xxx > /dev/null
    $ xxx 1 > /dev/null
    ```

## List CMD ##
* List files in details. Note the file size is in Byte, "total" shows the size in KB in the pwd.
```
$ ll
```
* List files in human readable format, that the size would be in KB, MB... 
```
$ ll -h
```
* List veiw all including hiden files
```
$ ls -la
```
* List dic only
```
$ ld
$ ls -d
```
* List files that sort by modification time(mtime)
```
ls -lt
ll -t
```
* Most used 
```
$ ls -ltr
```
* Count the newline symbol of the list result(`l` is line).
```
$ ls | wc -l
```
* wc(word count?) //print the number of newlines, words, and bytes in files
```
$ wc README 
  2  25 177 README
```

## System Tools(Process, Disk...) ##
* Monitor the workstation
[http://wiki.linux.org.hk/wiki/index.php?title=Monitor_processes_with_top&variant=zh-tw]
*“TIME+” fomat is minutes:seconds.hundredths ? The time value seems non-reasonable.
```
$ top
//press 'u' terminal will ask you Which user 
//press 'q' will stop monitor
//press 'k' can kill job
//press '1' can show CPU cores info.
//press 'c' toggle full command.
//State of process
'D' = uninterruptible sleep
'R' = running
'S' = sleeping
'T' = traced or stopped //attched by GDB now
'Z' = zombie
```
* free (check the memory/CPU cached status)
```
//free -b,-k,-m,-g show output in bytes, KB, MB, or GB
$ free -g
             total       used       free     shared    buffers     cached
Mem:           504        503          0          0          0        419
-/+ buffers/cache:         84        419
Swap:           36          0         36

//for this case, 'free' represents 'GB' for L1~3 cached(SRAM) and 'buffers' represents 'DDR-RAM'. The HW information is in mother-board.
```

* VIRT, RES, SHR
```
VIRT(total mem size for a process) stands for the virtual size of a process, which is the sum of memory it is actually using, memory it has mapped into itself (for instance the video card’s RAM for the X server), files on disk that have been mapped into it (most notably shared libraries), and memory shared with other processes. VIRT represents how much memory the program is able to access at the present moment.

RES(physical mem size) stands for the resident size, which is an accurate representation of how much actual physical memory a process is consuming. (This also corresponds directly to the %MEM column.) This will virtually always be less than the VIRT size, since most programs depend on the C library.

SHR(shared mem size with other process) indicates how much of the VIRT size is actually sharable (memory or libraries). In the case of libraries, it does not necessarily mean that the entire library is resident. For example, if a program only uses a few functions in a library, the whole library is mapped and will be counted in VIRT and SHR, but only the parts of the library file containing the functions being used will actually be loaded in and be counted under RES.
```

* Monitor user's processes
```
$ top -u chhsuzt
```
* Note that some .nfs files will be created when an open file is removed but is still being accessed!!
* lsof can dump the information of the .nfs file, but only for the server that open bin and create .nfs
```
$ lsof .nfs
COMMAND    PID    USER  FD   TYPE DEVICE    SIZE     NODE NAME
```

* capture all processes status and show the user
```
$ ps -A u
```
* capture all processes on the server
```
$ ps aux
```
* capture my processes
```
//'l' is long
ps -l 
```
* cpature the process tree of some user
```
//'a' is to show command arguments
$ pstree chhsuzt -a 
```
* kill some process whose PID = xx
```
$ kill -signal PID
//kill in normal
$ kill -SIGTERM a
$ kill -15 a
//kill by force
$kill -SIGKILL a
$kill -9 a
```
* restart a terminated process
```
$ kill -SIGHUP a
$ kill -1 a
```
* Exit the "dead run" in command line
```
'Ctrl' + 'C' 
```
* Disk Quota - du (disk usage?)
    * list all files under a dir
    ```
    $ du -a ./
    ```
    * summarize total size in human readable 
    ```
    $ du -sh 
    ```
    * depth of sub-dict
    ```
    $ du -h --max-depth=1
    ```
    * exculde a dir
    ```
    $ du -h --exclue=/path/to/dir --exclude=./log
    ```
    * Retreive the number of files that have name "griffey*" under PWD
    ```
    $ du * | grep griffey | awk '{sum+=$1}END{print sum}'
    ```
* Check the system mounted disk, df(disk free?)
    * check the quota of /vol0/ 
    ```
    $ /vol0/sys/tool/df4 -h
    ```
    * mount on '/' is 'root'
```
$ df -h /home/opc/chhsuzt
Filesystem            Size  Used Avail Use% Mounted on
/dev/sda3             421G  246G  155G  62% /
```
* rsync (a backup tool to keep file's properties)
    * rsync src dict to target. 'r' is recursive, 'u' is update, 'a' is all, 'l' is link to copy symlinks as symlinks, and 'v' is verbose. Note '/' is to avoid to create src/ to target/src/ again. It has no "delete" action. If target is not empty, the old files would be kept!
    ```
    $ rsync -rlu src/ target/
    ```
    * To avoid the "/opc_cb/.*" hidded dir, ex. .git/
    ```
    $ rsync -a /opc_cb/* /target/
    ```
    * Include "delete" action, sync src/ tp target/ . Note that --delete wouldn't act if '*' used in the path!
    ```
    $ rsync -a --delete src/ target/
    ```
    * Exclude a sub-dir by using the relative path
    ```
    $ rsync -a --delete --exclude ".git/" src/ target/
    ```


* cron, to run jobs periodically by the current account
```
$ crontab -l #list all jobs
$ crontab -e #edit 
```
* NetWork
    * capture the net state of the current server
    ```
    $ netstat -lntap //'l' is listen, 'n' is ip:port number, 't' is tcp package, 'a' is list all, 'p' is PID/Program
    ```
    * cature the net state of current server including 'socket' for communication of local processes.
    ```
    $ netstat -a //'a' is to list including 'connect', 'listen' and 'socket'
    ```		
    * Query visible host names.
    ```		
    $ qhost
    ```
* Hardware information
    * CPU information
    ```
    $ cat /proc/cpuinfo
    ```
    * Memory info
    ```
    $ cat ./proc/meminfo
    ```
    * PCI device information	
    ```
    $ /sbin/lspci
    ```
    * issue?
    ```
    $ cat /etc/issue
    ```

    
## Tar and Zip ##
* Create a compressed archive(note that whiout using gzip, it only 'pack' to an archive)
```
$ tar czvf filename.tgz dir //c=create, z=use 'gzip' to compress, v=verbose, f=filename, x=extract(expend)? files
```
* Expand a compressed archive to pwd
```
$ tar xzvf filename.tgz
```
* Expand a compressed file to dest dir
```
$ tar xzvf filename.tgz -C dest //C is change to dictionary
```

## ELF(excutable linkabel format) ##
* To see the file-format of a file
```
$ file libboost_chrono.so.1.48.0
libboost_chrono.so.1.48.0: ELF 64-bit LSB shared object, AMD x86-64, version 1 (SYSV), not stripped
$ file test_spectrum.py
test_spectrum.py: ASCII English text
$ file exe 
exe: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x6b1c428f682d2a237c9fe4166f2c63f06c7d0d51, not stripped
```
* Check the symbol table for non-removable .nfs file
```
//'-s' means symbol.
$ readelf -s .nfs00000000040fd5880000133d | less
// '-t' means table.
$ objdump -t .nfs000000000457dd4900000e8c | less
```

## Shebang(sha-bang) ##
  //it's fist 2 ANSI characters,"#!", of a script file for specified interpreter.
  //for ex., we like put in the 1st line of "/path/a.py"
    #! /usr/bin/python
    //It is equal to shell cmd as if "/path/a.py" is the 1st argument.
    $/usr/bin/python /path/a.py 
  //for portable issue, we like put in the 1st line of "a.py"
    #! /usr/bin/env python
    //env is a symbolic link of a shell script.
    //It is equal to shell cmd as if we pass 2 arguments to 'env'
    $/usr/bin/env python a.py
  //note that Shebang has some conditions
  //(1). It should be in 1st line of a script.
  //(2). It can only be in 1 line length.
  //(3). It should assign a 'absolute' path.


## FTP ##
* Note that the password mechanism may diff from rlogin
* login, then key-in userID and Password.
```
$ ftp i1004
```
* change dictionary
```
ftp> cd /pd1/
```
* list files
```
ftp> ls -ltr
```
* change to binary mode
```
ftp> bin
200 Switching to Binary mode
```
* Turn-off the interactive mode
```
ftp> prompt
Interactive mode off.
```
* upload files to the remote
```
ftp> put filname
```
* download files from remote to local dictionary in multi-task
```
ftp> mget *.*
```
* "ctl+z" to suspend ftp, then when we want it, forward ground it
```
ftp> fg
```
* logout FTP
```
ftp> bye
'CTRL' + 'd'
```
* Display local directory listing
```
$ lls  
```
* Print local pwd
```
$ lpwd
```

## Misc ##
* merge several pdf files to one
```
$ gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=CEM_ch1.pdf -dBATCH CEM_1.pdf CEM_2.pdf
```
* run slitho whith open-mp in multi-thread mode.(on c7241 16 cores)
```
$ slitho -omp 16
```

* mkdir
```
mkdir -p, --parents: no error if existing, make parent directories as needed
cp -p: preserve the specified attributes (default:mode,ownership,timestamps)
```

* Monitor the memory status
```
-g is in giga, -t is for total
$ free -g -t
```

## Linux Tools for ELF ##
* Notify System default PATH
```
$PATH // tell Linux where to find excutable file.
$LD_LIBRARY_PATH // tell Linux where to find dynamic link library(.so) and static library(.a)? This name is specified by GCC?
```
* archive .o files into a static lobary.
```
// 'c' is create, 'q' is quick append file, 's' is to index(symbol-table) that is eqaulivant to 'ranlib' 
$ar -cqsv libtest.a main.o
```
* dump out the header of a .obj file 
```
$objdump -h main.o
```
* ldd (ld linker dependency?) - print the names of dependent .so of a executabele/.so file
```
$ldd ./so
```

* nm - print out the symbol table of a file
```
$nm -A file
```

# vim: set ft=markdwon ai ts=4 et sw=4 sts=4 tw=105:

