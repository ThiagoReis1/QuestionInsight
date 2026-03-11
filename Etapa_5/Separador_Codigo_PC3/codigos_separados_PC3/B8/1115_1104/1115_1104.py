from math import*
salario=float(input())
codigo=int(input())
if(salario>=0) and (codigo>=101) and (codigo<=104):
	if(codigo==101 and salario>=0):
		novo=round(salario*1.008,2)
		print("Entradas: R$", salario, "e codigo", codigo)
		print("Novo salario: R$", novo)
	elif(codigo==102 and salario>=0):
		novo=round(salario*1.0065,2)
		print("Entradas: R$", salario, "e codigo", codigo)
		print("Novo salario: R$", novo)
	elif(codigo==103 and salario>=0):
		novo=round(salario*1.006,2)
		print("Entradas: R$", salario, "e codigo", codigo)
		print("Novo salario: R$", novo)
	elif(codigo==104 and salario>=0):
		novo=round(salario*1.0055,2)
		print("Entradas: R$", salario, "e codigo", codigo)
		print("Novo salario: R$", novo)
else:
	print("Entradas: R$", salario, "e codigo", codigo)
	print("Dado invalido")