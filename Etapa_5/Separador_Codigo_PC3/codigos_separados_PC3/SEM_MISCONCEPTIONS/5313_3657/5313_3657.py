process=float(input("De a velocidade do processador: "))
primeiro=7206.14
anos=0
while(primeiro<process):
	primeiro=0.65*primeiro+primeiro
	anos=anos+1
anos=2018+anos
print(anos)