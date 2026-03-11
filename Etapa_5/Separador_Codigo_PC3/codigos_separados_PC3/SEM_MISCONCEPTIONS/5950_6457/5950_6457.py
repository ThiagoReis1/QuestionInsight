pedido = input("Digite T se for fatia ou P se for pastel: ")
q_pedido = int(input("Digite a quantidade de fatias de torta ou pastel: "))
q_cap = int(input("Digite a quantidade de cappuccinos: "))

t = 6.00
p = 5.00
c = 4.50

if pedido == "T":
	v = (q_pedido * t) + (q_cap * c)
else:
	v = (q_pedido * p) + (q_cap * c)
print(round(v, 2))
	