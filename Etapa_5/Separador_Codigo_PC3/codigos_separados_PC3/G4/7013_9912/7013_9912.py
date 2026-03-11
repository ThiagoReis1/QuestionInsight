X=int(input("Numeros pertencentes: "))
Y=int(input("Numeros pertencentes: "))
cont=0
soma=0

while (X%2):
	if (X<=2) and (Y>=2):
		cont=cont+1
		soma=soma+1
		
	X=int(input("Numeros pertencentes: "))
	Y=int(input("Numeros pertencentes: "))
	
print(soma)