from numpy import *
t = array(eval(input("Tempos dos corredores: ")))
m = max(t)
i = 0

while(i < size(t) and (t[i] != m)):
	i = i + 1
print(i)