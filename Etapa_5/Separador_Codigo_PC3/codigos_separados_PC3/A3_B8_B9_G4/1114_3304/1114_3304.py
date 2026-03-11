v =  float(input("Valocidade do trem: "))
t = float(input("Tempo de viagem: "))
e = t*v

if(e<=100):
	x = "Proxima parada: Avalon"
elif((e>100)and(e<=200)):
	x = "Proxima parada: Bravos"
if((e>200)and(e<=400)):
	x = "Proxima parada: Castamere"
if((e>400)and(c<=600)):
	x = "Proxima parada: Doriath"
if((e>600)and(c<=750)):
	x = "Proxima parada: Edoras"
if((e>750)and(e<=1150)):
	x = "Proxima parada: Gondor"
if((e>1150)and(e<=1400)):
	x = "Proxima parada: Hogsmead"
else:
	x = "Dados invalidos"

print("Entrada:", v,"km/h e", t,"h")
print(x)