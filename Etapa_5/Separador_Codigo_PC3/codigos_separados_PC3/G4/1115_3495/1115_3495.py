s=float(input())
c=int(input())

if (c==101):
	a=s*0.008
	stotal=round(a+s,2)
	print("Entradas: R$",s,"e codigo",c)
	print("Novo salario: R$",stotal)
elif (c==102):
	a=s*0.0065
	stotal=round(a+s,2)
	print("Entradas: R$",s,"e codigo",c)
	print("Novo salario: R$",stotal)
elif (c==103):
	a=s*0.006
	stotal=round(a+s,2)
	print("Entradas: R$",s,"e codigo",c)
	print("Novo salario: R$",stotal)
elif (c==104):
	a=s*0.0055
	stotal=round(a+s,2)
	print("Entradas: R$",s,"e codigo",c)
	print("Novo salario: R$",stotal)
else:
	print("Entradas: R$",s,"e codigo",c)
	print("Dados invalidos")