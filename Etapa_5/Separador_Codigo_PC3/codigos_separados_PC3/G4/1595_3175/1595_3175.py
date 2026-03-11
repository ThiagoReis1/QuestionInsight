from numpy import *

n = array(eval(input("Informe as notas: ")))

g = []

a = min(n)

i = 0

while i < size(n):
	if(n[i] != a):
		g.append(n[i])
		
	i = i + 1
	
print(round(sum(g)/size(g), 2))