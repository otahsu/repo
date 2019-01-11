#!/usr/bin/env python
import sys, os

def Function_1(a,b):
    '''
    1-1
    '''
    if (b==0):
        return 1
    if (b==1):
        return a
    else:
        return a*Function_1(a,b-1)

def Function_2(list):
    '''
    1-2
    '''
    for i in xrange(len(list)):
        for j in xrange(i):
            if (list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def reverse_list(list):
    '''
    2-1
    '''
    temp = 0
    for i in xrange(len(list)/2):
        temp = list[i]
        list[i] = list[len(list) -i -1]  
        list[len(list) -i -1] = temp
    return list
        
def switch_list(list):
    '''
    2-2
    '''
    temp = 0
    for i in xrange(len(list)/2):
        temp = list[2*i]  # 2*i = 0,2~10
        list[2*i] = list[2*i + 1]
        list[2*i + 1] = temp
    
    return list

def remove_duplicated_sorted_list(list):
    '''
    3-1
    '''
    j=0
    for i in xrange(1, len(list)):
        if (list[j] < list[i]): # i = 5, 8
            j += 1    # j = 1, 2
            list[j] = list[i] 
    
    return j+1, list

def sum_n(n):
    '''
    4-1
    '''
    sum = 0
    if n <=0 :
        return sum
    else:
        for i in xrange(1,n+1):
            sum += i
        return sum

def sum_fib(n):
    '''
    4-2
    https://openhome.cc/Gossip/AlgorithmGossip/FibonacciNumber.htm
    '''
    if (n==0 or n==1):
        return n
    else:
        t0=0 ; t1=1;
        for i in xrange(2,n+1):
            temp = t1
            t1 += t0
            t0 = temp
        return t1

def removeDuplicates(nums):
    '''
    Allow duplicated twice elememts.
    From LeetCode : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C%2B%2B-Java-Python-Ruby
    '''
    i = 0
    ite = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
        ite += 1
        print "iteration=%d, i=%d, nums=%s" %(ite, i, nums)
    return i

def remove_fourice_sorted_list(list):
    '''
    3-2

    Allow repeated thrice elememts.
    '''
    j = 0
    num = 0
    ite = 0
    for i in xrange(1,len(list)):
        if i < 3:
            j +=1
        elif list[i] > list[j-3]:
            j += 1
            list[j] = list[i]
        ite += 1
        #print "iteration=%d, i=%d, nums=%s" %(ite, i, nums)
    return list

def test_3duplicated_sorted_list(list): 
    '''
    3-2: [1,1,1,1,2,2,2,3,3,4]
    
    '''
    j=0
    num=0
    for i in xrange(1, len(list)):
        if (num <2): 
            if (list[j] == list[i]):
                num += 1
                j += 1
            else:
                j += 1
        else:
            list[j] = list[i]  
            num = 0
    return j, list
if __name__ == "__main__":

    print "AI entrance exam!"
    print "===================================="
    print "1-1: Function_1(3,3) = %r" %(Function_1(3,3))
    Input = [4,5,3,7,6,1,2]
    print "1-2: Function_2(list) = %r" %Function_2(Input)
    print "2-1: reverse_list(['A','I','A','o','T','e','m','o','c','l','e','W']) = %r" %reverse_list(['A','I','A','o','T','e','m','o','c','l','e','W']) 
    
    print "2-2: switch_list(['e','W','c','l','m','o','T','e','A','o','A','I'])= %r" %switch_list(['e','W','c','l','m','o','T','e','A','o','A','I']) 
    
    A = [1,1,2,2,2,3,4]
    #A = [1,2,3,4]
    print "3-1: remove_duplicated_sorted_list(A)=%r,%r" %remove_duplicated_sorted_list(A)
    
    ls=[1,1,2,3,4,5,5,5,5,5,5,5]
    ls=[1,1,1,1,2,2,2,3,3,4]
    #ls=[1,2,3,4,4,4,4]
    #ls=[1,1,1,2,2,3,4]
    #ls=[1,2,3,4]
    print remove_fourice_sorted_list(ls)
    #print sum_n(0)
    #print sum_n(1)
    #print sum_n(3)
    print sum_fib(2), sum_fib(3), sum_fib(4),sum_fib(5)
    #removeDuplicates(ls)
    #removeDuplicates3(ls)

# vim: set ft=python ff=unix fenc=utf8 ai et sw=4 ts=4:
    
