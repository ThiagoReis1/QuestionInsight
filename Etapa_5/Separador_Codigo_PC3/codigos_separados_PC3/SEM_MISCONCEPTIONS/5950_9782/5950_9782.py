pedido1 = input("T ou P: ")
qnt_fatias = int(input("Quantidade de fatias de torta ou pastel: "))
qnt_cap = int(input("Quantidade de cappuccinos: "))

valor_torta = 6
valor_pastel = 5
cap = 4.50

if pedido1 == "T":
	total = (qnt_fatias * valor_torta) + (qnt_cap * cap)
	print(round(total,2))
else:
	total = (qnt_fatias * valor_pastel) + (qnt_cap * cap)
	print(round(total, 2))