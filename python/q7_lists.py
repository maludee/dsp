# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

"""
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
"""


def match_ends(words):
    count = 0
    for word in words:
        if len(word) > 1:
            if word[0] == word[len(word) - 1]:
                count = count + 1
            else:
                count = count
        else: count = count
    return count

print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print match_ends(['aaa', 'be', 'abc', 'hello'])


"""
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
"""


def front_x(words):
    
    sortlist = sorted(words)
    newlist = []
    n = 0

    for s in sortlist:
        if s[0] == 'x':
            newlist.insert(n, s)
            n = n + 1
        else:
            newlist.append(s)
    
    return newlist

print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    

"""
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
"""


def sort_last(tuples):
    tuples = sorted(tuples, key=lambda x: x[1:])
    return tuples

print sort_last([(1, 3), (3, 2), (2, 1)])
print sort_last([(2, 3), (1, 2), (3, 1)])
print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])


"""
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
"""
    
    
def remove_adjacent(nums):
    nums = [n for i, n in enumerate(nums) if i == 0 or n != nums[i-1]]
    return nums
            

print remove_adjacent([1, 2, 2, 3])
print remove_adjacent([2, 2, 3, 3, 3])   
print remove_adjacent([3, 2, 3, 3, 3])


"""
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
"""

    
def linear_merge(list1, list2):
    i = 0
    newlist = []
    
    while list1 and list2:
        if list1[0] < list2[0]:
            newlist.append(list1.pop(0))
        else:
            newlist.append(list2.pop(0))
    
    return newlist + list1 + list2

print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
