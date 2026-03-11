c = float(input("Valor do carro: "))
d = float(input("Valor inicial: "))
m = float(input("Deposito mensal: "))
j = float(input("Taxa de juros: "))
soma = d
t = 0
if (c <= 0 or d <= 0 or m <= 0 or j <= 0):
	print("Dados incorretos")
	while (soma == c):
		t = t + 1
		soma = d + m * j
		
print(t)
		

		
