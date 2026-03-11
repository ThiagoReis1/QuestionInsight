from numpy import*
v = input().upper()
i = 0
valor1 = 0
valor2 = 0
while i < len(v):
	if v[i] != 'A' and  v[i] != 'E' and  v[i] != 'I' and  v[i] != 'O' and v[i] != 'U':
		valor1 = valor1 + 0.17
	else:
		valor2 = valor2 + 0.15
	i = i + 1
valor = valor1+valor2
print(round(valor,2))