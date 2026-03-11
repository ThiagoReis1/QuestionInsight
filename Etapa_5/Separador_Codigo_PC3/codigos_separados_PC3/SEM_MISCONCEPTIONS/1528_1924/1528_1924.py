forca_g= int(input("insira a quantidade de força do guerreiro"))
troll= int(input("insira a quantidade de força inicial do troll"))
regen = int(input("insira quantidade de força que o troll recupera a cada rodada"))
i = 0
while(troll>0):
	troll= troll - (5 * forca_g) + regen
	i = i+1
print(i)