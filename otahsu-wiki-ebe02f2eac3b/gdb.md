## GDB ##
//ddd provide a GUI console for GDB
$ddd

//move cusor in UI
'Alt' + 'up'

//compile src in debug mode.
$scons -u --debug-build

//start gdb
$gdb
//end gdb
$quit //or 'ctrl+d'

//help
$ help list

//set the file for debugging
$file exe

//set the input arguments without argv[0]
$set arg arg1 arg2

//set local variable
$set var=1

//run the file
$run
$r

//show env
$show listsize
$set listsize 20
//show the arguments
$show args

//list current line
$l

//list filename(not enclude path) 
$list filename:num
$l filename:num
$l func_name
$l RegionFilter::TraverseCell
//list line number in the current file
$l 333

//set break-point
  //note that if we change the args, they can be used in the next runtime.
$b  //break at next line for the present.
$break func_name // no need args list.
$break aioLabelSetting_C::aioLabelSetting_C
$break line_num // on the line of the present list show file
$b 110
$break file_name:line_num

//condition break point.
//into the frame in labelFinder.cpp:129, and stop when the condition is True
br labelFinder.cpp:129 if m_ScanLine.IntersectedWith(ShapeSeg, pt) == 1
//note blank after if
br CutHitOperation_C :: AppendPntAry2Layer if (p_unLayerNum==127 && p_unDataType==0)

//info break-points
$info break
$i b

//delete the break point #num
$ delete 1 2 3 
$ del

//clear the break point of line #
$clear line

//continue to the next breakpoint or the end
$continue
$c

//step into the next line, diving into function
$step
$s

//step over the next line without diving into function
$next
$n

//see the current stack frame and the corresponding src 
$ frame
// up stack(corresponding to the order for bt list)
$ up 
// down stack(corresponding to the order for bt list) 
$ down
// last 2 frame(corresponding to the order for bt list)
$frame 2

//Continue running until just after function in the selected stack frame returns,
//print the returned value (if any), that is, "finish the stack frame?"
$finish

//get out of the loop
$until
$u

//Kill the child process in which your program is running under GDB.
$kill

//print variables
$print var
$p var
  //show the last var in some format(d=decimal)
  $p/d
//print the first n elements of an array.
print P@N
p *(Vector._M_impl._M_start)@N

//display a variable when program stops 
$disp var
$undisp

//watch a variable by it's address location, where '-l' is location.
//it breaks when the var value changes
$watch -l var
//a watch point is a break pt., it can be deleted by assigned number#
$info br
$delete num
$del

//see the current stack in the memory
$where

//shell cmd
$shell ls

//use sub-shell to prevent from bad 'cd'
$(cd xxx; pwd); pwd

// see where the program dead
$backtrace
$bt

// attach a running process to GDB, then GDB would take over this process.
$attach PID
or
//know pid by aux at first.
$ps aux | grep python2.7
$gdb -pid 7417

// A deleted pointer can access by GDB, while this would be unregtisted in OS.
// This block would be overwrited.