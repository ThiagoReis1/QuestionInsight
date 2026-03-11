from numpy import*
ent = input("").upper()
acum = 0
for i in range (len(ent)):
	if(ent[i] == 'C'):
		acum = acum + 1
print(acum)
	
	