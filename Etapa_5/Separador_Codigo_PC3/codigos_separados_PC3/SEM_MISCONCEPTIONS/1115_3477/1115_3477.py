st = float(input("digite o salario: "))
codigo = int(input("digite o codigo: "))
print("Entradas: R$", st, "e codigo", codigo)

if(codigo == 101):
	p = st+(st*0.80/100)
	print("Novo salario: R$",round(p,2))
elif(codigo == 102):
	p = st+(st*0.65/100)
	print("Novo salario: R$",round(p,2))	
elif(codigo == 103):
	p = st+(st*0.60/100)
	print("Novo salario: R$",round(p,2))
elif(codigo == 104):
	p = st+(st*0.55/100)
	print("Novo salario: R$",round(p,2))
else:
	print("Dados invalidos")
