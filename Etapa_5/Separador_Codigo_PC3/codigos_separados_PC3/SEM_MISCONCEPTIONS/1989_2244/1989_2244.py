a= input("Aminoacido:").upper()
c=12.011
h=1.00794
n=14.00674
o=15.999
asparagina= (c*4) + (h*8) + (n*2) + (o*3)
glutamina= (c*5) + (h*8) + (n*1) + (o*4)
triptofano= (c*11) + (h*11) + (n*2) + (o*2)
if(a== "ASPARAGINA"):
	print(round(asparagina,2))
elif(a== "GLUTAMINA"):
	print(round(glutamina,2))
elif(a== "TRIPTOFANO"):
	print(round(triptofano,2))
else:
	print("Entrada:", a)
	print("Dado Invalido")