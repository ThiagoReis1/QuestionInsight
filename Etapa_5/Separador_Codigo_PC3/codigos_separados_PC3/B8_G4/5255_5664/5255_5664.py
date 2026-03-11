p= float(input('peso: '))
d= float(input('distancia: '))
c= int(input('codigo: '))

if c==1:
	ic=17
	s= (p*25+d*0.1)*(1+(ic/100))
	print(round(s,2))
	
elif c==2:
	ic=17.5
	s= (p*25+d*0.1)*(1+(ic/100))
	print(round(s,2))

elif c==3:
	ic=18
	s= (p*25+d*0.1)*(1+(ic/100))
	print(round(s,2))
	
elif c==4:
	ic=20
	s= (p*25+d*0.1)*(1+(ic/100))
	print(round(s,2))