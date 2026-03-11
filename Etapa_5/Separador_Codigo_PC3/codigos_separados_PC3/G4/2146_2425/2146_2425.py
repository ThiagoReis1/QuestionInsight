s = input("s:")
ss = ''
for i in range(0, len(s)):
	if((s[i].islower())==0):
		ss = ss + s[i].lower()
	else:
		ss = ss + s[i].upper()
print(ss)
		
		