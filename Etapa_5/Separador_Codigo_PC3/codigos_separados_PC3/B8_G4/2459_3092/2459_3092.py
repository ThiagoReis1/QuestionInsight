p=float(input("p?"))
d=float(input("d?"))
cod=int(input("cod?"))

ckg=25
ckm=0.10

if(cod==1):
	x=17.0
	s=((p*ckg)+(d*ckm))*((x/100)+1)
elif(cod==2):
	x=17.5
	s=((p*ckg)+(d*ckm))*((x/100)+1)
elif(cod==3):
	x=18.0
	s=((p*ckg)+(d*ckm))*((x/100)+1)
elif(cod==4):
	x=20.0
	s=((p*ckg)+(d*ckm))*((x/100)+1)

print(round(s,2))
