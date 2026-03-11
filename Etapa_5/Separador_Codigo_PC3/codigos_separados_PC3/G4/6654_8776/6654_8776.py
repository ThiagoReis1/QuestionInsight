from numpy import *
n = array(eval(input()))
v0 = array([1,3,2,5])
v1 = n*v0
v = sum(v1)/sum(v0)
print(round(v,2))