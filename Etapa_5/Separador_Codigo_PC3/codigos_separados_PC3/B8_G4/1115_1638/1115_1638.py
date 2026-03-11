x = float(input("Digite o salario atual: "))
y = int(input("Digite o codigo do cargo: "))


if(x>0):
	if("Administrador" == 101):
		reajuste = x * 0,80
		z = x + reajuste
	elif("Engenheiro" == 102):
		reajuste = x * 0,65
		z = x + reajuste
	elif("Medico" == "103"):
		reajuste = x * 0,60
		z = x + reajuste
	elif("Outros_Cargos" == 104):
		reajuste = x * 0,55
		z = x + reajuste
else:
	print("Entradas: R$",x, "e codigo", y)
	print("Dados invalidos")
		 
print("Entradas: R$",x, "e codigo", y)
print("Novo salario: R$", z)
	
			