qtdforc=int(input("Quantidade de força de cada guerreiro:"))
qtdtroll=int(input("Quantidade de força do troll:"))
qtdad=int(input("Quantidade recuperada pelo troll a cada rodada:"))
rodada = 0

while qtdtroll > 0:
	qtdtroll = qtdtroll - (qtdforc * 5)
	qtdtroll = qtdtroll + qtdad
	rodada = rodada + 1
print(rodada)