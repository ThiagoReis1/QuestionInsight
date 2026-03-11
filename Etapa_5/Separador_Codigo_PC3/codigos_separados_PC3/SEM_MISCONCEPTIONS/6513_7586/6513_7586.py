# faça seu código aqui
quant = int(input("quantidade: "))

if quant >= 4:
	conta = (quant * 20) 
	desconto = conta -(conta * 0.15)
	print(round(desconto,2))
						
else: 
	conta = (quant * 20)
	print(round(conta, 2))
	