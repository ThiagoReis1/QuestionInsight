v= float(input("Velocidade: "))
t= float(input("tempo: "))
d= v*t
if((v<=0) or (t<0)):
	y= "Dados invalidos"
	
elif((d>0) and (d<100)):
	y= "Proxima parada: Bravos"
elif((d>=100) and (d<200)):
	y= "Proxima parada: Castamere"
elif((d>=200) and (d<400)):
	y= "Proxima parada: Doriath"
elif((d>=400) and (d<600)):
	y="Proxima parada: Edoras"
elif((d>=600) and (d<750)):
	y="Proxima parada: Fangorn"
elif((d>=750) and (d<1150)):
	y="Proxima parada: Gondor"
else:
	y="Proxima parada: Hogsmead"
	
print("Entradas:", v, "km/h e", t, "h")
print(y)
	