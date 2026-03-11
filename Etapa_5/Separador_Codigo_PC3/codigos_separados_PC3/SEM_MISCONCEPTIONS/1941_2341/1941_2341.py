from math import*
amin=(input("digite amn:"))

O=12.011
C=1.0079
H=14.00674

glicina=(*2*O)+(5*C)+(2*H)
serina=(3*O)+(7*C)+(3*H)

if(amin.upper == "GLICINA"):
	print(round(glicina))
else:
	print(round(serina))