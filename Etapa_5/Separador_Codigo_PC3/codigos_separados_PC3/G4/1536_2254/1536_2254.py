nx = float(input(":"))
ni = int(input(":"))
b = 2
soma = 1
sinal = - 1
cont = 1
while(cont<ni):
	soma = soma + sinal * ((nx**b)/b)
	b = b + 1
	sinal = sinal * -1
	cont = cont + 1
print(round(soma,10))