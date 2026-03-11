from numpy import*

x = input("estado").split(',')
p =zeros(5,dtype=int)

for i in range(size(x)):
	if x[i] == "AC":
		p[0] = p[0]+1
	elif x[i] == "AM":
		p[1] = p[1]+1
	elif x[i] == "PA":
		p[2] = p[2]+1
	elif x[i] =="RO":
		p[3] = p[3]+1
	elif x[i] == "RR":
		p[4] = p[4]+1
		
print(max(p))
print(p)