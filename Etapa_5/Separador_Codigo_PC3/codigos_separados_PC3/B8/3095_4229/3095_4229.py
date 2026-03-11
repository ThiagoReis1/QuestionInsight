a=input("Resultados: ")
V=3
E=2
D=1
somav=0
somad=0
somae=0
while(a!="X"):
	if(a.upper()=="V"):
		somav=somav+V
	elif(a.upper()=="D"):
		somad=somad+D
	elif(a.upper()=="E"):
		somae=somae+E
	a=input("Resultados: ")
print(somav)
print(somae)
print(somad)