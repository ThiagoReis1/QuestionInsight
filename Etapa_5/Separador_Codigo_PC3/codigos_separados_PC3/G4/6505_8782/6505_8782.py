tc=input("A,B,C: ").upper()
Q=int(input("quantidade: "))
if(tc)== "C":
	tt=30*Q
	ccl1=tt*(15/100)
	ccl=tt-ccl1
else:
	ccl=30*Q
print(round(ccl,2))
