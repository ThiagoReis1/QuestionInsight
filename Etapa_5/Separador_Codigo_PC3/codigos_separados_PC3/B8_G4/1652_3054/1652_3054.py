from numpy import*

v = input("n: ").split(',')
s = zeros(5, dtype = int)

for i in v:
	if i == "B":
		s[0]= s[0] + 1
	elif i == "PA":
		s[1] = s[1] + 1
	elif i == "PR":
		s[2] = s[2] + 1
	elif i == "A":
		s[3] = s[3] + 1
	elif i == "I":
		s[4] = s[4] + 1
print(max(s))
print(s)
		
	
	
	

