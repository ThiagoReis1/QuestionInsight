n=input().upper()
a=int(input())
if(a<0 or a>1000):
	print("Entrada invalida")
elif(n=="COMPUTADOR"):
	print(round(a*12,2))
elif(n=="FREEZER"):
	print(round(a*52,2))
elif(n=="FURADEIRA"):
	print(round(a*1.7,2))
elif(n=="LIQUIDIFICADOR"):
	print(round(a*1.8,2))
elif(n=="MICROONDAS"):
	print(round(a*15,2))
elif(n=="NOTEBOOK"):
	print(round(a*2.5,2))
elif(n=="TELEVISOR"):
	print(round(a*15,2))
elif(n=="VENTILADOR"):
	print(round(a*2.4,2))
else:
	print("Entrada invalida")
