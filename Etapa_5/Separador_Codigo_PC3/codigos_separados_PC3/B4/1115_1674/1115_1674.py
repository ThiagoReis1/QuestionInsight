salario_atual = float(input("Qual o salario atual?"))
codigo_do_cargo = int(input("Qual o codigo do cargo?"))
if(codigo_do_cargo == 101 and salario_atual > 0):
	salario = ( salario_atual * 1.008 )
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Novo salario: R$",round(salario,2))
elif(codigo_do_cargo == 101 and salario_atual <= 0):
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Dados invalidos")
elif(codigo_do_cargo == 102 and salario_atual > 0):
	salario = ( salario_atual * 1.0065)
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Novo salario: R$",round(salario,2))
elif(codigo_do_cargo == 102 and salario_atual <= 0):
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Dados invalidos")
elif(codigo_do_cargo == 103 and salario_atual > 0):
	salario = (salario_atual * 1.006 )
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Novo salario: R$",round(salario,2))
elif(codigo_do_cargo == 103 and salario_atual <= 0):
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Dados invalidos")
elif(codigo_do_cargo == 104 and salario_atual > 0):
	salario = ( salario_atual * 1.0055)
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Novo salario: R$",round(salario,2))
elif(codigo_do_cargo == 104 and salario_atual <= 0):
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Dados invalidos")
else:
	print("Entradas: R$", salario_atual,"e codigo",codigo_do_cargo)
	print("Dados invalidos")
	

