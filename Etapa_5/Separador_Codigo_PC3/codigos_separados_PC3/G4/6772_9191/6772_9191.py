V=float(input("valor total da compra:"))
C=input("D/P/C1/C2?:")

if C=="D" or C=="P":
	x=V*0.83

elif C=="C1":
	x=V
	
else:
	x=V*1.08

print(round(x,2))
