N = int(input("digite n: "))

cont = 1
soma = 0

base = 5 + 3 + soma
sinal = 1
resultado = 1
exp = 2

while(N != 0):
	resultado =   cont **exp / base
	resultado = resultado + 1
	sinal = sinal * -1
	soma = soma + 2
print(round(resultado,10)