vv = float(input("digite o valor de vendas"))

if (vv < 1000):
	comissao =  (vv*(0.05))
else:
	comissao = (1000*0.05 + (vv-1000)*0.1)
	
print(round(comissao,2))

