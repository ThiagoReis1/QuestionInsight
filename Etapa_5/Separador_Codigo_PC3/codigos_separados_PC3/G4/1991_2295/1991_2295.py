aminoacido=input().upper()
o= 15.9994
c= 12.011
n= 14.00674
h= 1.0079
if(aminoacido == "GLICINA"):
	p=(c * 2) + (h * 5) + n + (o * 2)
	print(round(p,2))
elif(aminoacido == "PROLINA"):
	p = (c * 5) + (h * 10) + n + (o * 2)
	print(round(p,2))
elif(aminoacido == "SERINA"):
	p = (c * 3) + (h * 7) + n + (o * 3)
	print(round(p,2))
else:
	print("Entrada:",aminoacido)
	print("Dado Invalido")