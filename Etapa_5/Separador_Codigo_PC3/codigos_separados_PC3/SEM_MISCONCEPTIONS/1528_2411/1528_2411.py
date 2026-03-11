ataque = int(input())
vida = int(input())
reg = int(input())
rodada = 0
while(vida > 0):
	x = 5*ataque
	vida = vida - x + reg
	rodada = rodada + 1
print(rodada)
	