escolha=input("T OU S").upper()
q=int(input("quantidade"))
acai=int(input("quantidade"))
if(escolha)=="T":
	ccl=(3.50*q)+(acai*13)
else:
	ccl=(5*q)+(acai*13)
print(round(ccl,2))