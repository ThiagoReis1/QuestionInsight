tv = int(input("tempo de voo: "))
m = 60

if (tv <= 200) :
	mensagem = (5000 + (100*m))
	print(round(mensagem,2))
else:
	mensagem = (8000 + (100*200) + (90*m))
	print(round(mensagem,2))
