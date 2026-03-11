from numpy import * 
s = input("rotulo da etiqueta: ")
i = 0
s = s.lower()
a = 15/100
b = 17/100
while(i<len(s)):
	if(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
		s = s.replace(s[i],str(a))
		i = i + 1
	else:
		s = s.replace(s[i],str(b))
		i = i + 1
print(round(sum(s), 2))