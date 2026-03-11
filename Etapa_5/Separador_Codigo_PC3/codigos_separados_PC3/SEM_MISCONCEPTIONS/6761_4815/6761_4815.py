# faça seu código aqui!
velocidade = int(input())
taxa = 60.
if velocidade > 50:
	taxa += 6.5
elif velocidade == 50:
	taxa += 5.5
else:
	taxa += 4.5
print(round(taxa, 2))