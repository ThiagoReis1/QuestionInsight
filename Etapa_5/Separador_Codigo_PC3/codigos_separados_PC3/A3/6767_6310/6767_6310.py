valor = float(input())
tipo = input()
tipo = tipo.upper()
total = 0.0
if(tipo == 'D' or tipo == 'P'):
	total = valor - (valor*12/100)
elif(tipo == 'C2'):
	total = valor + (valor*7/100)
else:
	total = valor
print(round(total,2))