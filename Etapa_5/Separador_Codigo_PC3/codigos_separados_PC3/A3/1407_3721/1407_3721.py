vendas= float(input()) 

if (vendas<= 1.000):
	comissao= 5/100*vendas
else:
	comissao= 5/100*1.000+10/100* 
print(round(comissao,2))