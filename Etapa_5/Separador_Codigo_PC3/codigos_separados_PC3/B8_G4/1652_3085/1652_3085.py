from numpy import *

s = input("digite a string: ").split(',')

v = zeros(5, dtype=int)

for i in range(len(s)):
	if(s[i] == "B"):
		v[0] = v[0] + 1
	elif(s[i] == "PA"):
		v[1] = v[1] + 1
	elif(s[i] == "PR"):
		v[2] = v[2] + 1
	elif(s[i] == "A"):
		v[3] = v[3] + 1
	elif(s[i] == "I"):
		v[4] = v[4] + 1
		
m = max(v)

print(m)
print(v)
	
	