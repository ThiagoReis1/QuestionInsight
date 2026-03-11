X = float(input("Valor do salario atual:"))
Y = int(input("Codigo do cargo:"))

if Y == 101 :
	Z = X + (X*0.0080)
	print("Entradas: R$",X,"e codigo",Y)
	print("Novo salario: R$",round(Z,2))
elif Y == 102 :
	Z = X + (X*0.0065)
	print("Entradas: R$",X,"e codigo",Y)
	print("Novo salario: R$",round(Z,2))
elif Y == 103 :
	Z = X + (X*0.0060)
	print("Entradas: R$",X,"e codigo",Y)
	print("Novo salario: R$",round(Z,2))
elif Y == 104 :
	Z = X + (X*0.0055)
	print("Entradas: R$",X,"e codigo",Y)
	print("Novo salario: R$",round(Z,2))
else:
	print("Entradas: R$",X,"e codigo",Y)
	print("Dados invalidos")