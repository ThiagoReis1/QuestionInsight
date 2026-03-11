from numpy import*
s= input("secao?: ")
i=0
c=0
cont=0
cont2=0
cont3=0
while (i<len(s)):
	if(s[i] == "D"):
		c = c+2.25
		cont = cont+1
	elif (s[i] == "S"):
		c = c+4.0
		cont2 = cont2+1
	elif (s[i] == "I"):
		c = c+6.90
		cont3 = cont3+1
	i = i+1
c1=round(c,2)
print(c1,cont,cont2,cont3)
		