q=int(input("bilhetes:"))
t=input("tipo de acomodacao:")
if(t=="rede"):
	x=q*500.00
	print(round(x,2))
elif(t=="camarote"):
	x=q*1200.00
	print(round(x,2))
elif(t=="suite"):
	x=q*1500.00
	print(round(x,2))
else:
	print("acomodacao invalida")