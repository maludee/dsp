# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

"""
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
   
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
"""
 

def donuts(count):
    if count > 9:
        return "Number of donuts: many"
    else:
        return "Number of donuts: " + str(count)
    
print donuts(4)
print donuts(9)
print donuts(10)
print donuts(99)


"""
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz' 
"""
 

def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]

print both_ends('spring')
print both_ends('Hello')
print both_ends('a')
print both_ends('xyz')


"""
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
"""
   

import string

def fix_start(s):
    new_s = string.replace(s[1:],s[0],'*')
    return s[0] + new_s
                   
print fix_start('babble')
print fix_start('aardvark')
print fix_start('google')
print fix_start('donut')
   

"""
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
"""

    
def mix_up(a, b):
    return b[:2] + a[2:] + " " + a[:2] + b[2:]

print mix_up('mix', 'pod')
print mix_up('dog', 'dinner')
print mix_up('gnash', 'sport')
print mix_up('pezzy', 'firm')


"""
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
"""


def verbing(s):
    if len(s) > 2:
        if s.endswith('ing'):
            return s + 'ly'
        else:
            return s + 'ing'
    else:
        return s
        
print verbing('hail')
print verbing('swiming')
print verbing('do')


"""
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
"""


import string

def not_bad(s):
    if 'not' in s:
        if 'bad' in s:
            a = s.find('not')
            b = s.find('bad') + 3
            if b < a:
                return s
            else:
                n = string.replace(s, s[a:b], 'good')
            return n
        else:
            return s
    else:
        return s

print not_bad('This movie is not so bad')
print not_bad('This dinner is not that bad!')
print not_bad('This tea is not hot')
print not_bad("It's bad yet not")


"""
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
"""


def front_back(a, b):
   
    if len(a) % 2 == 0:
        indexa = len(a) / 2
    else:
        indexa = len(a) / 2 + 1

    if len(b) % 2 == 0:
        indexb = len(b) / 2
    else:
        indexb = len(b) /2 + 1
    
    return a[:indexa] + b[:indexb] + a[indexa:] + b[indexb:]
        
    
print front_back('abcd', 'xy')
print front_back('abcde', 'xyz')
print front_back('Kitten', 'Donut')
