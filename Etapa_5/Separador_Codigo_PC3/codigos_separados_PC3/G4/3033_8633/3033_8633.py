x = float(input("abra: "))

if(-100<= x <0):
	t = -1/x
	print(round(t, 4))
elif(0 < x <=100):
	t = 1/x
	print(round(t, 4))
else:
	print('entrada invalida')

	