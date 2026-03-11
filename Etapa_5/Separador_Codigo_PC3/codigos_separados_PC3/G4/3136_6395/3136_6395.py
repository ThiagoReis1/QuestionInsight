from numpy import *

v = array(eval(input("Digite:")))
i = 0
n = 0
for i in range(size(v)):
	n = n + log(v[i]+ 1)
m = exp(n/size(v))-1

print(round(m, 2))
