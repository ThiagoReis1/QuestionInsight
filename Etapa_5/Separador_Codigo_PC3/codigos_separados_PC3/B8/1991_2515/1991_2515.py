aminoacido=input("Qual eh o nome do aminoacido?")
O=15.9994
C=12.011
N=14.00674
H=1.0079
pesoglicina=(2*C)+(5*H)+N+(2*O)
pesoprolina=(5*C)+(10*H)+N+(2*O)
pesoserina=(3*C)+(7*H)+N+(3*O)
if(aminoacido=="glicina".upper()):
	print(round(pesoglicina,2))
elif(aminoacido=="prolina".upper()):
	print(round(pesoprolina,2))
elif(aminoacido=="serina".upper()):
	print(round(pesoserina,2))
else:
	if((aminoacido!="glicina") and (aminoacido!="prolina") and (aminoacido!="serina")):
		print("Entrada:",aminoacido)
		print("Dado Invalido")