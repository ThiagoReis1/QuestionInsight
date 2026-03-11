aminoacido = input("Digite um aminoacido:")
o = 15.9994
c = 12.011
n = 14.0067
e = 32.066
h = 1.0079

if(aminoacido.upper() == "ASPARTATO" or aminoacido.upper() == "FENILALANINA" or aminoacido.upper() == "TIROSINA"):
	if(aminoacido.upper() == "ASPARTATO"):
		peso_molecular = (c*4+h*6+n+o*4)
	elif(aminoacido.upper() == "FENILALANINA"):
		peso_molecular = (c*9+h*11+o*2+s)
	else:
		peso_molecular = (c*9+h*11+n+o*3)
										
	
else:
	print("Entrada: ", aminoacido.upper())
	print("Dado Invalido")
			
	
   

print(round(peso_molecular, 2))
													 