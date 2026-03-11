#variaveis
fatb = 5
salg = 4
capp = 7.50

pedido1 = input(" informe se e bolo ou salgado: ")
quantidade = int(input(" informe a quantidade: "))
cappuccino = int(input(" quantidade: "))

if pedido1.upper() == "B":
	pedido = fatb * quantidade
	p1 = pedido + (cappuccino * capp)
	
else: 
	pedido = salg * quantidade
	p1 = pedido + (cappuccino * capp)

total_pagamento = p1
print(round(total_pagamento,2))

	


	