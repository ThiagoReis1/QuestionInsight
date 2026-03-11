x = input("L ou S: ")
y = float(input("Quantidade de L ou S: "))
z = float(input("Quantidade de refrigerantes: "))

lanche = (y * 5.00) + (z * 4.00)
salgado = (y * 3.50) + (z * 4.00)

if(x == "L"):
	print(lanche)
	
else:
	print(salgado)