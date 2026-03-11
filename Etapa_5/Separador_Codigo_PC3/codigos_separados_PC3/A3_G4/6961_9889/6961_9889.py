x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))

divisores = 1 # quantidade de numeros divisiveis por 3
soma = 0 # soma dos divisores (variavel acumuladora)

while (x<=y):
	if(x%3 == 0): #divisiveis por 3	
		soma = soma + x
	x = x + 3
	
print(soma)	