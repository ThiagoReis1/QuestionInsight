x = input("Lanche ou salg")
q = int(input("quantidades de lanches ou salg"))
r = int(input("quantidades de refri"))

L = "Lanche"
S = "Salgado"
c = r*4

if (x == "L"):
	a = q*5
	print(c+a)
else:
	b = q*3.5
	print(b+c)
	

