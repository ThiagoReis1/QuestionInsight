import math

molecula= input()
o=15.999
c=12.011
n=14.00674
h=1.00794

if(molecula.upper()=="ASPARAGINA"):
		molecula=((c*4) + (h*8) +(n*2) + (o*3))
		print(molecula,2)
elif(molecula.upper()=="GLUTAMINA"):
		molecula =((5*c)+(8*h)+(1*n)+(4*o))
		print(molecula,2)
elif(molecula.upper()=="TRIPTOFANO"):
		molecula= ((11*c)+(11*h)+(2*n)+(2*o))
		print(molecula,2)
else:
	print("Dado Invalido")
	