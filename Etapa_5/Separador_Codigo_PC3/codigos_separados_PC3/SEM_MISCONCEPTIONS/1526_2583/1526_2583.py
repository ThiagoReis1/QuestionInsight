mana = int(input())
mana2 = int(input())
mana3 = int(input())

dia = 0

while(mana > 0):
	mana = (mana - mana2) + mana3
	dia = dia + 1

print(int(dia))
