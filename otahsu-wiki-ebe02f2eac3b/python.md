## 140427 ##

/** Python command **/
//command usage
$python2.7 [option] ... [-c cmd | -m mod | file | -] [arg]

//run cProfile module into that a script passing
//run library module, cProfile as a script
//'m' represents module. 's' represents sort.
//'>' is Linux amc that is to stdout to a file. 
$python2.7 -m cProfile -o <outputfile-name> <script-name> <options>
$python2.7 -m cProfile -s time ./transmission > profile.log
//sort by cumulative time
$python2.7 -m cProfile -s cumulative script.py

/** Python syntax **/
//get the argruments when running a python script
    import sys
    print sys.argv[0] # it's the py filename.
    print sys.argv[1] # it's 1st append argument.

//Indentation in Python
  //Python can auto-detect across lines in function arguements f(a1, a2), else need to add '\' to the line end.
  //Furthermore, ()and{} break the indetation rules.

//indexing operation []
  //it can apply on tuple, list and dictionary....
  >>>print list[1]
  >>>print tuple[1]
  >>>print dict['key']

//sequence objects(tuple,list) can be multiplied/added
[1]*3 == [1, 1, 1]
[1]+[2] == [1, 2]

//range(start[, end, step]) to generate list sequence
//note that end is never generated.
>>> range(0, 10, 3)
[0, 3, 6, 9]

//Passing arguments would be grouped into a tuple - args that has no keys or a dict - kw that has keys
def fun3(*args, **kw):
    print args
    print kw

fun3(1,2,key='g') # arg == (1,2) kw == {'key'='g'}

//* means break the outter () of a tuple
fun3(1,2) == fun3(*(1,2))

//** means break the outter {} of a dict
fun3(**{'key':'g'}) == fun3(key='g')

//dir() a list of valid attributes for that object by using __getattr__()
//the parent's attribute is visible in this.
dir(object) 

//object.__dict__ is the dictionary that save the object namspace and their values
//it doesn't include class data
//but does include class object instance data in if we use super(xx, self).__init__(*args)

//class data can be accessed from class object by __getattr__()
cobj = class()
assert(cobj.data == class.data)
//the class data is a static data
cobj.data = 2
assert(cobj.data == class.data)

//python don't create obj instance by assigning(=)
a = 1
b = a	#like a copy of pointer to a
assert( a is b)

//Floating point numbers are usually implemented using double in C

//python can return sequence objects, a tuple('1', '2') ar once
def fun1():
  retrun '1', '2'

//List in Python
	//the index from 0
  	//len(list): show the number of elements in the list
  	//the slice syntax list[n1:n2]: slice out list[n1] ~ ls[n2-1]
  	//list[-n] return the element of index = len(list)-n
    
    //list.insert(i, obj); insert a obj into the existing list at index i

//Dictionary in Python	
	//basic
	//for example, key is a string -'one'
	dict = {'one': 1}
	dict['one'] // return the dict value of key 'one'
	
	//get
	dict.get(key[,default]) // retrun the dict value of key if it has, else return default
	//pop
	dict.pop(key[,default]) // retrun the dict value of key if it has and delete it, else return default
	
//Import in Python
	//there are 3 levels: package(dictionary with __init__.py), module(.py file in a packge), variable or function(in a .py file)
	//import order would follow sys.path, where 'sys' means python system
	//sys.path; a list that stores the import modules order, and it can be modified. The default is as PYTHONPATH in Linux eniviroment settings
    //sys.modules; a dictionary that maps module names to modules which have already been loaded
	
    //import module
	import module_a		//execute module_a.py and copy the module name 'module_a' into the present module space.
	module_a.num = 2	//change the data in module_a
	
	//import module alias - as
	import module_a as a	//execute module_a.py and name it as 'a' into the present module space.
	a.num = 2			//change the data in module_a

	//from module import something 
	import module_a
	from module_a import num //execute module_a.py and copy module_a.num as 'num' into the present module space.
	print module_a.num
	>> 1
	num = 2			
	print module_a.num
	>> 1	//it didn' change the data in module_a
	from module_a import list // list = module_a.list
	print list 
	>> [1]
	list[0] = 2
	print list == module_a.list
	>> True					//because list is a mutable object, it
	
	//from module import * //copy all vars. in module into the present module space.  
 
    //python has math module, pow(x,y) is x^y
    >>import math.pow

//Build-in variables in a script module
  //__name__ is the name of the namespace
  //__file__ is the 'relative path' of the running script

//Build-in function in Python
    //sorted(iterable[, cmp[, key[, reverse]]]) - Return a new sorted list from the items in iterable.

//Python path
  //os.path module (refer to OS because of the file-system)
  //os.path.dirname(path), basename(path); returns dirname/basename of a path
  //os.path.abspath(path); returns the absolute path of a relative path
   
//Python string, note that string is a type of immutabel sequence.
  //Using '==' to compare values of strings
  //'is' is equalivant to compare id of 2 objects
  //'in' is to compare value of each object of an 'iterable' object
  >>> a = 'g8'
  >>> b = ''.join(['g','8'])
  >>> id(a) == id(b)
  False
  >>> a is b
  False
  >>> a == b
  True
  >>> a in ('g8', 'g9')
  True
  >>> b in ('g8', 'g9')
  True

//Python try-excpet
//sample code -
s1 = "Catch the exception, handle it then break the block."
s2 = "Continue the script execution."

def raise_error(error, detail):
    raise error(detail)

print "==== start try-except block ===="
try:
    pass
    #raise_error(ValueError, "VE")
    raise_error(ZeroDivisionError, "ZDE")
except ValueError as e:
    print e
    print s1 
except Exception as e:
    print "It's the base class of all exception. Thus it should be the last "\
            + "except-clause."
    print type(e)
    print s1
else:
    print "There is no exception in try-clause!"
finally:
    print "It would execute no matter if there is exception or not, "\
           + "thus it usually does such things like 'file close'."
print "=== end try-except block ===="
print s2

//if no error-handle for a certain error, the execusion stops.
Traceback (most recent call last):
  File "try.py", line 12, in <module>
    raise_error(ZeroDivisionError, "ZDE")
  File "try.py", line 6, in raise_error
    raise error(detail)
ZeroDivisionError: ZDE 

//File mode in Python
  //'w+' is write/read a new file and truncated old one from the started line.
  //'r+' is write/read a old file and truncated it from the started line.

/*** cx_freeze ***/
//to compile and package a python script along with a python run-time and the needed libraries.   
$cxfreeze gen_miniAIOLabel.py --target-dir ./

/*** 140509 add ***/
* flush the buffer of stdout.
```
import sys
print show_log_immediately
sys.stdout.flush()
```
* file flush to disk.
```
# fflush in libc.a -> write data to kernel buffer
# fsync in kernal -> write data from kernal to disk
try : 
    file.write(line)
    file.flush() 
    file_id = file.fileno() # get file descriptor id.
    os.fsync(file_id)
except :
    raise RuntimeError("fail to write_line_to_disk()!")
```

*view the last answer in IDLE, type underscore(_)
```
>>>_
```