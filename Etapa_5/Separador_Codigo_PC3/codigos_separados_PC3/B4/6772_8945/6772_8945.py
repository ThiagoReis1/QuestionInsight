valor_compra = float(input("Digite o valor total da compra: "))
codigo_pagamento = input("Digite o cogigo de pagamento: ").upper

if codigo_pagamento == "D":
	print(-0.17 * valor_compra)
elif codigo_pagamento == "p":
   print(-0.17 * valor_compra)
elif codigo_pagamento == "C1":
	print(valor_compra)
elif codigo_pagamento == "C2":
	print(0.08 * valor_compra)
else:
	print()
	
valor_compra = round(valor_compra, 2)
