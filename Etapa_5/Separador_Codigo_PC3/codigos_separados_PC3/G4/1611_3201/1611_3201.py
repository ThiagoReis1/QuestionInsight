from numpy import*
s=input( ).upper()
v=float(s)
i=0
acum=0


while i<size(v):
	if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
		s[i]=0.15
	else:
		s[i]=0.17
	acum=acum+s[i]
	i=i+1
print(round(acum,2))