from numpy import*
s=input("digite a senha: ").upper()
i=0
vu=0
cont1=0
cont2=0
total=0
while (i<len(s)):
	if ((s[i]=="A") or (s[i]=="E") or (s[i]=="I") or (s[i]=="O") or (s[i]=="U")):
		vu=3.15
		cont1=cont1+vu
	else:
		vu=4.17
		cont2=cont2+vu
	total=cont1+cont2
	i=i+1
print(round(total,2))
		
		