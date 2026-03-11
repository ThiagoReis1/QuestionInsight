p =float(input("Peso: "))
d=float(input("Distancia: "))
c= int(input("Codigo do estado: "))

#T= (p*25+d*0.10) * (1+(i/100))

if (c==1):
	i=17
	T = (p*25+d*.10) * (1+i/100)
	print(round(T,2))
elif (c==2):
	i=17.5
	T=(p*25+d*0.10) * (1 + i/100)
	print(round(T,2))
elif (c==3):
	i=18
	T=(p*25+d*0.10) * (1+i/100)
	print(round(T,2))
elif (c==4):
	i=20
	T=(p*25+d*0.10) * (1+i/100)
	print(round(T,2))