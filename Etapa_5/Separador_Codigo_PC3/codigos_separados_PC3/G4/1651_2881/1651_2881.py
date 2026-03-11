from numpy import *
tdp = (input("")).split(",")
z = zeros(6, dtype=int)
for i in range(size(tdp)):
	if tdp[i]=="MC":
		z[0]+=1
	if tdp[i]=="C":
		z[1]+=1
	if tdp[i]=="CM":
		z[2]+=1
	if tdp[i]=="EM":
		z[3]+=1
	if tdp[i]=="E":
		z[4]+=1
	if tdp[i]=="ME":
		z[5]+=1

print(max(z))
print(z)