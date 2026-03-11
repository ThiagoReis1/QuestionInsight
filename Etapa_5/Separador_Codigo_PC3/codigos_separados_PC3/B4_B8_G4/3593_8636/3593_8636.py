from numpy import*

vet = array(eval(input("numero de vetores: ")))
cont = 200
i = 0
while i < size(vet):
	if vet[i] == 1:
		cont = cont / 2
	elif vet[i] == 2:
		cont = cont * 3
	elif vet[i] == 3:
		cont = cont / 2
	elif vet[i] == 4:
		cont = cont * 3
	elif vet[i] == 5:
		cont = cont / 2
	elif vet[i] == 6:
		cont = cont * 3
	i = i + 1
print(cont)	
