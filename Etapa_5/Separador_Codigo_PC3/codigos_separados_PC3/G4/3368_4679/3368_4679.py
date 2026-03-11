C=(input("celsius?"))
T=float(input("temperatura?"))

if(C=="C"):
	K=T+273.15
	print(round(K,2))
else:
	C=T-273.15
	print(round(C,2))