X = float(input("qual o salario: "))
Y = int(input("qual o codigo: "))
print("Entradas: RS", X , "e", "codigo", Y )
if (Y == 101):
	novo_salario = X + (X * 0.8)
	print(round(novo_salario,2))
elif (Y == 102):
	novo_salario = (X * 0.65
	print(round(novo_salario, 2))
elif (Y == 103):
	novo_salario = X * 0.6
	print(round(novo_salario, 2))
elif (Y == 104):
	novo_salario = X * 0.55
	print(round(novo_salario, 2))
else:
	print("Entradas:", X, "e", Y, "Dados invalidos")