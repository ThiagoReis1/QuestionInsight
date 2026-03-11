x = float(input("valor de x: "))

if x <= -100 or x < 0:
	total = - 1/x
	print(round(total, 4))
	
elif 0 < x and x <= 100:
	total = 1/x
	print(round(total, 4))
else:
	print ("entrada invalida")