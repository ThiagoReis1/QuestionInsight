velocidade_i = float(input("velocidade em Mbps:"))

if velocidade_i < 50:
	custo = 60 + 4.50
elif velocidade_i == 50:
	custo = 60 + 5.50
else:
	custo = 60 + 6.50
print(custo)