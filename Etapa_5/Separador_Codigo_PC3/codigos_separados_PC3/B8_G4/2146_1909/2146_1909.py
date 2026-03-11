from numpy import*
s = input()

for i in range(len(s)):
	if(s[i].isupper()==True):
		s = s + s[i].lower()
	elif(s[i].islower()==True):
		s = s + s[i].upper() 
print(s)
		
	