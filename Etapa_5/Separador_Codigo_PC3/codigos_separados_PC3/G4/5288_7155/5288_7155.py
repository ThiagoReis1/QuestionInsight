x = int(input("Idade: "))	
cont = 0
soma = 0

while (x != -1):
	cont = cont+1
	if (x < 18):
		soma = soma + 1
	x = int(input("Idade: "))
	
j = (soma*100)/cont

print(cont)
print(round(j,2))