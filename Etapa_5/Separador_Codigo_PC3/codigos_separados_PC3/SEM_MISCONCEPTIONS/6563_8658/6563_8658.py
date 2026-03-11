# faça seu código aqui!
dia = int(input("dias reservados: "))

if dia < 15:
	valor = (dia*175) + 20
elif dia == 15:
	valor = (dia*175) + 16
else:
	valor = (dia*175) + 10
print("total= ", round(valor,2))