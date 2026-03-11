b=float(input("insira a quantidade de bilhetes"))
a=(input("insira o tipo de acomodacao"))
if(a=="rede"):
	print(round(float(b*500),2))
elif(a=="camarote"):	
   print(round(float(b*1200),2))
elif(a=="suite"):
   print(round(float(b*1500),2))
else:
	print("acomodacao invalida")