qb=int(input("quantidade de bilhetes desejados: "))
ad=input("acomodacao desejada: ").lower()

if(ad!="rede")and(ad!="camarote")and(ad!="suite"):
	print("acomodacao invalida")
else:
	if(ad=="rede"):
		vt=qb*500.00
		print(round(vt, 2))
	elif(ad=="camarote"):
		vt=qb*1200.00
		print(round(vt, 2))
	elif(ad=="suite"):
		vt=qb*1500.00
		print(round(vt, 2))