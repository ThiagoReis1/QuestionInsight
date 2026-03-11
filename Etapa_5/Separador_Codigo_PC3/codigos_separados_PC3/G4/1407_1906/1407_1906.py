x = int(input("Quantidade inicial de pontos de vida:"))
y1 = int(input("O primeiro valor sorteado no lancamento:"))
y2 = int(input("O segundo valor sorteado no lancamento:"))
y3 = int(input("O terceiro valor sorteado no lancamento:"))
n = y1+y2+y3
if (x-10*n>0):
	print(x-10*n)
	print("VIVO")
else:
	print("O")
	print("MORTO")
	