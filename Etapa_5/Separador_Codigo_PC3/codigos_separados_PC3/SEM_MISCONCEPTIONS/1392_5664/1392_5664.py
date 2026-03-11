consumo= float(input('consumo: '))

if consumo<10:
	conta= 30 + 3*consumo
else:
	conta= 30 + 3.5*consumo


print(round(conta,2))