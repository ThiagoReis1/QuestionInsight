amino = input()

aux = amino

amino = amino.lower()

aspartato=((4* 12.011)+(6*1.0079)+(14.0067)+(4*15.9994))
fenilalanina= ((9*12.011)+(11*1.0079)+(2*15.9994)+(32.066))
tirosina= ((9*12.011)+(11*1.0079)+(14.0067)+(3*15.9994))
if(amino == "aspartato" ):
	print(round(aspartato, 2 ))
elif(amino == "fenilalanina"):
	print(round(fenilalanina, 2))
elif(amino == "tirosina"):
	print(round(tirosina, 2 ))
else:
	print("Entrada:",aux)
	print("Dado Invalido")