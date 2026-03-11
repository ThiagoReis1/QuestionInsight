valor = float(input("Indique o valor da compra: "))
cod = input(" Indique o codigo do pagamento: (D,P,C1,C2)").upper()

if cod == "D":
	desc = 0.17
	juros = 0
	
elif cod == "P":
	desc = 0.17
	juros = 0
	
elif cod == "C1":
	desc = 0
	juros = 0
	
elif cod == "C2":
	desc = 0
	juros = 0.08
	
total = valor - (valor * desc) + (valor * juros)
print (round(total,2))