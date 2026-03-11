x = input()
c = int(input("comida: "))
b = int(input("bebida: "))

if (x == "L") :
	f = (c*6)+(3*b)
	print(round(f, 1))

else :
	t = (4.50*c)+(3*b)
	print(round(t, 1))