from numpy import*
s = input("nacionalidades: ").upper().split(',')
r = zeros(5,dtype=int)

for i in range(len(s)):
	if (s[i]=="AR"):
		r[0] = r[0] + 1
	elif(s[i]=="BR"):
		r[1] = r[1] + 1
	elif(s[i]=="CL"):
		r[2] = r[2] + 1
	elif(s[i]=="CO"):
		r[3] = r[3] + 1
	elif(s[i]=="UY"):
		r[4] = r[4] + 1
print(max(r))
print(r)
