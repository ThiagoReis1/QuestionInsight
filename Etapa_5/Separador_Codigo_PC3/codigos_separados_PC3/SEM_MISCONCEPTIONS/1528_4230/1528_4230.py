danopg=int(input())
hp=int(input())
regen=int(input())
g = 5
rodadas = 0

while(hp>0):
	dano = g * danopg
	hp = hp - dano + regen
	rodadas = rodadas + 1
print(rodadas)
	