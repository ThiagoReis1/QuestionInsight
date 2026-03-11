#from numpy import *

s = input("Digite uma palavra: ")

s1 = ""

for i in range(len(s)):
	if(s[i].isupper()):
		s1 = s1 + s[i].upper()
	elif(s[i].islower()):
		s1 = s1 + s[i].lower()

print(s1)
		
		

		
		
