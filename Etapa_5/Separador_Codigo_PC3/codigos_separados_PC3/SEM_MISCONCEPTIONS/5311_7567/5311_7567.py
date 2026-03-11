di = float(input(""))
meses = int(input(""))
i = 0
total = di
while(i < meses):
	i = i + 1
	total = total + (total * 1.2/100)
	print(round(total, 2))