s = float(input())
c = int(input())
print("Entradas: R$", s,"e codigo",c)
if (s>0 and c>0):
	if(c == 101):
		ns = s + (s*0.80/100)
		print("Novo salario: R$", round(ns,2))
	elif (c == 102):
		ns = s + (s*0.65/100)
		print("Novo salario: R$", round(ns, 2))
	elif (c == 103):
		ns = s + (s*0.60/100)
		print("Novo salario: R$", round(ns, 2))
	elif(c == 104):
		ns = s + (s*0.55/100)
		print("Novo salario: R$", round(ns, 2))
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")
