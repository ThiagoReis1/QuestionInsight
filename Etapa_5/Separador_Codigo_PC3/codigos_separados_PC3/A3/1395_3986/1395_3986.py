var1=float(input("valor de vendas do funcionario: "))
comissao1=0.05
comissao2=0.10
if(var1 <= 1000):
	x=var1 * comissao1
	print(round(x,2))
else:
	e=var1 - 1000
	y=(1000 * comissao1) + ((var1 - 1000) * comissao2)
	print(round(y,2))