from numpy import *
from math import *
v = array(eval(input("digite os valores: ")))
n = size(v)
s = 1 
for x in range(size(v)):
	s = s*((v[x])**1/n)
print(round(s,2))