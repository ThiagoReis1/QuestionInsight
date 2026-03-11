comida = input("Digite L ou S: ").upper()
quantidade = int(input("Digite o numero de comida: "))
refrigerante = int(input("Digite o numero de refrigerante: "))
L = 5.00
S = 3.50
R = 4.00 
if comida == "L" :
	valor = (L*quantidade)+ (refrigerante*R)
	print(valor)
else:
	valor1 = (S*quantidade) + (refrigerante*R)
	print(valor1)