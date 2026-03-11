x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y:"))

cont = x 
soma = 0 

while (cont < y):
	if (cont % 3 == 0):
		soma = soma + cont
	cont += 1
		
		
		
print(soma)