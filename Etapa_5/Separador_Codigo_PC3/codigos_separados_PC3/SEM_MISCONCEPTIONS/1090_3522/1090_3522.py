limite = float(input("limite do cartao: "))
compra1 = float(input("valor da compra1: "))
compra2 = float(input("valor da compra2: "))
compra3 = float(input("valor compra3: "))
compra4 = float(input("valor compra4: "))
if(round(compra1 + compra2 + compra3+ compra4,2) <= limite):
		msg = "Dentro do limite"
else:
		msg = "Estourou o limite"	
print(round(compra1 + compra2 + compra3 + compra4, 2)) 
print(msg)