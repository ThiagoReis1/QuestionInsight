valor = float(input())
forma = input()

if forma == "D":
	resultado = valor - (valor * 0.13)
elif forma == "P":
	resultado = valor - (valor * 0.13)
elif forma == "C":
	parcela = int(input())
	if parcela == 1:
		resultado = valor
	else:
		resultado = valor + (valor * 0.08)
		
resultado_arredondado = round(resultado, 2)
print(resultado_arredondado)