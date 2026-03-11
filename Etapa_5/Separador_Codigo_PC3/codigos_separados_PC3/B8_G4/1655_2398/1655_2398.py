from numpy import*
n = input()
s = n.split(',')
z = zeros(5, int)
for i in range(size(s)):
	if(s[i]=="AC"):
		z[0] = z[0]+1
	elif(s[i]=="AM"):
		z[1] = z[1]+1
	elif(s[i]=="PA"):
		z[2] = z[2]+1
	elif(s[i]=="RO"):
		z[3] = z[3]+1
	elif(s[i]=="RR"):
		z[4] = z[4]+1
m = max(z)
print(m)
print(z)