E = input("L ou S: ")

if(E == "L"):
	L = int(input("lanches: "))
	R = int(input("refrigerante: "))
	c = L*5.00+R*4.00
	print(c)
else:
	S = int(input("salgado: "))
	R = int(input("refrigerante: "))
	C = S*3.50+R*4.00
	print(C)

	
	