mi=input("milhas:")
dis=float(input("distancia"))
if(mi=="M"):
	mi1=dis*1.60934
	print(round(mi1, 2))

else:
	km=dis/1.60934
	
	print(round(km, 2))
	
