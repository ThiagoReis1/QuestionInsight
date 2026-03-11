from numpy import*
ataque = array(eval(input("vetor de danos: ")))
i = 0
cont = 0
while (i < size(ataque)):
	cont = cont + 1
	i = i + 1 
	peso = ataque[cont] * i
	
print(peso)
	

