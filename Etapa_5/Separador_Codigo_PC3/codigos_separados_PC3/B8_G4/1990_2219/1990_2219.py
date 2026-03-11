aminoacido = input("Informe o aminoacido:").upper()
O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794
if(aminoacido == "GLUTAMINA" or aminoacido =="SERINA" or aminoacido=="TREONINA" ):
	if (aminoacido =="GLUTAMINA"):
		calc = (C*5)+(H*8)+(N*1)+(O*4)
	elif(aminoacido=="SERINA"):
		calc = C*3+ H*7+ N+ O*3
	elif (aminoacido=="TREONINA"):
		calc = C*4+ H*9+ N+ O*3
		
	print(round(calc,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")