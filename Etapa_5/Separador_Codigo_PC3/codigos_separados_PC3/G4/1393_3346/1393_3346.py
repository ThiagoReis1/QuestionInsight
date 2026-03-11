g=float(input("gramas:"))
tf=60.00
c1=0.05*g
c2=0.04*g+tf
if(g<=4999.9):
	print(round(c1,2))
else:
	print(round(c2,2))