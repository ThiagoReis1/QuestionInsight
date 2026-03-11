from numpy import*
x=input()

ve = x.split(',')
v2= zeros(5, dtype=int)

for c in ve:
	if c.upper() == "AR":
		v2[0]=v2[0]+1
	elif c.upper() == "BR":
		v2[1]=v2[1]+1
	elif c.upper() == "CL":
		v2[2]=v2[2]+1
	elif c.upper() == "CO":
		v2[3]=v2[3]+1
	elif c.upper()== "UY":
		v2[4]=v2[4]+1
		
print(max(v2))
print(v2)
