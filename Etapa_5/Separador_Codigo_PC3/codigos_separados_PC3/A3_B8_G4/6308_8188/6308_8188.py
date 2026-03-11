from numpy import*
s=input("digite ").upper()
A=16.75
L=4.65
P=2.85
i=0
var=0
cont=0
cont1=0
cont2=0


while(i<len(s)):
	if(s[i]=="A"):
		cont=cont+1
		var=var+16.75
	elif(s[i]=="L"):
		cont1=cont1+1
		var=var+4.60
	elif(s[i]=="P"):
		cont2=cont2+1
		var=var+2.85
	i=i+1
print(round(var,2))
print(cont,cont1,cont2)

		