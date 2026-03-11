from numpy import *
n = array(eval(input("n: ")))
s = 0
for i in n:
	s += exp(i)
print(round(log(s/exp(size(n))), 2))