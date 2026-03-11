qm=int(input("quantidade inicial de mana: "))
mg=int(input("qunatidade de mana gasta: "))
mr=int(input("quantidae de mana que recupera: "))

quandmana=qm
qdias=0

while(quandmana > 0):
	quandmana = quandmana - mg + mr
	qdias= qdias + 1
	
print(qdias)
