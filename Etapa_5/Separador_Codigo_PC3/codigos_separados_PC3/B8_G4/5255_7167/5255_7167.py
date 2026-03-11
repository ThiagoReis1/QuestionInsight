peso=float(input("peso: "))
dist=float(input("distancia: "))
cod=int(input("codigo: "))
kg=25
km=0.10
if(cod==1):
	s=(peso*kg+dist*km)*(1.0+17/100)
	print(round(s,2))
elif(cod==2):
	s=(peso*kg+dist*km)*(1.0+17.5/100)
	print(round(s,2))
elif(cod==3):
	s=(peso*kg+dist*km)*(1.0+18/100)
	print(round(s,2))
elif(cod==4):
	s=(peso*kg+dist*km)*(1.0+20/100)
	print(round(s,2))
	