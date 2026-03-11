from numpy import*

v= eval(input("vetores:"))

s=[]

for i in range(size(v)):
	 if(v[i]!=0):
			s.append(v[i])
for i in range(size(v)):
	if(v[i] == 0):
		s.append(v[i])
print(array(s))