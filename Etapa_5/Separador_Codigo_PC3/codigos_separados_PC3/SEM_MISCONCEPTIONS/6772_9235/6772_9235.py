valor_total = float(input("digite o valor total: "))
codigo_pagamento = input("digite o codigo de pagamento: ")

if(codigo_pagamento == "D") or (codigo_pagamento == "P"):
	valor_final = valor_total - (valor_total * 17/100)
elif(codigo_pagamento == "C1"):
	valor_final = valor_total
else:
	valor_final = valor_total + (valor_total * 8/100)

print(round(valor_final, 2))