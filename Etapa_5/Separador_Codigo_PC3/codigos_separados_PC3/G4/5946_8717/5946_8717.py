a = input("(L/P): ")
b = int(input("Quantos pedidos: "))
c = int(input("Quantos refris: "))

l = b*6.0
p = b*4.5
r = c*3.0

if (a == "L"):
	t = l+r
	print(round(t, 2))
	
if (a == "P"):
	t = p+r
	print(round(t, 2))