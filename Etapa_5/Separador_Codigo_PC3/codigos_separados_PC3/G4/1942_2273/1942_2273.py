#aminoacido 
amino= input("digite o aminoacido  :")

O= 15.999
C= 12.011
N= 14.00674
H=1.00794


if(amino.lower() == "histidina"): 
   x= (6*C) + (10*H) + (3*N) + (2*O)

else:
	x= (5*C) + (10*H) + (1*N) + (2*O)
	
print(round(x,2))	


