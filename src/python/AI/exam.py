#!/usr/bin/env python
import sys, os

def test_3duplicated_sorted_list(list): 
    '''
    3-2:
    
    '''
    j=0
    num=0
    for i in xrange(1, len(list)):
        if list[i] == list[j]: 
            num += 1
            if num <= 3:
                j += 1
        else:
            list[j] = list[i]  # (i=5, j=3, [1,1,1,2,1,2,2,2,3,3])
            num = 0
    return len(list), list

def test_iteration_n_sum(n):
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

def test_fib(n):
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

def removeDuplicates3(nums):
    '''
    Allow duplicated thrice elememts.
    '''
    i = 0
    ite = 0
    for n in nums:
        if i < 3 or n > nums[i-3]:
            nums[i] = n
            i += 1
        ite += 1
        print "iteration=%d, i=%d, nums=%s" %(ite, i, nums)
    return i

if __name__ == "__main__":

    print "AI entrance exam!"
    print "===================================="
    ls=[1,1,1,1,1,2,2,2,3,3]
    #print test_3duplicated_sorted_list(ls)
    #print test_iteration_n_sum(0)
    #print test_iteration_n_sum(1)
    #print test_iteration_n_sum(3)
    #print test_fib(2), test_fib(3), test_fib(4),test_fib(5)
    #removeDuplicates(ls)
    removeDuplicates3(ls)

# vim: set ft=python ff=unix fenc=utf8 ai et sw=4 ts=4 tw=79:
    
