qi = int(input("Quantidade incial: "))
qx = int(input("Treinados por trimestre: "))
qy = int(input("Contaminados por Trimestre: "))


qt = 0

while(qi>0):
	qi = qi-qy+qx
	qt = qt+1
print(qt)
