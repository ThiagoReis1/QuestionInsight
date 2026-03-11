idade = int(input("Idade: "))

menoridade = 0
fim = -1

while idade != fim: 
	if idade < 18:
		menoridade = menoridade + 1
		idade = int(input("Idade: "))
	else:
		idade = int(input("Idade: "))
print(menoridade)