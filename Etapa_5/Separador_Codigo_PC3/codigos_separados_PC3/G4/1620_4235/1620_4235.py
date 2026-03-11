from numpy import *
from numpy.linalg import *
tbm= array(eval(input()))
pat = array(eval(input()))
a = (tbm*pat)
b = (a/100)
c = (b*5)
soma= sum(c)
print(round(soma,2))
		