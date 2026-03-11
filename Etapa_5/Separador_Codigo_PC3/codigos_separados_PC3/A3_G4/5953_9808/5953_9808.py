L = float ("6.00")
P = float ("13.50")
r = float ("3.00")

x = input("(L) lanche e (P) prato executivo: ")
y = int(input("Quantidade: "))
z = int(input("Quantos refrigerantes: "))

if (x == "L"):
	print(round(((y*6.00) + (z*3.00)),2))
	
else: 
	print (round(((y*13.50 + z*3.00)),2))