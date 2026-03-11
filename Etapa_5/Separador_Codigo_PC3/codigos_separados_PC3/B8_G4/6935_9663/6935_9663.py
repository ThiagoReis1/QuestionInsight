total = float(input("Informe o valor da compra: "))
cod = input("informe a opcao de pagemento: ").upper()

if cod == "C":
	p= int(input("quantas vezes?"))
	if p == 2:
		t = total + (total * 0.07)
		print(round(t,2))
	else:
		t = total
		print(t)
elif cod == "P":
	F = total - (total * 0.12)
elif cod == "D":
	F = total - (total * 0.12)
	
	print(round(F,2))
	