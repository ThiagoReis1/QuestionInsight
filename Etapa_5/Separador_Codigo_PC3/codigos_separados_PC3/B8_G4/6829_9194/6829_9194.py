s= input("inserir string:")
i=0
a=0

while i<len(s):
	if s[i]=="A":
		a+=19.90
	elif s[i]=="L":
		a+=3.50
	elif s[i]=="P":
		a+=4.25
	i+=1
	
print(round(a,2))