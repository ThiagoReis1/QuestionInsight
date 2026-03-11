tp = input("Informe T para fatia de torta ou P para pastel: ")
quant = int(input("Informe a quantidade de tortas ou de pasteis: "))
capp = int(input("Informe a quantidade de cappuccinos: "))

if tp.upper() == "T":
	total1 = quant * 6 + capp * 4.5
	print(round(total1, 2))
else: 
	total2 = quant * 5 + capp * 4.5
	print(round(total2, 2))