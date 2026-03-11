n = input("nome do equipamento: ")
c = int(input("capacidade de carga(kg): "))

if(n=="COMPUTADOR"):
	p=12
elif(n=="FREEZER"):
	p=52
elif(n=="FURADEIRA"):
	p=1.7
elif(n=="LIQUIDIFICADOR"):
	p=1.8
elif(n=="MICROONDAS"):
	p=15
elif(n=="NOTEBOOK"):
	p=2.5
elif(n=="TELEVISOR"):
	p=15
elif(n=="VENTILADOR"):
	p=2.4
else:
	print("Entrada invalida")	
q = int(c//p)
if((q<0)or(q>1000)):
	print("Entrada invalida")	
else:
	print(q)