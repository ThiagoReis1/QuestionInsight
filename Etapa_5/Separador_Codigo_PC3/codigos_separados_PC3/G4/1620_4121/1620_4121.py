from numpy import *
from numpy.linalg import *
tem = array(eval(input()))
aber = array(eval(input()))

aber = (aber/100)*5
aber=aber.T

z=dot(aber,tem)
print(z)
