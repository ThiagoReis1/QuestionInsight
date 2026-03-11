a=float(input("altura:"))
b=input("sexo:")
c=(72.7*a)-58
d=(62.1*a)-44.7
if(a<1.0) and (a>2.5):
	print("altura invalida")
elif(b!="M")and(b!="F"):
	print("codigo invalido de sexo")
elif(b=="M"):
	print(round(c, 2))
else:
	print(round(d, 2))