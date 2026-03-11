from numpy import *

t = input("T: ").upper()
out = zeros(4,dtype=int)
for i in range(len(t)):
	if t[i]=="A":
		out[0]+=1
	if t[i]=="P":
		out[1]+=1
	if t[i]=="D":
		out[2]+=1
	if t[i]=="M":
		out[3]+=1
		
print(out)		
	