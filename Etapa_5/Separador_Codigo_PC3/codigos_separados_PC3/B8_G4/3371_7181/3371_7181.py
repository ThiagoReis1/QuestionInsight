med=input("K para quilometro M para milhas:  ")

if(med.upper()=="M"):  
	ml=float(input("entre com as milhas:  "))
	km=1.60934*ml
	print(round(km, 2))
else:
	if(med.upper()=="K"):
		km=float(input("entre com os km:  "))
		ml=km/1.60934
		print(round(ml, 2))