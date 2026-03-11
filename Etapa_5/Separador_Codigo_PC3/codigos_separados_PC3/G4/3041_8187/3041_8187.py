x= float(input("valor de x: "))

if(-1000 <= x)and(x < -2):
	cal= -1/(x+2)
	print(round(cal,4))
elif(2 < x)and(x <= 1000):
	cal= 1/(x-2)
	print(round(cal,4))
else:
	print("entrada invalida")
