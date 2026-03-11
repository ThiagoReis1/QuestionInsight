tempo = float(input("Digite o tempo em minutos: "))
if tempo > 200:
	custo = 8000 + 200*100 + (tempo - 200)*90
else:
	custo = 5000 + tempo*100
print(round(custo,2))