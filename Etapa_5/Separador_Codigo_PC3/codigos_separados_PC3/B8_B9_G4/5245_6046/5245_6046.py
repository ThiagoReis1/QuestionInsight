sa= float(input("salario atual de um funcionario: "))

print("Entrada: R$", sa)

if sa>0:
	if sa<=800:
		n1= (sa*50)/100
		nv= sa+n1
		nv1= round(nv, 2)
		print("Novo salario: R$", nv1)
	elif sa>800 and sa<=1000:
		n1= (sa*40)/100
		nv=sa+n1
		nv1= round(nv, 2)
		print("Novo salario: R$", nv1)
	elif sa>1000 and sa<=1200:
		n1= (sa*30)/100
		nv= sa+n1
		nv1= round(nv, 2)
		print("Novo salario: R$", nv1)
	elif sa>1200 and sa<=1400:
		n1= (sa*20)/100
		nv= sa+n1
		nv1= round(nv, 2)
		print("Novo salario: R$", nv1)
	elif sa>1400 and sa<=1600:
		n1= (sa*10)/100
		nv= sa+n1
		nv1= round(nv, 2)
		print("Novo salario: R$", nv1)
	elif sa>1600:
		n1= (sa*5)/100
		nv= sa+n1
		nv1= round(nv, 2)
		print("Novo salario: R$", nv1)
		
else: 
	print("Dado invalido")