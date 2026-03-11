#Asparagina = C4+H8+N2+O3
#Glutamina = C5+H8+N1+O4
#Triptofano = C11+H11+N2+O2
f = input("Nome do aminoácido: ")
x=(f).upper()
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
if(x=="ASPARAGINA")or (x=="GLUTAMINA") or (x=="TRIPTOFANO"):
	if(x=="ASPARAGINA"):
		z=((c*4)+(h*8)+(n*2)+(o*3))
		print(round(z,2))
	elif(x=="GLUTAMINA"):
		z=((c*5)+(h*8)+(n*1)+(o*4))
		print(round(z,2))
	elif(x=="TRIPTOFANO"):
		z=((c*11)+(h*11)+(n*2)+(o*2))
		print(round(z,2))
else:
	print("Entrada:",f)
	print("Dado Invalido")