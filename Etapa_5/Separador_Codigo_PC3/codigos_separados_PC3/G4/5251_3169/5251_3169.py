x = input()
i = int(input())
cd = x.upper()
p = 30/100

if(i>=0 and i<=150 and (cd=='PORTOVELHO' or cd=='SANTAREM' or cd=='BELEM' or cd=='TEFE' or cd=='TABATINGA')):
	if(i<=2):
		if(cd=='PORTOVELHO'):
			print("Entradas: PortoVelho",",",i)
			print("Passagem: R$ 0.0")
		elif(cd=='SANTAREM'):
			print("Entradas: Santarem",",",i)
			print("Passagem: R$ 0.0")
		elif(cd=='BELEM'):
			print("Entradas: Belem",",",i)
			print("Passagem: R$ 0.0")
		elif(cd=='TEFE'):
			print("Entradas: Tefe",",",i)
			print("Passagem: R$ 0.0")
		else:
			print("Entradas: Tabatinga",",",i)
			print("Passagem: R$ 0.0")
	elif(i>=3 and i<=12):
		if(cd=='PORTOVELHO'):
			a = round((500/2), 2)
			print("Entradas: PortoVelho",",",i)
			print("Passagem: R$",a)
		elif(cd=='SANTAREM'):
			a = round((370/2), 2)
			print("Entradas: Santarem",",",i)
			print("Passagem: R$",a)
		elif(cd=='BELEM'):
			a = round((600/2), 2)
			print("Entradas: Belem",",",i)
			print("Passagem: R$",a)
		elif(cd=='TEFE'):
			a = round((360/2), 2)
			print("Entradas: Tefe",",",i)
			print("Passagem: R$",a)
		else:
			a = round((550/2), 2)
			print("Entradas: Tabatinga",",",i)
			print("Passagem: R$",a)
	elif(i>12 and i<65):
		if(cd=='PORTOVELHO'):
			a = round(500, 2)
			print("Entradas: PortoVelho",",",i)
			print("Passagem: R$",a)
		elif(cd=='SANTAREM'):
			a = round(370, 2)
			print("Entradas: Santarem",",",i)
			print("Passagem: R$",a)
		elif(cd=='BELEM'):
			a = round(600, 2)
			print("Entradas: Belem",",",i)
			print("Passagem: R$",a)
		elif(cd=='TEFE'):
			a = round(360, 2)
			print("Entradas: Tefe",",",i)
			print("Passagem: R$",a)
		else:
			a = round(550, 2)
			print("Entradas: Tabatinga",",",i)
			print("Passagem: R$",a)
	else:
		if(cd=='PORTOVELHO'):
			a = round((500-(p*500)), 2)
			print("Entradas: PortoVelho",",",i)
			print("Passagem: R$",a)
		elif(cd=="SANTAREM"):
			a = round((370-(p*370)), 2)
			print("Entradas: Santarem",",",i)
			print("Passagem: R$",a)
		elif(cd=='BELEM'):
			a = round((600-(p*600)), 2)
			print("Entradas: Belem",",",i)
			print("Passagem: R$",a)
		elif(cd=='TEFE'):
			a = round((360-(p*360)), 2)
			print("Entradas: Tefe",",",i)
			print("Passagem:",a)
		else:
			a = round((550-(p*550)), 2)
			print("Entradas: Tabatinga",",",i)
			print("Passagem:",a)
else:
	print("Entradas:",x,",",i)
	print("entradas invalidas")

#queria saber onde e o erro.