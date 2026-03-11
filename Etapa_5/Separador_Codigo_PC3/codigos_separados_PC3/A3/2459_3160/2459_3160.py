peso = float(input("peso:"))
distancia = float(input("distancia:"))
codigo = float(input("codigo:"))
if(codigo==1):
	s= (peso*25) + (distancia*0.10)
	icms= s/0.17
	sf= s*(1+icms/100)
	print(round(icms,2))
if(codigo==2):
	s= (peso*25) + (distancia*0.10)
	icms= s/0.175
	sf= s*(1+icms/100)
	print(round(icms,2))
if(codigo==3):
	s= (peso*25) + (distancia*0.10)
	icms= s/0.18
	sf= s*(3+icms/100)
	print(round(icms,2))
if(codigo==4):
	s= (peso*25) + (distancia*0.10)
	icms= s/0.2
	sf= s*(4+icms/100)
	print(round(icms,2))