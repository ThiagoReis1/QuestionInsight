a= (input()).upper()
b= int(input())
if(b<0 or b>1000):
	print("Entrada invalida")
else:	
	if(a == "COMPUTADOR"):
		x= b//12
		print(int(x))
	elif(a== "FREEZER"):
		x= b//52
		print(int(x))
	elif(a== "FURADEIRA"):
		x= b//1.7
		print(int(x))
	elif(a== "LIQUIDIFICADOR"):
		x=b//1.8
		print(int(x))
	elif(a== "MICROONDAS"):
		x=b//15
		print(int(x))
	elif(a== "NOTEBOOK"):
		x= b//2.5
		print(int(x))
	elif(a== "TELEVISOR"):
		x= b//15
		print(int(x))
	elif(a=="VENTILADOR"):
		x= b//2.4
		print(int(x))
	
	
	