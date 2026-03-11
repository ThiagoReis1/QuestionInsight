tempo = int(input("Digite o tempo de voo: "))

if ( tempo <= 200):
	custo = 5000.0 + (100 * tempo)
	print(round(custo, 2))
	
else:
	custo = 8000.0 + (100 * 200) + ( tempo - 200) * 90
	print(round(custo, 2))