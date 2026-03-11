vendas= float(input())
if(vendas<=1000):
	comissao= vendas*0.05
else:
	dif= vendas-1000
	comissao= (1000*0.05)+(dif*0.10)
print(round(comissao,2))