from numpy import *

v = array(eval(input("Digite os valores da compra: ")))

i = 0
t = 0

while i < size(v):
	if(v[i] > 80.0):
		v[i] = v[i] - 15/100*v[i]
	t = t + v[i]
	i = i + 1
print(round(t, 2))
		