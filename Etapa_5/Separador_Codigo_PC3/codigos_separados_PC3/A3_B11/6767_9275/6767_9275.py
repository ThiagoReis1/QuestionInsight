valor_da_compra = float(input("valor de compra total: "))
forma_de_pagamento = (input("digite o valor do codigo: "))

if forma_de_pagamento == D:
	some = valor_da_compra * 0.12
if forma_de_pagamento == P:
	some = valor_da_compra * 0.12
if forma_de_pagamento == C1:
	some = valor_da_compra
if forma_de_pagamento == C2:
	some = valor_da_compra * 0.7 
	
print(round(some, 2))