TP = input("Informe se e T ou P: ")
quant = int(input("Informe a quantidade de torta ou pastel: "))
quantCap = int(input("Informe a quantidade de cappuccinos: "))

if TP == "T":
	ValorTotal = quant * 6 + quantCap * 4.50
	
else:
	TP == "P"
	ValorTotal = quant * 5 + quantCap * 4.50
	
print(round(ValorTotal, 2))