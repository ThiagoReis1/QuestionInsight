from numpy import *

v = array(eval(input("digite os valores: ")))

m = 1

for i in range(size(v)):
	m = m*(v[i])
x = m**(1/size(v))

print(round(x, 2))