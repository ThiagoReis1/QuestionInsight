x = float(input("Digite o numero de vendas: "))

if(x<=1000):
	total = x*0.05
	print(round(total, 2))
else:
	y = x - 1000
	total = y* 0.10+1000*0.05
	print(round(total, 2))