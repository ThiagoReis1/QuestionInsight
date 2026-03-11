salario = float(input("salario atual: "))
codigo = int(input("codigo: "))
print("Entradas: R$",salario,"e codigo",codigo)
if salario >= 0 and codigo == 101:
	valor = salario * 0.008
	reajuste = salario + valor
	print("Novo salario: R$", round(reajuste,2))
elif salario >= 0 and codigo == 102:
   valor = salario * 0.0065
   reajuste = salario + valor
   print("Novo salario: R$", round(reajuste,2))
elif salario >= 0 and codigo == 103:
	valor = salario * 0.006
	reajuste = salario + valor
	print("Novo salario: R$", round(reajuste,2))
elif salario >= 0 and codigo == 104:
	valor = salario * 0.0055
	reajuste = salario + valor
	print("Novo salario: R$", round(reajuste,2))
else:
   print("Dados invalidos")