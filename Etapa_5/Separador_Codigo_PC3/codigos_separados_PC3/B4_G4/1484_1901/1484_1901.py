from math import*
a=input("Digite o nome do equipamento:")
b=int(input("Capacidade de Carga do Caminhão em Kg:"))
COMP=12
FRE=52
FUR=(1.7)
LIQ=(1.8)
MIC=15
NOT=(2.5)
TV=15
VENT=(2.4)
	
if (b<0) or (b>1000):
	print("Entrada invalida")
elif(a=="COMPUTADOR"):
	print(int(b/COMP))
elif (a=="FREEZER"):
	print(int(b/FRE))
elif(a=="FURADEIRA"):
	print(int(b/FUR))
elif(a=="LIQUIDIFICADOR"):
	print(int(b/LIQ))
elif(a=="MICROONDAS"):
	print(int(b/MIC))
elif(a=="NOTEBOOK"):
	print(int(b/NOT))
elif(a=="TELEVISOR"):
	print(int(b/TV))
elif(a=="VENTILADOR"):
	print(int(b/VENT))
else:
	print("Entrada invalida")



	
	
