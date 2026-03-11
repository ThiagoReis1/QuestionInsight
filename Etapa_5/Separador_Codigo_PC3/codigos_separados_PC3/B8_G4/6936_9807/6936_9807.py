a = float(input("valor total da compra: "))
b = input("forma de pagamento: ")



if b == "D":
	var1 = a - (a * 13/100)
	print(round(var1,2))
elif b == "P":
	var2 = a - (a * 13/100)
	print(round(var2,))
elif b == "C":
	c = int(input("Quantas vezes?: "))
	if c == 1:
		print(round(a,2))
	else:
		x = a + (a * 8/100)
		print(round(x,2))