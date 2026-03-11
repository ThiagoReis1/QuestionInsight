from numpy import*

vet = input("Informe uma string qualquer: \n")
cont = 0

for i in range(len(vet)):
	if (vet[i]=='a') or (vet[i]=='e') or (vet[i]=='i') or (vet[i]=='o') or (vet[i]=='u'):
		cont = cont + 1
resto = len(vet) - cont
print(cont)
print(resto)
