ami = input("AMINOACIDO:").upper()


O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794

if(ami == "GLUTAMINA" or ami == "SERINA" or ami == "TREONINA"):
	if(ami == "GLUTAMINA"):
		calculo = round(((C*5) + (H*8) + (N*1) +(O*4)),2)
		print(calculo)
	elif(ami == "SERINA"):
		calculo = round(((C*3)+(H*7)+(N*1)+(O*3)),2)
		print(calculo)
	elif(ami == "TREONINA"):
		calculo = round(((C*4)+(H*9)+(N*1)+(O*3)),2)
		print(calculo)
else:
	print("Entrada:",ami)
	print("Dado Invalido")