from numpy import*
from numpy.linalg import*

t = array(eval(input()))
c = array(eval(input()))

C = (c / 100) * 5
C = C.T

A = dot(C, t)

print(A)
