from numpy import *
v = array (eval(input ("Digite o tempo: ")))
y = min (v)
i = 0
while (i < size (v) and v[i] != y) :
	i = i + 1
print (i)