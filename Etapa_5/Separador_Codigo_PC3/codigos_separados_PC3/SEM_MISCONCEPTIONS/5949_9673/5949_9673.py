fatia = input("B se for bolo ou C se for croissant: ").upper()
quantidade = int(input("quantidade de fatias: "))
quantidade2 = int(input("quantidade de cappucinos: "))

if fatia == "B":
	total = (quantidade * 3.00) + (quantidade2 * 5.50)
	print(round(total, 2))
else: 
	total = (quantidade * 6.00) + (quantidade2 * 5.50)
	print(round(total,2))
	
