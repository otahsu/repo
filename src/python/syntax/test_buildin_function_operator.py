#!/usr/bin/env python2.7

def test_queue():
    """
    + https://docs.python.org/2/tutorial/datastructures.html
    It doesn't suggest that implements queue by list because of performance issue, 
    but use 'deque' container to instead. 
    + https://docs.python.org/2/library/collections.html#collections
    collections is for High-performance container datatypes.
    + list-like container with fast appends and pops on either end
    """
    from collections import deque 
    
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")           # Terry arrives
    queue.append("Graham")          # Graham arrives
    print queue.popleft()           # The first to arrive now leaves
    #'Eric'
    print queue.popleft()           # The second to arrive now leaves
    #'John'
    print queue                     # Remaining queue in order of arrival
    #deque(['Michael', 'Terry', 'Graham'])
    print queue.pop()
    print queue
    queue.appendleft('a')
    print queue

def test_sort():
    """
    https://docs.python.org/2/howto/sorting.html#sortinghowto
    """
    # TODO: list.sort(key) or sorted(...)
    pass

if __name__ == '__main__':
    test_queue()

# vim: set ft=python ff=unix ai et nu sw=4 ts=4 tw=100: