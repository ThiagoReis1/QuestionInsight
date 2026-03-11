e=float(input("salario: "))
m=int(input("tipo: "))
if m==101 and e>=0:
	print("Entradas: R$", e ,"e codigo", m)
	print("Novo salario: R$", round(e*0.08+e,2))
elif m==102 and e>=0:
	print("Entradas: R$", e ,"e codigo", m)
	print("Novo salario: R$", round(e*0.65+e,2))
elif m==103 and e>=0:
	print("Entradas: R$", e ,"e codigo", m)
	print("Novo salario: R$", round(e*0.6+e,2))
elif m==104 and e>=0:
	print("Entradas: R$", e ,"e codigo", m)
	print("Novo salario: R$", round(e*0.55+e,2))
else:
	print("Entradas: R$", e ,"e codigo", m)
	print("Dados invalidos")