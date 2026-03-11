ataque = str(input("tipo de ataque: "))
d1 = int(input("d1: "))
d2 = int(input("d2: "))
d3 = int(input("d3: "))
d4 = int(input("d4: "))

if(ataque == "espada"):
	esp = (d1*d2*d3*d4 + 4) + 6
	print(esp)
else:
	cau = (d1+d2+d3)*d4
	print(cau)