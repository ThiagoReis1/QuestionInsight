ingr = input("").upper()
quant = int(input(""))

if ( quant >= 0 and quant <=1000):
	if ( ingr == "ARROZ"):
		num = quant // 500
	elif (ingr == "CENOURA"):
		num = quant // 100
	elif (ingr == "KAMPYO"):
		num = quant // 20
	elif  (ingr == "NORI"):
		num = quant // 50
	elif (ingr == "PEPINO"):
		num = quant // 150
	elif (ingr == "SALMAO"):
		num = quant // 300
	elif (ingr == "SHITAKE"):
		num = quant // 150
	print (num)
else:
	print("Entrada invalida")