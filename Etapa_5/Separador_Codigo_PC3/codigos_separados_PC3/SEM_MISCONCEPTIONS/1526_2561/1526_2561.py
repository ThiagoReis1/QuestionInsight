mana0 = int(input())
manaG = int(input())
manaR = int(input())

mana = mana0
dias = 0
while (mana > 0):
	mana = mana - manaG + manaR
	dias = dias + 1
	
print(dias)