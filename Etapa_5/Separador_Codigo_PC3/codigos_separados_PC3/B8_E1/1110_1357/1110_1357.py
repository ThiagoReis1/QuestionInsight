prato = int(input())
sobremesa = int(input())
bebida = int (input())
if (prato<1 or prato>4 or sobremesa<1 or sobremesa>4 or bebida<1 or bebida>4):
	print ("Entradas", prato,",", sobremesa, ",", bebida)
	print("Dados invalidos")
else:
	if(prato==1):
		x=275
		print(x)
	elif (prato==2):
		x=410
		print (x)
	elif (prato==3):
		x=520
		print (x)
	elif (prato==4):
		x=615
		print(x)
		
		
		