nome= input("nome: ").upper()
quantidade= int(input("quantidade: "))

if nome=="SALMAO" and quantidade>=0 and quantidade <=1000:
	por=quantidade//300
	print(por)
elif nome=="ARROZ" and quantidade>=0 and quantidade <=1000:
	por=quantidade//500
	print(por)
elif nome=="CENOURA" and quantidade>=0 and quantidade <=1000:
	por=quantidade//100
	print(por)
elif nome=="KAMPYO" and quantidade>=0 and quantidade <=1000:
	por=quantidade//20
	print(por)
elif nome=="NORI" and quantidade>=0 and quantidade <=1000:
	por=quantidade//50
	print(por)
elif nome=="OMELETE" and quantidade>=0 and quantidade <=1000:
	por=quantidade//200
	print(por)
elif nome=="PEPINO" and quantidade>=0 and quantidade <=1000:
	por=quantidade//150
	print(por)
elif nome=="SHITAKE" and quantidade>=0 and quantidade <=1000:
	por=quantidade//150
	print(por)
else:
	 print("Entrada invalida")