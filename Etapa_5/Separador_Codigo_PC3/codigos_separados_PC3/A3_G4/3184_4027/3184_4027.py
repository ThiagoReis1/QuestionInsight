from numpy import *
ent = array(eval(input("Letras em ordem descrescente: ")))
n = size(ent)
j = n - 1
for i in range(n//2):
	c = ent[n - 1 - i]
	ent[n - 1 - i] = ent[i]
	ent[i] = c
print(ent)