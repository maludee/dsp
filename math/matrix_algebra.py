# Matrix Algebra

import numpy as np

# Create matrix variables
A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')

# Create vector variables
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

## Question 1

print A.shape
print B.shape
print C.shape
print D.shape
print u.shape
print w.shape
print ""

## Question 2

print u + v
print u - v
print 6 * u
print u * v
print np.linalg.norm(u)
print ""

## Question 3

#print A + C - answer not defined b/c dimensions
print A - C.T
print C.T - (3*D)
print np.dot(B, A)
#print np.dot(B, A.T) - answer not defined b/c dimensions
#print np.dot(B, C) - answer not defined b/c dimensions
print np.dot(C, B)
print B**4
print np.dot(A, A.T)
print np.dot(D.T, D)

