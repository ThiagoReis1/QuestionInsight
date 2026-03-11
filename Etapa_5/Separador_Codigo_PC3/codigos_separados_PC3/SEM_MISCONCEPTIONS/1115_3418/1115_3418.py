from math import*

#ENTRADA

salario_atual = float(input("Salario Atual: "))
cargo = int(input("Codigo do cargo: "))

#CONDICIONAL

if(cargo == 101):
	reajuste = (salario_atual * 0.008)
	novo_salario = (round(salario_atual + reajuste, 2))
	print("Entradas:", "R$", salario_atual, "e codigo", cargo)
	print("Novo salario: R$", novo_salario)
elif(cargo == 102):
	reajuste = (salario_atual * 0.0065)
	novo_salario = (round(salario_atual + reajuste, 2))
	print("Entradas:", "R$", salario_atual, "e codigo", cargo)
	print("Novo salario: R$", novo_salario)
elif(cargo == 103):
	reajuste = (salario_atual * 0.0060)
	novo_salario = (round(salario_atual + reajuste, 2))
	print("Entradas:", "R$", salario_atual, "e codigo", cargo)
	print("Novo salario: R$", novo_salario)
elif(cargo == 104):
	reajuste = (salario_atual * 0.0055)
	novo_salario = (round(salario_atual + reajuste, 2))
	print("Entradas:", "R$", salario_atual, "e codigo", cargo)
	print("Novo salario: R$", novo_Salario)
else:
	print("Entradas:", "R$", salario_atual, "e codigo", cargo)
	print("Dados invalidos")