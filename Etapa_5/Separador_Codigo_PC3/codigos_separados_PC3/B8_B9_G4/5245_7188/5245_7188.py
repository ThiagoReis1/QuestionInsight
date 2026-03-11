sa= float(input("salario atual"))
if sa > 0:
	if sa<= 800:
		p= sa+ (sa*0.50)
		print("Entrada: R$",sa)
		print("Novo salario: R$", round(p,2))
	elif sa> 800 and sa<= 1000:
		p= sa+ (sa*0.40)
		print("Entrada: R$",sa)
		print("Novo salario: R$",round(p,2))	
	elif sa>1000 and sa<= 1200:
		p= sa+ (sa*0.30)
		print("Entrada: R$",sa)
		print("Novo salario: R$",round(p,2))
	elif sa>1200 and sa<= 1400:
		p= sa+ (sa*0.20)
		print("Entrada: R$",sa)
		print("Novo salario: R$",round(p,2))
	elif sa>1400 and sa<= 1600:
		p= sa+ (sa*0.10)
		print("Entrada: R$",sa)
		print("Novo salario: R$" ,round(p,2))
	elif sa > 1600:
		p= sa+ (sa*0.05)
		print("Entrada: R$",sa)
		print("Novo salario: R$",round(p,2))
else:
	print("Dado invalido")