valor_total_da_compra = float(input())
codigo_da_opcao_de_pagamento = input()
#esse aqui gostei de fazer de novo, mas queria dar ctrl+c/ctrl+v nas minhas variáveis
if codigo_da_opcao_de_pagamento == "C":
	card = int(input("1 ou 2 vezes? "))
	if card == 1:
		valor_final_a_ser_pago = valor_total_da_compra
	elif card == 2:
		valor_final_a_ser_pago = valor_total_da_compra + (valor_total_da_compra * 6/100)
else:
	valor_final_a_ser_pago = valor_total_da_compra - (valor_total_da_compra * 11/100)
	
print(round(valor_final_a_ser_pago, 2)) 