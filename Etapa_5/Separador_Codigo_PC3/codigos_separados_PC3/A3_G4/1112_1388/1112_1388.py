x=float(input("Digite o salario do funcionario: R$ "))
y=0
if x<0:
	y= -1
elif x<=800.00:
	y=x+(x/2)
elif 800.00<x<=1000.00:
	y=x+(x*(2/5))
elif 1000.00<x<=1200.00:
	y=x+(x*(3/10))
elif 1200.00<x<=1400.00:
	y=x+(x*(1/5))
elif 1400.00<x<=1600.00:
	y=x(x*(1/10))
else:
	y=x+(x*(1/20))
y=round(y, 2)
if y==-1:
	print("Entrada: R$ ",x)
	print("Dado invalido")
else: 
	print("Entrada: R$ ",x)
	print("Novo salario: R$ ",y)