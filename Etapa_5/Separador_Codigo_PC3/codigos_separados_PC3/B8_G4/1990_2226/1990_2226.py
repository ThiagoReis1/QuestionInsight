am=input("nome do aminoacido").upper()

if((am=="GLUTAMINA") or (am=="SERINA") or (am=="TREONINA")):
	if(am=="GLUTAMINA"):
		x=((12.011*5)+(1.00794*8)+(14.0067*1)+(15.9994*4))
		print(round(x,2))
	elif(am=="SERINA"):
		y=((12.011*3)+(1.00794*7)+14.0067+(15.9994*3))
		print(round(y,2))
	elif(am=="TREONINA"):
		z=((12.011*4)+(1.00794*9)+14.0067+(15.9994*3))	
		print(round(z,2))
		
else:
	print("Entrada:", am)
	print("Dado Invalido")
