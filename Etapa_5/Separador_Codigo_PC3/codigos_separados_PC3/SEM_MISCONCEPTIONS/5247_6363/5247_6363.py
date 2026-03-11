salario = float(input("salario: "))
cargo = int(input("codigo do cargo: "))

if(cargo == 101):
	x = salario+((salario*0.80)/100)
	print("Novo salario: R$" , (round(x, 2)))
elif(cargo==102):
	x = salario+((salario*0.65)/100)
	print("Novo salario: R$" , (round(x, 2)))
elif(cargo==103):
	x = salario+((salario*0.60)/100)
	print("Novo salario: R$" , (round(x, 2)))
elif(cargo==104):
	x = salario+((salario*0.55)/100)
	print("Novo salario: R$" , (round(x, 2)))
else:
	print("Dados invalidos")
	
	