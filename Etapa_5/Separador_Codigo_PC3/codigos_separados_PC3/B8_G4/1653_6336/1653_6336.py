from numpy import*
s = (input("digite a string: ")).split(',')

v = zeros(5, dtype = int)

for i in  range(len(s)):
	if s[i] ==  "AR":
		v[0] = v[0] + 1 
	elif s[i] == "BR":
		v[1] = v[1] + 1 
	elif s[i] == "CL":
		v[2] = v[2] + 1 
	elif s[i] == "CO":
		v[3] = v[3] + 1 	
	elif s[i] == "UY":
		v[4] = v[4] + 1 
	
print(max(v))  
print(v)
	
 		

