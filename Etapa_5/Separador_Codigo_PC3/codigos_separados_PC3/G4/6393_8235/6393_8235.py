from numpy import*
v = array(eval(input("numerodevetores: ")))
s = zeros(size(v),dtype=int)

for i in range (size(v)):
	if v[i] == 9:
		s[i] = 0**2
	else: 
		s[i] =(v[i]+1)**3
print(s)
	
	
