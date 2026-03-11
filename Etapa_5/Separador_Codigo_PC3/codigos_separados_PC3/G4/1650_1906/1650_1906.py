from numpy import*
s = input("")
s = s.replace(",","")
n = zeros(5,dtype=int)
for i in range(0,len(s)):
	if(s[i] == "P"):
		n[0] = n[0] + 1
	elif(s[i] == "C"):
		n[1] = n[1] + 1
	elif(s[i] == "R"):
		n[2] = n[2] + 1
	elif(s[i] == "L"):
		n[3] = n[3] + 1
	else:
		n[4] = n[4] + 1
print(max(n))
print()
	