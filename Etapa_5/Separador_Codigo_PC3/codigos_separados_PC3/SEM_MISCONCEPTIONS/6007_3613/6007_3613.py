#milho = 1.85
# quant>6 milho = 1.50

quant = int(input())

if quant >= 6:
	print(quant*1.50)
else:
	print(quant*1.85)