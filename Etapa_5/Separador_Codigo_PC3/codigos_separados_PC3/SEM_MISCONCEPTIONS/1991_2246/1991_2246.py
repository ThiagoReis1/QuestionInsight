a= input("aminoacido:").upper()
o= 15.9994
c= 12.011
n= 14.00674
h= 1.0079

glicina = (c*2)+(h*5)+(n*1)+(o*2)
prolina = (c*5)+(h*10)+(n*1)+(o*2)
serina= (c*3)+(h*7)+(n*1)+(o*3)

if(a=="GLICINA"):
	print(round(glicina,2))
elif(a=="PROLINA"):
	print(round(prolina,2))
elif(a=="SERINA"):
	print(round(serina,2))
else:
	print("Entrada:",a)
	print("Dado Invalido")