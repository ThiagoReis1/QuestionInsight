from numpy import*
v=input("digite o pais:").upper().split(',')
p = zeros(5,dtype=int)

for a in v:
	if (a=="BE"):
		p[0] = p[0]+1
	elif(a=="ES"):
		p[1] = p[1]+1
	elif(a=="FR"):
		p[2]=p[2]+1
	elif(a=="IT"):
		p[3]=p[3]+1
	elif(a=="PT"):
		p[4] = p[4]+1
print(max(p))
print(p)
		
		
		
		