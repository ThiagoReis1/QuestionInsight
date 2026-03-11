sa = float(input('salario atual de um funcionario')) 

print("Entrada: R$",round(sa, 2))

if (sa>0 and sa<=800):
	nv = sa * 1.5
	print("Novo salario: R$",round(nv, 2))	
elif(sa>800 and sa<=1000):
	nv = sa * 1.4
	print("Novo salario: R$",round(nv, 2))	
elif(sa>1000 and sa<=1200):
	nv = sa * 1.3
	print("Novo salario: R$",round(nv, 2))	
elif(sa>1200 and sa<=1400):
	nv = sa * 1.2
	print("Novo salario: R$",round(nv, 2))	
elif(sa>1400 and sa<=1600):
	nv = sa * 1.1
	print("Novo salario: R$",round(nv, 2))	
elif(sa>1600):
	nv = sa * 1.05
	print("Novo salario: R$",round(nv, 2))	
else:
	print("Dado invalido")