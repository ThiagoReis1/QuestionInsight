from numpy import*

de = array(eval(input("Golpe de espada: ").upper()))
nc = array(eval(input("Nível dos combatentes: ")))
CENOURA = 2
FERRO = 4
DWARVEN = 8
ELVEN = 11
DAEDRIC = 14
x = 0
i = 0
while(i < size(nc)):
	x = x + de[i]*nc[i]
	i = i + 1
print(x)
	