#! /usr/bin/env python2.7
import os, sys

def list_atof(str_list):
    try:
        num_list = [ float(s) for s in str_list ]
    except Exception as e:
        print e
    return num_list

def check_is_triangle(triangle_ls):
    #triangle_ls = sorted(triangle_ls)
    #print triangle_ls 
    return triangle_ls[0] + triangle_ls[1] > triangle_ls[2]

def check_is_iso(triangle_ls):
    if not check_is_triangle(triangle_ls):
        return False
    else:
        cond1 = triangle_ls[0] == triangle_ls[1]
        cond2 = triangle_ls[1] == triangle_ls[2]
        return cond1 or cond2

def check_is_equal(tri_ls):
    if not check_is_iso(tri_ls):
        return False
    else:
        return tri_ls[0]==tri_ls[1]==tri_ls[2]

if __name__ == '__main__':
    input_str = raw_input('Please key-in 3-number-tuple (a,b,c) as the lengths of a triangle : ')
    #print type(input_str), input_str
    str_ls = input_str.split(',')
    #print str_ls
    triangle_ls = list_atof(str_ls)
    triangle_ls = sorted(triangle_ls)
    #print 1+2 >= 3
    isTriangle = check_is_triangle(triangle_ls)
    #print isTriangle
    isIso = check_is_iso(triangle_ls)
    isEqual = check_is_equal(triangle_ls)
    print "(isTriangle, isIso, isEqual) = %g, %g, %g" %(isTriangle, isIso, isEqual)

#vim set: syntax=python tabstop=4 softtabstop=4 ai expandtab nu:


