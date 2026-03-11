#Entradinhas
s = float(input("Insira seu salario atual: "))
cod = int(input("Insira o codigo correspondente ao seu cargo: "))
print("Entradas: R$", s , "e codigo", cod)
#Condições
if((s>0) and (101 <= cod <= 104)):
	if(cod == 101):
		print("Novo salario: R$",round(s + s*0.0080,2))
	elif(cod == 102):
		print("Novo salario: R$",round(s + s*0.0065,2))
	elif(cod == 103):
		print("Novo salario: R$",round(s + s*0.0060,2))
	elif(cod == 104):
		print("Novo salario: R$",round(s + s*0.0055,2))
else:
	print("Dados invalidos")