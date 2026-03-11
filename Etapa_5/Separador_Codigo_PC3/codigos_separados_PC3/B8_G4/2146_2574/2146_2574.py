from numpy import*
s = input("Insira uma string: ")

ss = ""

for i in range(len(s)):
	if(s[i].islower()):
		ss = ss + s[i].upper()
	elif(s[i].isupper()):
		ss = ss + s[i].lower()

	
print(ss)

