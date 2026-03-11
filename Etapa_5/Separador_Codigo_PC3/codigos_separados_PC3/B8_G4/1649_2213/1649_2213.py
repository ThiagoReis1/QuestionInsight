from numpy import*
c=input(":").split(',')
p=zeros(5,dtype=int)
for i in range (size(c)):
	if c[i]=='P':
		p[0]+=1
	elif c[i]=='C':
		p[1]+=1
	elif c[i]=='M':
		p[2]+=1
	elif c[i]=='V':
		p[3]+=1
	elif c[i]=='A':
		p[4]+=1
print(max(p))
print(p)