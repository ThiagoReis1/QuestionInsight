from numpy import *

v = array(eval(input("Digite a quantidade de demandas: ")))

n = size(v)

cont = 0

for i in range(n):
	crit = v[0]
	if v[i] > crit :
		print(i)
		cont = cont + 1 
print(cont)