#Digite um aminoacido:
amino = input("Aspartato/Fenilalanina/Tirosina").lower() 

#Atomos:
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.0079

if((amino != "aspartato") and (amino != "fenilalanina") and (amino != "tirosina")):
	print("Entrada:",amino)
	print("Dado Invalido")
	
elif(amino == "aspartato"):
	peso = (C*4) + (H*6) + N + (O*4)
	print(round(peso ,2))
	
elif(amino == "tirosina"):
	peso = (C*9) + (H*11) + N + (O*3)
	print(round(peso ,2))
	
elif(amino == "fenilalanina"):
	peso = (C*9) + (H*11) + (O*2) + S
	print(round(peso ,2))