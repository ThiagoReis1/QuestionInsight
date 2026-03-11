qnt_f = int(input("digite quantidade de pontos: "))
qnt_i = int(input("digite quantidade de pontos: "))
qnt_r = int(input("digite quantidade de pontos: "))
g = 5
rodadas = 0
troll = qnt_i
while (troll > 0):
	ataque = troll + qnt_r - (qnt_f * g)
	troll = ataque +  qnt_r - (qnt_f * g)
	rodadas = rodadas + 1
print(rodadas)
