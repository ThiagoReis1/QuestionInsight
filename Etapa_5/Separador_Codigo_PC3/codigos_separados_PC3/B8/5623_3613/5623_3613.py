item = input()
quant = int(input())
quantc = int(input())

if item.upper() == "B":
	print(round(quant*5+quantc*7.5, 2))
else:
	if item.upper() == "S":
		print(round(quant*4 +quantc*7.5, 2))
		
