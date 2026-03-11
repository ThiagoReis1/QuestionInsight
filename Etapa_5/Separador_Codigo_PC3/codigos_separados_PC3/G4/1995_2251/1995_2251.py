amino = input("Nome do aminoacido: ").lower()
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794 
if(amino == "aspartato" or amino == "cisteina" or amino == "metionina"):
	if(amino=="aspartato"):
		peso = (c*4)+(h*6)+n+(o*4)
	elif(amino=="cisteina"):
		peso = (c*3)+(h*7)+n+(o*2)+s
	else:
		peso = (c*5)+(h*11)+n+(o*2)+s
	print(float(round(peso,2)))
else:
	print("Entrada:", amino)
	print("Dado Invalido")

		