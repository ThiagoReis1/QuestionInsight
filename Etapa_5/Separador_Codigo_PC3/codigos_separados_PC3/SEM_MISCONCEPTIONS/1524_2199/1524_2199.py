qi = int(input("A quantidade inicial de grifos do rei Gardoc, antes da doença:"))
qx = int(input("A quantidade X de novos grifos treinados a cada trimestre:"))
qy = int(input("A quantidade Y de grifos contaminados a cada trimestre:"))

cont = 0

while(cont  qi):
	qi = (qi + qx) - qy
	cont = cont + 1
	
print(cont)
	