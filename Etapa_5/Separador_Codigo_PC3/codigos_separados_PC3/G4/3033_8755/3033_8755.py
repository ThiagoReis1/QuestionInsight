n= float(input("digite aqui o numero: "))

if (-100<= n < 0):
	e=(-1/n)
	print(round(e,4))
elif (0 < n <= 100):
	e=(1/n)
	print(round(e,4))
else:
	print("entrada invalida")