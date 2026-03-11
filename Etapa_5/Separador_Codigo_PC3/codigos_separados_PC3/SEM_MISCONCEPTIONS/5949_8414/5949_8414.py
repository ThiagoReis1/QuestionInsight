# B = fatia de bolo
# C = croaissant

pedido = input("qual o seu pedido B ou C: ")
qb = 
if pedido == B:
	qtb = round(int(input(" qual a quantidade de fatias de bolo:")), 2)
	qta = round(int(input("qual a quantiddade de cappuccinos: ")), 2)
	B = round((3*qtb) + (5.50*qta), 2)
	print(B)
	
else:
	qtc = round(int(input("qual a quantidade de croaissant:")), 2)
	qta = round(int(input("qual a quantidade de cappuccinos: ")), 2)
	C = round((6*qtc) + (5.50*qta), 2)
	print(C)
	