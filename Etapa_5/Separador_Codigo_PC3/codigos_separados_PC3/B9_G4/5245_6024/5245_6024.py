x = float(input("Insira um valor: "))
if x>0:
	if x<=800:
		resp = (x*50/100)+x
		print("Entrada: R$", x)
		print("Novo salario: R$", round(resp,2))
	elif x>800 and x<=1000:
		resp = (x*40/100)+x
		print("Entrada: R$", x)
		print("Novo salario: R$", round(resp,2))
	elif x>1000 and x<=1200:
		resp = (x*30/100)+x
		print("Entrada: R$", x)
		print("Novo salario: R$", round(resp,2))
	elif x>1200 and x<=1400:
		resp = (x*20/100)+x
		print("Entrada: R$", x)
		print("Novo salario: R$", round(resp,2))
	elif x>1400 and x<=1600:
		resp = (x*10/100)+x
		print("Entrada: R$", x)
		print("Novo salario: R$", round(resp,2))
	else:
		resp = (x*5/100)+x
		print("Entrada: R$", x)
		print("Novo salario: R$", round(resp,2))
else:
	print("Entrada: R$", x)
	print("Dado invalido")