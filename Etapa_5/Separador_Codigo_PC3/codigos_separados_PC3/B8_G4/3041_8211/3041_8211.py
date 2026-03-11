x = float(input("numero: "))
if(-1000 <= x) and (x < -2):
	t = -1/(x + 2)
	print(round(t, 4))
elif(2 < x) and (x <= 1000):
	t2 = 1/(x-2)
	print(round(t2, 4))
if(x >= -2) and (x <= 2):
	print("entrada invalida")