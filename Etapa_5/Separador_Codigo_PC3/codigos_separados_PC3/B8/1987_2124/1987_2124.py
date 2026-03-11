aminoacido=input("Digite um aminoacido:").upper()
if(aminoacido!="ALANINA" and  aminoacido!="VALINA" and aminoacido!="TIROSINA" ):
	print("Entrada:", aminoacido)
	print("Dado Invalido")
else:
	if(aminoacido=="ALANINA"):
		r=12.011*3+1.00794*7+14.00674+15.9994*2
		print(round(r,2))
	elif(aminoacido=="VALINA"):
		r=12.011*5+1.00794*11+14.00674+15.9994*2
		print(round(r,2))
	elif(aminoacido=="TIROSINA"):
		r=12.011*9+1.00794*11+14.00674+15.9994*3
		print(round(r,2))