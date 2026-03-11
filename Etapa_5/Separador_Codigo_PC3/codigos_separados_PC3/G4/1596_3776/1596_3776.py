from numpy import *
from numpy.linalg import *
v=array(eval(input()))
x= sum(v)- min(v)
d= size(v) - 1
f=x/d
print(round(f,2))
