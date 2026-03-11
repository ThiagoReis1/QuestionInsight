
from numpy import*

s = input("digite: ")
s1 = s.split(',')
a = 0
b = 0
c = 0
d = 0
e = 0
vcont = zeros(size(s1),dtype=int)
for i in range(size(s1)):
	if(s1[i]=="AZ"):
		a = a + 1  
	elif(s1[i]=="CA"):
		b = b + 1
	elif(s1[i]=="FL"):
		c = c + 1
	elif(s1[i]=="PA"):
		d = d + 1
	else:
		e = e + 1
print(max(a,b,c,d,e))	
	
	
vcont = zeros(5,dtype=int)	

for i in range(size(s1)):
	if(s1[i]=="AZ"):
		vcont[0] = vcont[0] + 1
	elif(s1[i]=="CA"):
		vcont[1] = vcont[1] + 1
	elif(s1[i]=="FL"):
		vcont[2] = vcont[2] + 1
	elif(s1[i]=="PA"):
		vcont[3] = vcont[3] + 1
	else:
		vcont[4] = vcont[4] + 1
		
print(vcont)
		



