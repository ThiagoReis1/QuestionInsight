s = float(input("Digite o salario atual: "))
c = int(input("Digite o codigo: "))

print("Entradas: R$", s, "e codigo", c)

if(s >=0):
	if(c == 101):
		n = s+s * 0.8/100 
		print("Novo salario: R$",n)	
	elif(c == 102):
		n = s+s * 0.65/100 
		print("Novo salario: R$",n)
	elif(c == 103):
		n = s+s * 0.60/100 
		print("Novo salario: R$", n)	
	elif(c == 104):
		n = s+s * 0.55/100 
		print("Novo salario: R$",n)
else:
	print("Dados invalidos")