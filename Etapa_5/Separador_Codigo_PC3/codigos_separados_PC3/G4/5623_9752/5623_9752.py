A = input("B ou S: ")
B = int(input("Qual a quantidade de B ou S: "))
C = int(input("Qual a quantidade de cappuccinos: "))

if A == "B":
	x = B * 5.00
	y = C * 7.50
	print(x+y)
else:
	d = B * 4.00
	v = C * 7.50
	print(d+v)