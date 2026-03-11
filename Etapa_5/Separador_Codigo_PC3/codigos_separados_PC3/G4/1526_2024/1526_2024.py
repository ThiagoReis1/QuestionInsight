A=int(input("mana in: "))
B=int(input("Quantidade gasta por dia: "))
C=int(input("Recupera: "))
dias=0
mana=A
while(mana>0):
	mana=(mana - B)+C
	dias=dias+1
print(dias)
	
	
	
