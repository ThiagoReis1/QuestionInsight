comida = input()
qtd = float(input())
suco = float(input())

if comida == 'C':
	print(round((qtd*2)+(suco*6), 2))
elif comida == 'E':
	print(round((qtd*4.5)+(suco*6), 2))