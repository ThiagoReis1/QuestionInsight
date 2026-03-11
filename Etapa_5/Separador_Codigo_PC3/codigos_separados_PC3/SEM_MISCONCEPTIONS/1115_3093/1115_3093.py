salario = float(input())
codigo = int(input())

if (codigo == 101) and (salario > 0):
	reajuste1 = salario * 1.008
	reajuste2 = round(reajuste1, 2)
	print("Entradas: R$", salario, "e codigo", codigo)
	print("Novo salario: R$", reajuste2)
elif (codigo == 102) and (salario > 0)	:
	reajuste1 = salario * 1.0065
	reajuste2 = round(reajuste1, 2)
	print("Entradas: R$", salario, "e codigo", codigo)
	print("Novo salario: R$", reajuste2)
elif (codigo == 103) and (salario > 0):
	reajuste1 = salario * 1.006
	reajuste2 = round(reajuste1, 2)
	print("Entradas: R$", salario, "e codigo", codigo)
	print("Novo salario: R$",reajuste2)
elif (codigo == 104) and (salario > 0):
	reajuste1 = salario * 1.0055
	reajuste2 = round(reajuste1, 2)
	print("Entradas: R$", salario, "e codigo", codigo)
	print("Novo salario: R$", reajuste2)
else:
	print("Entradas: R$", salario, "e codigo", codigo)
	print("Dados invalidos")