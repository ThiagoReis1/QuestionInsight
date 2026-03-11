x = int(input("Quantidade inicial: "))
y = int(input("Grifos treinados: "))
k = int(input("Grifos contaminados: "))
perdas = (k - y)
trimestre = 0
grifos = 0

while(x>0):
	x = x - perdas
	trimestre = trimestre + 1
	
print(trimestre) 

	


