s=float(input("qual o salario atual?"))
c=int(input("qual o codigo?"))
if (s>0 and c>=101 and c<=104):
	if c==101:
		ns=s+s*0.8/100
		print("Entradas: R$", s, "e codigo",c)
		print("Novo salario: R$", round(ns,2))
	elif c==102:
		ns=s+s*0.65/100
		print("Entradas: R$", s, "e codigo",c)
		print("Novo salario: R$", round(ns,2))
	elif c==103:
		ns=s+s*0.6/100
		print("Entradas: R$", s, "e codigo", c)
		print("Novo salario: R$",round(ns,2))
	elif(c==104):
		ns=s+s*0.55/100
		print("Entradas: R$", s, "e codigo", c)
		print("Novo salario: R$", round(ns,2))
else:
	print("Entradas: R$",s, "e codigo", c )
	print("Dados invalidos")