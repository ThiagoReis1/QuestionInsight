valor = float(input())
cod = input()


if cod.upper() == 'D':
	total = valor - (valor * 0.17)
elif cod.upper() == 'P':
	total = valor - (valor * 0.17)
elif cod.upper() == 'C2':
	total = valor + (valor * 0.08)
else:
	total = valor

print(round(total,2))