salario = float(input())
codigo = int(input())
print("Entradas:","R$",salario,"e codigo",codigo)

if((codigo != 101) and (codigo != 102) and (codigo != 103) and (codigo != 104) or (salario <= 0)):
	print("Dados invalidos")
elif(codigo == 101):
	print("Novo salario:","R$",(round(salario + (0.80 * salario / 100), 2)))
elif(codigo == 102):
	print("Novo salario:","R$",(round(salario + (0.65 * salario / 100), 2)))
elif(codigo == 103):
	print("Novo salario:","R$",(round(salario + (0.60 * salario / 100), 2)))
elif(codigo == 104):
	print("Novo salario:","R$",(round(salario + (0.55 * salario / 100), 2)))