p = float(input("preco: "))
c = int(input("codigo: "))

d = p * 40/100
x = p - d

if(c == 1):
	f = p * 10/100
	v = x + f
	print(round(v, 2))
elif(c == 2):
	f = p * 8/100
	v = x + f
	print(round(v, 2))
elif(c == 3):
	f = 0
	v = x + f
	print(round(v, 2))
else:
	f = p * 2/100
	v = x + f
	print(round(v, 2))
	