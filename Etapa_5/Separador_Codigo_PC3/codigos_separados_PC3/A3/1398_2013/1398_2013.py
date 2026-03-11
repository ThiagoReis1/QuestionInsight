#tempo de voo
tempo=int(input("tempo de voo em minutos"))
#custos 
if (tempo<=200):
	custo=5000+(100.00*tempo)
	print(round(custo,2))
else:
	tempo2=tempo-200
	custo2=8000+(100*200)+(90*(tempo-200.00))
	print(round(custo2,2))