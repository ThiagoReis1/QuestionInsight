x = float(input("insira o numero: "))
y = int(input("quantida de termos: "))

soma = 0
cont = 0

while cont < y:
	soma = soma + x/((2*cont) + 1)
	cont = cont + 1
	
print(round(soma,8))
	