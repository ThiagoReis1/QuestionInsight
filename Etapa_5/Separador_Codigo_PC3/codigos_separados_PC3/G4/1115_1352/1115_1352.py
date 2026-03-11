x=float(input("valor:"))
y=int(input("cargo:"))

if(x<80)or(x<65)or(x<60)or(x<55):
	print("Entradas: R$",x,"e codigo",y)
	print("Dados invalidos")
else:
	print("Entradas:R$",x,"e codigo",y)
	print("Novo salario: R$",x+y(round,2))