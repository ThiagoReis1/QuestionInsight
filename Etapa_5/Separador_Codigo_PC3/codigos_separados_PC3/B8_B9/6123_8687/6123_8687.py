c = float(input("Quantidade de combustivel comum: "))

if c > 0:
	if c < 17.5:
		zylium = c + 0.8
	elif c >= 17.5 and c < 35:
		zylium = c + 1.3
	elif c >= 35 and c < 50:
		zylium = c + 2.1
	elif c >= 50:
		zylium = c + 3
else:
	print("Error")
print(zylium)