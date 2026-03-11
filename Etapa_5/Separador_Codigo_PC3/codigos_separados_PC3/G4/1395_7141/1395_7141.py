v = float(input("Qual e o valor de vendas de um funcionario: "))

if(v <= 1000):
	c = v*0.05
	print(round(c, 2))
else:
	c = v*10/100-1000*0.05/1000-5/100
	print(round(c, 2))
			