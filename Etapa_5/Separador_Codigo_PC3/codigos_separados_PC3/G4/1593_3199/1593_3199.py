from numpy import *
n = array(eval(input("notas: "))) #notas 
i = 0 #indice
p = 1 #peso
s = 0 #soma dos pesos
while (i < size(n)):
	n[i] = n[i]*p
	p = p + 1
	s = s + p
	i = i + 1

print(p)
print(s)
q = n
m = sum(q)/s
print(round(m,2))