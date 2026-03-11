p=float(input(":"))
d=float(input(":"))
c=input(":")



if(c==1):
	s= ((p*25) + (d*0.10))*(1.0 + (17.0/100))
	print(round(s,2))
elif(c==2):
	s=((p*25) + (d*0.10))*(1.0 + (17.5/100))
	print(round(s,2))
elif(c==3):
	s=((p*25) + (d*0.10))*(1.0 + (18.0/100))
	print(round(s,2))
elif(c==4):
	s=((p*25) + (d*0.10))*(1.0 + (20.0/100))
	print(round(s,2))