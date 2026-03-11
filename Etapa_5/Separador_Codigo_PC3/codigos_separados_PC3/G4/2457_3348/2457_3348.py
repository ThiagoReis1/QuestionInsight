x=float(input("Quantidades de bilhetes:"))
tipo= input("Tipo de acomodacao:")
tipo= tipo.lower()
r=500
c=1200
s=1500
if(tipo=="rede"):
	msg= round((x*r),2)
elif(tipo=="camarote"):
	msg= round((x*c),2)
elif(tipo=="suite"):
	msg= round((x*s),2)
else:
	msg= "acomodacao invalida"
print(msg)