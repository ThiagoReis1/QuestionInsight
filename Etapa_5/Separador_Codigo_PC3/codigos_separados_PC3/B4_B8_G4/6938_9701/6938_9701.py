val = float(input("qual o valor da sua compra? "))
pag = input("qual sua forma de pagamento? ").upper()
if pag == "C":
	card = int(input("deseja pagar em 1 ou 2 vezes? "))
	if card == 1:
		print(round(val, 2))
	elif card == 2:
		total = val + (val*0.06)
		print(round(total, 2))
elif pag == "D":
	total = val - (val*0.11)
	print(round(total, 2))
elif pag == "P":
	total = val - (val*0.11)
	print(round(total, 2))