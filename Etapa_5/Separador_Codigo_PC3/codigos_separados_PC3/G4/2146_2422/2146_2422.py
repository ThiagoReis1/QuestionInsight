from numpy import*
s = input(":")
for i in range(len(s)):
	if(s[i].islower() == True):
		s[i] = s[i].upper()
	if(s[i].isupper() == True):
		s[i] = s[i].lower()
print(s)
	


