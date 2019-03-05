## gcc/g++ compiler##
* gcc compiler compile *.c file(module) once at a time.
```
$> gcc -c a.c 
```
<br>
The output is 'a.o'. '-c' is for compile only without link.
* pre-processor' statement, ex. '#ifdef', '#include' has only life-scope in .c to .o
* #include "a.h" in 'a.c' can be seen as pulling the codes from 'a.h' then copy/paste into 'a.c' before compliation.

> Consider a case: <br> 
  "a.c" have #include "a1.h" and #include "a2.h" <br>
  "b.c" have #include "a1.h" and #include "b.h"

* To aviod duplicating 'definition for one declaration' in the 'link stage', we often write only delerations in'x.h'

> if we write the definition of 'void foo(){}' in 'a1.h', then linking of 'a.o' and 'b.o' will fail. 

* declarations can be re-assign/dupilcated. 

> Consider another case: <br>
  'a.h' include 'a1.h', where 'a1.h' include 'a.h'. <br>
  __*It forms 'cyclic dependecy'!!*__ <br>
  To avoid it, we can use the 'header guard' flags as follows:

```
#ifndef __HEADER_A__
#define __HEADER_A__
...< body >    
#endif
```