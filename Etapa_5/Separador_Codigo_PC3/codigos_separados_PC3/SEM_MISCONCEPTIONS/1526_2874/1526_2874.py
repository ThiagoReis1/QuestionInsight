mana0 = float(input("Mana: "))
gasto = float(input("Gasto:"))
recupera = float(input("Recupera:"))
t = 0
mana = mana0

while(mana > 0):
	mana -= gasto
	mana += recupera
	t += 1
	#print(mana)
	
print(t)
