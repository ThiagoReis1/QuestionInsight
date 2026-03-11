from numpy import *

n = array(eval(input("N: ")))
p = ([5,1])
i = 0
s = 0

while i<size(n):
	j = n[i]*p[i]
	s = s + j
	i = i + 1
	
print(round(s/sum(p),2))