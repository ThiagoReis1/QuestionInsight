nomedaarma = input("Katana ou Sabre: ")
D = int(input("Destreza do personagem: "))
lado1 = int(input("Valor 1: "))
lado2 = int(input("Valor 2:"))

if(nomedaarma == "katana"):
	x = (2 * (lado1 + lado2)) + D
	
else:
	x = (lado1 + lado2) + (2 * D)
	
print(x)