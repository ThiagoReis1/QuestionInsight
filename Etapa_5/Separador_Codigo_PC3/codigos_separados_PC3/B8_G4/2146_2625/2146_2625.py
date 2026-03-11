from numpy import*

v = input(" ")
v1 = ""
i = 0


while(i<len(v)):	
	if(v[i].islower()):
		v1 = v1 + v[i].upper()
	elif(v[i].isupper()):
		v1 = v1 + v[i].lower()
	i = i + 1
print(v1)