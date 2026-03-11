tempo = int(input())

if (tempo <= 200):
	preco = 5000 + (100*tempo)
	print(round(preco,2))

else:
	preco =  8000 + (100*200) + 90*(tempo - 200)
	print(round(preco,2))