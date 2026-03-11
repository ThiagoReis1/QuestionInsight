from numpy import *
s = input("Digite a string: ")
si = ""
for i in range(len(s)):
	if(s[i].isupper()):
		si=si + s[i].lower() 
	elif(s[i].islower):
		si = si + s[i].upper() 
print(si)
