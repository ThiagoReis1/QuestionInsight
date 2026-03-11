from numpy import*
E= array(eval(input("Entrada da melhoria das UBS: ")))
cont= 0
for i in range(1,size(E)):
	if E[i] >= E[0]:
		print(i)
		cont= cont + 1
print(cont)