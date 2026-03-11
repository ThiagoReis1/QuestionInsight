n = int(input("Digite numeros inteiros: "))

#julia = total
julia = 0
par = 0

while (n != 0):
	if (n % 2 == 0):
		par = par + 1
	julia = julia + 1
	n = int(input("Digite numeros inteiros: "))
	
porcentagem = (100 * par) / julia

print(julia)
print(round(porcentagem, 2))