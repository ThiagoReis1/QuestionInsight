x = float(input("Digite o salario: "))
y = int(input("Digite o codigo: "))
print("Entradas: R$",x,"e codigo",y)
if(x <= 0):
	print("Dados invalidos")
else:
	if(y == 101):
		print("Novo salario: R$",round(x + x*0.008,2))
	elif(y == 102):
		print("Novo salario: R$",round(x + x*0.0065,2))
	elif(y == 103):
		print("Novo salario: R$",round(x + x*0.006,2))
	elif(y == 104):
		print("Novo salario: R$",round(x + x*0.0055,2))
	else:
		print("Dados invalidos")