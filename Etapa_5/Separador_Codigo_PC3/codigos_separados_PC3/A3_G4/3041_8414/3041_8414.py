x = float(input(""))
cont = 0

if -1000 <= x and x < -2:
	cont = -(1/(x+2))
	print(round(cont, 4))
elif 2 < x and x <= 1000: 
	cont = (1/(x-2))
	print(round(cont, 4))

else:
	print("entrada invalida")
