# Data: 14/05

# Le um numero real e no. de termos 
num = float(input('Numero: '))
qt = int(input('No. de termos: '))

i = 0     # contador
soma = 0  # acumulador
fim = qt - 1 # fim da contagem

while i <= fim:
	soma = soma + ((-1) ** i) * (num) ** (i)
	i = i + 1

print(round(soma , 7))