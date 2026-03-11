aminoacido=input("digite o nome de aminoacido: ").lower()

o=15.9994
c=12.011
n=14.0067
s=32.066
h=1.0079

#Aspartato=(C*4)(H*6)(N*1)(O*4)
#Fenilalanina =(c*9)(h*11)(o*2)(s*1)
#Tirosina= (C*9)(H*11)(N*1)(O*3)
if ((aminoacido == "aspartato") or (aminoacido == "fenilalanina") or (aminoacido == "tirosina")):
	if(aminoacido=="aspartato"):
		cal=c*4+c*6+n*1+o*4
	elif(aminoacido=="fenilalanina"):
		cal=c*9+h*11+o*2+s*1
	elif(aminoacido=="tirosina"):
		cal=c*9+h*11+n*1+o*3
	print(round(cal,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")
	