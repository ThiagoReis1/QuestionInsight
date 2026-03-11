a = float(input("Altura:"))
s = input("Sexo? ").upper()

if((1.0<a<2.5) and (s=="M")):
	pm=(((72.7)*a)-58)
	print(round(pm,2))
elif((1.0<a<2.5) and (s=="F")):
	pf=(((62.1)*a)-44.7)
	print(round(pf,2))
elif(s!="M" and s!="F"):
	print("codigo invalido de sexo")
else:
	print("altura invalida")