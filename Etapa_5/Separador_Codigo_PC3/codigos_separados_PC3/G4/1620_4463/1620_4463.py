from numpy import *

t = array(eval(input("Tempo de banho: ")))
p = array(eval(input("Percentual da torneira: ")))

cont = 0

for i in range(size(p)):
	if (t[i] > 0):
		cont = cont + (p[i]/100 * 5 * t[i])
	
print(cont)
