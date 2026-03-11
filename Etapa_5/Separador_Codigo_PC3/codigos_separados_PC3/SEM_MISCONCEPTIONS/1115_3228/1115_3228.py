salario = float(input("Digite o salario: "))
codigo = int(input("Digite o codigo: "))


print("Entradas: R$", salario,"e codigo", codigo)


if ((salario > 0) and (codigo == 101)):
	print("Novo salario: R$", round(salario * 0.0080 + salario, 2))
elif ((salario > 0) and (codigo == 102)):
	print("Novo salario: R$", round(salario * 0.0065 + salario, 2))
elif ((salario > 0) and (codigo == 103)):
	print("Novo salario: R$", round(salario * 0.0060 + salario, 2))
elif ((salario > 0) and (codigo == 104)):
	print("Novo salario: R$", round(salario * 0.0055 + salario, 2))
else:
	print("Dados invalidos")