#!/usr/bin/env python2.7
import os, sys

def test_set():
    s1 = set(['1', '2', '3', '5']) # set([iterable object]), '[]' means optional.
    s2 = set(('1', '2', '3', '5'))
    print s1 is s2, s1 == s2
    s3 = set(['4', '5', '6'])
    print 's1 =', s1 
    print 's3 =', s3 
    print 's1 OR s3 =', s1 | s3
    print "s1 XOR s3 =", s1 ^ s3
    print "s1 minus s3 =", s1 - s3
    print "s1 intersect s3 =", s1 & s3
    s3.add('7')
    print s3
    s3.remove('7')
    print s3 == {'4', '5', '6'}

def test_list():
    ls = [0, 1, 2, 3, 4, 5]
    # TODO-memo: slice [start:end] doesn't include the end-idx.
    print ls[1:2]
    # TODO-memo: It should set (end > start), else return [].
    print ls[-1:-2]
    # TODO-memo: The len(list) == (end - start)
    start = 0 ; end = len(ls)
    assert( len(ls) == end - start)
    # TODO-memo: The tail-idx is '-1'.
    print "ls[-1:len(ls)] =", ls[-1:len(ls)]
    # TODO-memo: [start:end:step] is good for stepping the elements.\\
    #default-value of 'start' is 0, 'end' is len(list), 'step' is 1.\\
    #And 
    print "ls[::] =", ls[::]
    print "ls[::2] =", ls[::2]
    # reverse elements in list.
    print "ls[::-1]", ls[::-1]

    # TODO-memo: reverse in-place.
    ls.reverse()
    print "Now here is the reversed from original ls =", ls
    #[5, 4, 3, 2, 1, 0]
    
    # append(x), insert(i, x), remove(x), pop(i)
    ls2 = ['a', 'd', 'c']
    print "ls2 =", ls2
    ls2.append('b')
    print "ls2 =",ls2
    ls2.remove('d')
    print "ls2 =", ls2
    ls2.pop(1) # defaulty pop the last one.
    print "ls2 =", ls2
    ls2.insert(1, 'aa')
    print "ls2 =", ls2
    ls2.insert(len(ls2), 'bb')
    print "ls2 =", ls2
    #['a', 'aa', 'b', 'bb']
    ls2.reverse()
    print "ls2 =", ls2
    #['bb', 'b', 'aa', 'a']

    # extend(L) append another list-object in-place.
    id_ori = id(ls2)
    ls2.extend(ls)
    print "ls2 =", ls2
    id_after = id(ls2)
    assert ( id_ori == id_after != id(ls)) # prove that it's in-place.

    # del a slice of a list.
    del ls2[1:3]
    assert (ls2[2:1] == []) # wrong slice-idx return [] empty-list.
    id_after = id(ls2)
    assert ( id_ori == id_after != id(ls)) # prove that it's in-place.
    print ls2
    #['bb', 'a', 5, 4, 3, 2, 1, 0]
    
    #testcase_list()

def test_slice():
    """
     + idx chart - https://docs.python.org/2/tutorial/introduction.html#strings
     +---+---+---+---+---+---+
     | P | y | t | h | o | n |
     +---+---+---+---+---+---+
     0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1
    
    """
    #TODO-Q: For a slice[start:end:step], what's about [-1:3] idx.\\
    #What is the exact definition/convention/explaination.
    #TODO-Ans: Maybe it can be explaned by the default value of (start, end, step),
    #where the slice-loop-condition may be (start += step < end)?
    str = 'abcd'
    print 'str =', str
    print "str[2:1:-1] =", str[2:1:-1]
    print "str[-1:-2:-1] =", str[-1:-2:-1]
    print "str[:-2:-1] =", str[:-2:-1] # TODO-Q: start from len(str)-1?
    assert str[-1:3] == ''
    print str[-3:]

def testcase_list():
    #TODO: rewrite this as a test-case!
    """
    Sample-code from \"https://docs.python.org/2/tutorial/datastructures.html\"
    """
    a = [66.25, 333, 333, 1, 1234.5]
    print a.count(333), a.count(66.25), a.count('x')
    #2 1 0
    a.insert(2, -1)
    a.append(333)
    print a
    #[66.25, 333, -1, 333, 1, 1234.5, 333]
    a.index(333)
    #1
    a.remove(333)
    print a
    #[66.25, -1, 333, 1, 1234.5, 333]
    a.reverse()
    print a
    #[333, 1234.5, 1, 333, -1, 66.25]
    a.sort()
    print a
    #[-1, 1, 66.25, 333, 333, 1234.5]
    print a.pop()
    #1234.5
    print a
    #[-1, 1, 66.25, 333, 333]
    
    # Using lists as stacks.
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print stack
    #[3, 4, 5, 6, 7]
    print stack.pop()
    #7
    print stack
    #[3, 4, 5, 6]
    print stack.pop()
    #6
    print stack.pop()
    #5
    print stack
    #[3, 4]

def test_list_comprehension():
    """
    https://docs.python.org/2/tutorial/datastructures.html?highlight=list%20comprehensions
    """
    squares = [x**2 for x in xrange(10)]
    print squares
    
    # conditionaly and multi-loop generate a flat list.
    pnt_ls = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print pnt_ls
    
    pnt_ls2 = []
    for x in [1,2,3]:
        for y in [3,1,4]:
            if x !=y:
                pnt_ls2.append( (x,y))
    assert pnt_ls == pnt_ls2
    
    # nested-list
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]] # list of row-lists.
    print matrix
    trans = [[row[i] for row in matrix] for i in range(4)] # inner expand listcomp firstly.
    print trans
    '''
    As we saw in the previous section, the nested listcomp is evaluated in the context of the for that follows it, so this example is equivalent to:
    '''
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    print transposed
    assert transposed == trans # TODO-memo: "==" is value-eaqual can dive into deep-levels(not shollow).
    # use unzip function for nested is prefered.
    print zip(*matrix)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--switch_key', dest='switch_key', action='store',
                default='set', type=str,
                help='Choose to test either \'set\',\'list\',\'compre\', \'slice\' module; default is %(default)s.')
    cmd_args = parser.parse_args()
    #print cmd_args, type(cmd_args), cmd_args.__dict__ # Namespace(switch_key='set') <class 'argparse.Namespace'> {'switch_key': 'set'}
    
    # To inimate "switch structure" from http://openhome.cc/Gossip/Python/LambdaExpression.html
 
    flow_ctl_dict = { 'set': lambda : test_set(),
                      'list': lambda : test_list(),
                      'compre': lambda : test_list_comprehension(),
                      'slice': lambda : test_slice(),
                    }
    flow_ctl_dict.get(cmd_args.switch_key, None)()

# vim: set ft=python ff=unix ai et nu sw=4 ts=4 tw=100: