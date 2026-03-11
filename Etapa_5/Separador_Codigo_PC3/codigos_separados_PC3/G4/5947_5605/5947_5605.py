CS=input("")
Q=int(input(""))
Qs=int(input(""))
C = 2.00
E = 4.50
S= 6.00
vf= Q * C + Qs * S
vfa= Q * E + Qs* S
if(CS == "C"):
	print(round(vf,2))

else:
	print(round(vfa,2))