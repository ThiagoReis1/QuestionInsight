quan = int(input("Quantidade: "))

if (quan >= 5):
	final = quan * 3.45
	print(round(final, 2))
else:
	final = quan * 3.80
	print(round(final, 2))