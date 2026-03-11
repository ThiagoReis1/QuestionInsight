q = input("bolo ou salgado: ")
quant1 = int(input("quantidade: "))
quant2 = int(input("quantidade: "))

if q.upper() == "B":
	total = quant1 * 5 + quant2 * 7.5
	print(round(total, 2))
else :
	total = quant1 * 4 + quant2 * 7.5
	print(round(total, 2))