from numpy import*

V = array(eval(input("Digite o registro de acidentes: ")))

cont = 0
i = 0

for i in range(1,size(V)):
	if V[i] >= V[0]:
		print(i)
		cont = cont + 1
print(cont)


