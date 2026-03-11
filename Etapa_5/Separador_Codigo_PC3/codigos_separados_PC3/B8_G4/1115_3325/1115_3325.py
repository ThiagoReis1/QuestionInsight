x = float(input("salario atual: "))
y = int(input("seu cod. correspondente: "))
print("Entradas: R$", x,"e codigo", y)
if(y==101)or(y==102)or(y==103)or(y==104):
	if(y==101):
		ns= x+(x*0.8/100)
		print("Novo salario: R$", round(ns,2))
	elif(y==102):
		ns= x+(x*0.65/100)
		print("Novo salario: R$", round(ns,2))
	elif(y==103):
		ns= x+(x*0.6/100)
		print("Novo salario: R$", round(ns,2))
	elif(y==104):
		ns= x+(x*0.55/100)
		print("Novo salario: R$", round(ns,2))
else:
	print("Dados invalidos")
