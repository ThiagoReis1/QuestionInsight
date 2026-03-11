tipo= input("").upper()
q= int(input())
r=int(input())
if(tipo=="L"):
	vt=(q*6)+(r*3)
	print(round(vt,2))
if(tipo=="P"):
	vt=(q*13.50)+(r*3)
	print(round(vt,2))
else:
	print("")
