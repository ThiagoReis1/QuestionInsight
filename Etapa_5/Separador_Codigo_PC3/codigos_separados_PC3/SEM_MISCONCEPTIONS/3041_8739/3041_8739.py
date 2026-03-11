x = float(input("x: "))

if (-1000 <= x) and (x <-2) :
	total = -1 / (x + 2)
	print(round(total,4))

elif (x > 2) and (1000 >= x) :
	total = 1 / (x - 2)
	print(round(total,4))
	
else :
	print("entrada invalida")