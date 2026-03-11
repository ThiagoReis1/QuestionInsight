v = float(input("valor da mensalidade: "))
c = int(input("numero de criancas: "))

if (c == 1):
	x = (v*c)
	val = (x - x*(0.1))
	print(round(val, 2))
elif (c == 2):
	x = (v*c)
	val = (x- x*(0.3)) 
	print(round(val, 2))
elif (c >= 3):
	x = (v*c)
	val = (x - x*(0.4))
	print(round(val, 2))