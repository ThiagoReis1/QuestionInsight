from numpy import *

n = array(eval(input()))

p= [2,2,6,1]

np = sum(n*p)/sum(p)
print(round(np, 2))