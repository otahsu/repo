#!/usr/bin/env python2.7
# Python scope rules -LEGB
"""
+ L, Local (Names assigned in any way within a function (def or lambda)), and not declared global in that function.

+ E, Enclosing function locals. Name in the local scope of any and all enclosing functions (def or lambda), form inner to outer.

+ G, Global(module). Names assigned at the top-level of a module file, or declared global in a def within the file.

+ B, Built-in (Python). Names preassigned in the built-in names module :
"""
#TODO: It may be simplified to - Python would find a variable from
# "inner-block to outter-block" and the outtest are Module, and Build-in
# namesapce.  

#TODO: Fuctions as closures. P.98~100 in 'Python Essential Reference'.
#TODO-Q: Fiction closure : Functions which are defined along whith the enviroment they excute. 
def test_closure():
    def callf(func): # function is an object in Python.
        return func() # call it.
   
    x = 10
    def bar():
        x = 13
        def helloworld():
            print "This function namespace is stored in helloworld.__globals__ =",\
            helloworld.__globals__ 
            print dir()
            print helloworld.__dict__
            return "Hello World. x is %d" %x
        ret = callf(helloworld)
        print ret
    
    bar()

if __name__ == '__main__':
    test_closure()

# vim: set ft=python ff=unix ai et nu sw=4 ts=4 tw=100: