## K & R notes ##
* **module** : means a '.c'/'.cpp' file.
* **header file** : it usually is for prepocessor-use, including variable declaraion, macro and function prototype only, exluding definition/implemetation. For a module, it can be copy/paste at the fornt with *#include "header.h"* by the compiler in the preopcessor stage.
* **declaration** : means to declare a variable's type, without initializing/allocating the value/memory.
<<<<<<< HEAD
* **definition** : means to allocate the memory space for a varibale/function and initialize values/line-operation on them. Without a specified initialized value, the global variable is setted by 0 defaultly, and the local(automatic) variable is setted by trash-value(undefine behavior). Note that the definition of a variable/function can occur only once between modules, while the declaration can occur many times only if the type of them are the same.
=======
* **definition** : means to allocate the memory space for a varibale/function and initialize values/line-operation on them. Without a specified initialized value, the global variable is setted by 0 defaultly, and the local(automatic) variable is setted by trash-value(undefine behavior).
>>>>>>> 0751e3360885bc4bd7378ccdcb8f29433306f45f
* **automatic variable** : a synonym for *'local variable'*. The scope and liftime is in the block it defined.
* **external** : a keyword before a declartion to specify the variable be outside any function/block. It's a synonym for *'global'*. The scope of the external varibale is global between all modules for a program. The lifetime is along with the program it belongs.[https://en.wikipedia.org/wiki/External_variable](https://en.wikipedia.org/wiki/External_variable)
* **static** : static and extern are mutually exclusive. This is a keyword before a declaration of a local/global variable. It means this variable is 'static' or 'stick'. The scope is in the function-block/module, and the lifetime is along with the program.

## GCC compiler error ##
* "undefined reference to" : it usually means compiler find the function declaration but no definition. [http://ticktick.blog.51cto.com/823160/431329]

## Linux System Programming ##
* [http://www.cs.cf.ac.uk/Dave/C/]

## Macro ##
* va_list [http://www.cprogramming.com/tutorial/lesson17.html] 

## Pointer ##
* In C, pointer is exact a 'long int' for 8bytes, so (void*) is good enough to save the starting address,
* OS would take care what the real usage for the memory block that starts from the pointer.
* For normal usage, the address should generate by OS. Forcing read/write some specified address, ex.0x12345, would occur 'core-dump' crush. 
* ```pointer = null``` is a special case, null is 0. And 0 can't be read/write by program in normal cases.
* pointer to a struct
```
struct some {int a; int b; int c; double d}
```
* Implementaion of pointer in OS level(?)
    1. Compiler would save the offest from start address of "some" &some for 'b'(+4), 'c'(+4x2) and what the type is it(?)
    2. Comiler would optimize the memory layout - int whould save in the address of 4 multiple, double would save in 8. Thus there may be 4 wasting bytes between 'c' and 'd'.
    3. Thus we can parsing when we get a pointer(int address) whatever we want, but the behavior may be not expected - wrong value, core-dump, ..etc.

## Constructor ##
* [http://www.cprogramming.com/tutorial/constructor_destructor_ordering.html](http://www.cprogramming.com/tutorial/constructor_destructor_ordering.html)
* member initializer list : where m_nIdx(0) can equal to m_nIdx=0 
```
A(): m_nIdx(0), m_fNum(0.1), m_obj(objC) {}
```
* Woud m_obj(objA) call A()? or copy constructor of A?

## Standard Template Library (STL) ##
* ```for_each( ivec.begin(), ivec.end(), func_on_elements )``` ivec.begin() returns a iterator of a vector, func_on_elements is a function that apply on each element without modify their value.

## 140427 ##
/** C syntax **/
//main function prototype in GCC compiler for Linux
int main(int p_nArgc, char** p_aArgv)
  //we only need to input argument string list, the length of arg list would be determinated automatically,
  //.i.e, p_nArgc.
  //note that p_aArgv[0] is the file name of executable file
  $exe arg1 arg2

int main()
  //we can use this form if we don't need to input arguments
  //retrun 0 usually means "runtime is normal terminated", other value ,ex., -1, means not. 

//Copy string function
scpy()

//format output of printf()
  //%f is to print type 'double'/'float' in x.xxxx(default 6)
  //%e is to print type 'double'/'float' in x.e-x(default 6)
  //%g is to print type 'double'/'float' in %f or %e
  //standard C doesn't treat type 'bool', but we may use %d to print it
  $printf("%d\n", true);  
  >>1

// pointer
  //In C, pointer is exact a 'long int' for 8bytes, so (void*) is good enough to save the starting address,
  //OS(?) would take care what the real usage for the memory block that starts from the pter.
  //In normal usage, the address should generate by OS. Force to read/write some specified address , 0x12345 would occur 'core-dump'.
  //pter = null is a special case, null is 0. And 0 can't be read/write by program in normal cases.

// pointer to a struct
  //struct some {int a; int b; int c; double d}
  //the mechnism
  (1). Compiler would save the offest from start address of "some" &some for 'a'(+4), 'c'(+4x2) and what the type is it(?)
  (2). Comiler would optimize the memory layout - int whould save in the address of 4 multiple, double would save in 8. Thus there may be 4 wasting bytes between 'c' and 'd'.
  (3). Thus we can parsing when we get a pointer(int address) whatever we want, but the behavior may be not expected - wrong value, core-dump.....

/** CPP syntax **/
// For call-back registering, "function pointer" should save in a file/global scope, or static member function.
// not in a form of member function, otherwise, compile fail msg.....
build/src/bin/VMK_merge/VMK_merge.cpp:41:52: error: cannot convert ?oid (VMK_mergeApp_C::*)(int)??to ?_sighandler_t {aka void (*)(int)}??for argument ????to ?oid (* signal(int, __sighandler_t))(int)??


/*** 140509 add ***/
* fopen mode 
http://en.cppreference.com/w/c/io/fopen
File access 
mode string	 Meaning	 Explanation	 Action if file 
already exists	 Action if file 
does not exist
"r"	 read	 Open a file for reading	 read from start	 failure to open
"w"	 write	 Create a file for writing	 destroy contents	 create new
"a"	 append	 Append to a file	 write to end	 create new
"r+"	 read extended	 Open a file for read/write	 read from start	 error
"w+"	 write extended	 Create a file for read/write	 destroy contents	 create new
"a+"	 append extended	 Open a file for read/write	 write to end	 create new
File access mode flag "b" can optionally be specified to open a file in binary mode. This flag has effect only on Windows systems. 
On the append file access modes, data is written to the end of the file regardless of the current position of the file position indicator.


# vim: set ft=markdwon ai ts=4 et sw=4 sts=4:
