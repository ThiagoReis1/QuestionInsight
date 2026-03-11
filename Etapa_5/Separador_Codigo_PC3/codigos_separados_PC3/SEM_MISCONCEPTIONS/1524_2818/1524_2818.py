qi = int (input("número de grifos:"))
x = int(input("numero de grifos treinados:"))
y = int(input("numero de grifos contaminados:"))
perdas = (y - x)
trimestre = 0


while (qi>0):
	qi = qi - perdas 
	trimestre = trimestre + 1

print (trimestre)