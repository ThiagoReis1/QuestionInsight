x = float(input("qual o valor de x: "))
t1 = -(1/(x+2))
t2 = (1/(x-2))
if (x >= -1000) and (x < -2):
	print(round(t1,4))
elif (x > 2) and (x <= 1000):
	print(round(t2,4))
else:
	print("entrada invalida")