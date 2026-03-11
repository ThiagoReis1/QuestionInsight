tempo= float(input(""))


if(tempo <= 200):
	custo = 5000 + ( tempo * 100)
else:
	tempo_mais= tempo - 200
	custo = 8000 + (100 * 200) + (90 * tempo_mais)
print(custo)