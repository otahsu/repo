#! /usr/bin/env python2.7

#############################
# Class
#############################
class Aha(object): 
    def __init__(self, int):
        super(Aha, self).__init__()
        self.int = int
        print self.int, id(int)==id(self.int)

#############################
# Global Functions
#############################
def pass_int(int):
    print int, id(int)

def pass_list(list):
    for i in list:
        print i,
    print id(list)

def pass_cls_obj(obj):
    obj.int = 2

############################
# Test Functions
############################
def call_pass_int():
    a = 1
    b = a 
    print a, id(a)
    print id(a) == id(b)
    b = 2
    print a, b
    print id(a) == id(b)
    pass_int(a)

def call_pass_list():
    ls_a = [0]
    ls_b = ls_a
    print id(ls_a) == id(ls_b)
    ls_b[0] = 1
    print id(ls_a) == id(ls_b)
    pass_list(ls_a)

def call_pass_class_obj():
    obj1 = Aha(1)
    obj2 = obj1
    
    obj2.int = 2

    print obj1.int, obj2.int
    
    int = 1
    obj = Aha(int)
    print id(int) == id(obj.int)



if __name__ == '__main__':
    #call_pass_int()
    #call_pass_list()
    call_pass_class_obj()

# vim: set ft=python ff=unix ai et nu sw=4 ts=4 tw=95