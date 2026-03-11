x =  float(input("X: "))

if -100 <= x < 0:
	cont = -1/x
	print(round(cont,4))
elif 0 <	x <= 100:
	cont = 1/x
	print(round(cont,4))
else:
	print("entrada invalida")
	